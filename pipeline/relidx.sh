#!/usr/bin/env bash
# relidx.sh — restore/upload a big LanceDB index dir as a GitHub Release, auto-splitting into
# <2GB parts (GitHub caps a single Release asset at 2GB). Backward-compatible: under the limit it
# uploads/restores a single <name>.tar.gz exactly as before; over it, <name>.tar.gz.part-NN.
#
#   relidx.sh restore <release> <dir>            # e.g. relidx.sh restore irindex pipeline/state/irdb
#   relidx.sh upload  <release> <dir> [title]
# Needs: gh (GH_TOKEN), tar, split. No-op-safe: restore exits 0 if the release/asset is absent.
set -euo pipefail
PART_MAX=1900m            # split chunk size (< the 2GB single-asset ceiling)
SPLIT_AT=1990000000      # bytes: split the tarball above this

cmd="${1:?restore|upload}"; release="${2:?release name}"; dir="${3:?index dir}"
base="$(basename "$dir")"; parent="$(dirname "$dir")"; tar="${base}.tar.gz"

fsize() { stat -c%s "$1" 2>/dev/null || stat -f%z "$1"; }

case "$cmd" in
  restore)
    mkdir -p "$parent"; tmp="$(mktemp -d)"
    if gh release download "$release" -p "$tar" -D "$tmp" 2>/dev/null; then
      tar -C "$parent" -xzf "$tmp/$tar"
    elif gh release download "$release" -p "${tar}.part-*" -D "$tmp" 2>/dev/null; then
      cat "$tmp/${tar}".part-* | tar -C "$parent" -xz       # glob sorts part-00,part-01,…
    else
      echo "relidx: no '$release' release/asset yet — skip"; rm -rf "$tmp"; exit 0
    fi
    rm -rf "$tmp"; echo "relidx: restored $release -> $dir ($(du -sh "$dir" 2>/dev/null | cut -f1))"
    ;;
  upload)
    title="${4:-$release index}"; tmp="$(mktemp -d)"
    tar -czf "$tmp/$tar" -C "$parent" "$base"
    sz="$(fsize "$tmp/$tar")"
    gh release view "$release" >/dev/null 2>&1 || gh release create "$release" -t "$title" -n "auto-updated index" >/dev/null
    # clear stale assets (single + any parts) so old layout never lingers
    for a in $(gh release view "$release" --json assets --jq '.assets[].name' 2>/dev/null | grep -E "^${tar}(\.part-[0-9]+)?$" || true); do
      gh release delete-asset "$release" "$a" -y 2>/dev/null || true
    done
    if [ "$sz" -lt "$SPLIT_AT" ]; then
      gh release upload "$release" "$tmp/$tar"
      echo "relidx: uploaded $release ($((sz/1000000))MB, single)"
    else
      ( cd "$tmp" && split -b "$PART_MAX" -d -a 2 "$tar" "${tar}.part-" )
      gh release upload "$release" "$tmp/${tar}".part-*
      echo "relidx: uploaded $release ($((sz/1000000))MB, $(ls "$tmp/${tar}".part-* | wc -l | tr -d ' ') parts)"
    fi
    rm -rf "$tmp"
    ;;
  *) echo "usage: relidx.sh restore|upload <release> <dir> [title]"; exit 2 ;;
esac
