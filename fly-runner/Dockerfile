# Self-hosted GitHub Actions runner for the Fintech Radar pipeline, running on a Fly.io Machine.
# Bakes in every tool the workflows use (python, node, gh, rclone, claude-code, pip deps) so job
# runs don't reinstall each time. Registers itself against the repo at boot via a PAT (see entrypoint).
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# base tooling + runner runtime deps (libicu/liblttng for the .NET-based runner)
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl wget git jq unzip tar sudo gnupg build-essential \
      python3 python3-pip python3-venv \
      libicu70 liblttng-ust1 \
 && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs \
 && install -m 0755 -d /etc/apt/keyrings \
 && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg -o /etc/apt/keyrings/gh.gpg \
 && chmod go+r /etc/apt/keyrings/gh.gpg \
 && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/gh.gpg] https://cli.github.com/packages stable main" > /etc/apt/sources.list.d/gh.list \
 && apt-get update && apt-get install -y gh \
 && curl -fsSL https://rclone.org/install.sh | bash \
 && npm install -g @anthropic-ai/claude-code \
 && rm -rf /var/lib/apt/lists/*

# pipeline python deps (matches pipeline/semsearch/requirements.txt + pymupdf for IR PDF text)
RUN pip3 install --no-cache-dir "lancedb>=0.33" python-frontmatter pymupdf pyarrow

# non-root runner user (the Actions runner refuses to run as root)
RUN useradd -m -s /bin/bash runner && echo "runner ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/runner
USER runner
WORKDIR /home/runner/actions-runner

# install the latest linux-x64 Actions runner
RUN V=$(curl -fsSL https://api.github.com/repos/actions/runner/releases/latest | jq -r .tag_name | sed 's/^v//') \
 && curl -fsSL -o r.tgz "https://github.com/actions/runner/releases/download/v${V}/actions-runner-linux-x64-${V}.tar.gz" \
 && tar xzf r.tgz && rm r.tgz

COPY --chown=runner:runner entrypoint.sh /home/runner/entrypoint.sh
RUN sudo chmod +x /home/runner/entrypoint.sh
ENTRYPOINT ["/home/runner/entrypoint.sh"]
