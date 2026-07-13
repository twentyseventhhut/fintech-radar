#!/usr/bin/env python3
"""drive_map.py — build the path -> Google Drive link map for the IR redirect.

Drive addresses files by opaque ID, not by path, so we enumerate the shared folder ONCE via the
Drive API (metadata only — no downloads), reconstruct each file's path from its parent chain (the
Drive tree mirrors the local `data/<slug>/...` layout), and emit:

  pipeline/ir/drive_map.json :  { "<rel_path>": {"file_id","webViewLink","size","md5"} }

This joins to the index by the relative `note_path` already stored in every row — so the redirect is
a thin lookup layered on top; the index is NOT rebuilt. Re-run anytime / incrementally after new files.

Auth: a Google service account with Drive API enabled, and the IR-dataset folder SHARED to its email.
  GOOGLE_APPLICATION_CREDENTIALS=/path/to/sa.json   (or GDRIVE_SA_KEY = the JSON itself, for CI)
  IR_DRIVE_FOLDER = <root folder id>   (the folder whose children are data/, registry/, …)

Usage: python3 pipeline/ir/drive_map.py --folder <id> [--out pipeline/ir/drive_map.json]
Deps (install when running): google-api-python-client google-auth
"""
import argparse, json, os, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIELDS = "nextPageToken, files(id,name,mimeType,parents,size,md5Checksum,webViewLink)"
FOLDER_MIME = "application/vnd.google-apps.folder"


def from_rclone(remote):
    """Build the map from `rclone lsjson` (OAuth — no service-account key, no org-policy conflict).
    Returns {rel_path: {file_id, webViewLink, size, md5}}. remote e.g. 'irdrive:' or 'irdrive:IR-dataset'."""
    out = subprocess.run(["rclone", "lsjson", "--recursive", "--files-only",
                          "--hash", remote], capture_output=True, text=True, check=True)
    m = {}
    for f in json.loads(out.stdout):
        fid = f.get("ID", "")
        if not fid:
            continue
        m[f["Path"]] = {"file_id": fid,
                        "webViewLink": f"https://drive.google.com/file/d/{fid}/view",
                        "size": f.get("Size", 0),
                        "md5": (f.get("Hashes") or {}).get("md5", "")}
    return m


def _service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    raw = os.environ.get("GDRIVE_SA_KEY")
    if raw:
        info = json.loads(raw)
        creds = service_account.Credentials.from_service_account_info(
            info, scopes=["https://www.googleapis.com/auth/drive.readonly"])
    else:
        p = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if not p or not os.path.exists(p):
            sys.exit("set GDRIVE_SA_KEY (JSON) or GOOGLE_APPLICATION_CREDENTIALS=/path/sa.json")
        creds = service_account.Credentials.from_service_account_file(
            p, scopes=["https://www.googleapis.com/auth/drive.readonly"])
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def crawl(svc, root):
    """BFS the folder tree -> {rel_path: meta}. rel_path is relative to `root` (e.g. data/apple/...)."""
    out, stack = {}, [(root, "")]
    while stack:
        fid, prefix = stack.pop()
        token = None
        while True:
            resp = svc.files().list(
                q=f"'{fid}' in parents and trashed=false",
                fields=FIELDS, pageSize=1000, pageToken=token,
                supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
            for f in resp.get("files", []):
                rel = f"{prefix}/{f['name']}" if prefix else f["name"]
                if f["mimeType"] == FOLDER_MIME:
                    stack.append((f["id"], rel))
                else:
                    out[rel] = {"file_id": f["id"], "webViewLink": f.get("webViewLink", ""),
                                "size": int(f["size"]) if f.get("size", "").isdigit() else 0,
                                "md5": f.get("md5Checksum", "")}
            token = resp.get("nextPageToken")
            if not token:
                break
            if len(out) % 2000 == 0:
                print(f"  crawled {len(out)} files…", flush=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", default=os.environ.get("IR_DRIVE_FOLDER"),
                    help="root Drive folder id (children = data/, registry/, …)")
    ap.add_argument("--out", default=os.path.join(REPO, "pipeline", "ir", "drive_map.json"))
    ap.add_argument("--merge", action="store_true", help="merge into the existing map (incremental)")
    ap.add_argument("--from-rclone", default=os.environ.get("RCLONE_REMOTE"),
                    help="build via `rclone lsjson <remote>` (OAuth, no SA key) — RECOMMENDED")
    a = ap.parse_args()
    if a.from_rclone:
        found = from_rclone(a.from_rclone)          # OAuth path — no service-account key needed
    elif a.folder:
        found = crawl(_service(), a.folder)         # service-account path (needs a downloadable key)
    else:
        sys.exit("pass --from-rclone <remote> (recommended) or --folder <id> (service-account)")
    # the tree may be rooted at the IR-dataset folder; index note_paths start at 'data/...'.
    # keep keys as-is; the resolver tries both '<rel>' and 'data/<...>' forms.
    if a.merge and os.path.exists(a.out):
        base = json.load(open(a.out)); base.update(found); found = base
    json.dump(found, open(a.out, "w"), ensure_ascii=False, indent=0)
    print(f"drive_map: {len(found)} files -> {a.out}")


if __name__ == "__main__":
    main()
