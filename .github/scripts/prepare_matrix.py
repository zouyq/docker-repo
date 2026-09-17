#!/usr/bin/env python3
"""Filter the build matrix: skip images whose upstream has not changed."""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATRIX_FILE = ROOT / ".github" / "build-matrix.json"
VERSIONS_FILE = ROOT / "build-versions.json"
BASE_DIR = "zouyq"


def load_json(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def dockerfile_hash(item: dict) -> str:
    path = ROOT / BASE_DIR / item["dir"] / item["dockerfile"]
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_upstream_sha(url: str, ref: str) -> str:
    if ref in ("", "HEAD", "head"):
        cmd = ["git", "ls-remote", url, "HEAD"]
    else:
        cmd = ["git", "ls-remote", url, f"refs/tags/{ref}", f"refs/heads/{ref}", ref]
    try:
        out = subprocess.check_output(cmd, text=True, timeout=60).strip()
    except Exception as exc:
        print(f"::warning::ls-remote failed for {url} {ref}: {exc}", file=sys.stderr)
        return ""
    if not out:
        return ""
    # Prefer the first exact line
    return out.splitlines()[0].split()[0]


def main() -> None:
    force = os.environ.get("FORCE", "false").lower() == "true"
    only_raw = os.environ.get("ONLY", "").strip()
    only = {x.strip() for x in only_raw.split(",") if x.strip()}

    matrix = load_json(MATRIX_FILE, [])
    state = load_json(VERSIONS_FILE, {"images": {}, "history": []})
    images = state.get("images") or {}

    selected = []
    for item in matrix:
        name = item["name"]
        if only and name not in only:
            continue

        entry = dict(item)
        entry["dockerfile_sha"] = dockerfile_hash(item)
        prev = images.get(name) or {}

        if force:
            entry["upstream_sha"] = resolve_upstream_sha(item.get("upstream") or "", item.get("upstream_ref") or "HEAD")
            entry["force"] = True
            selected.append(entry)
            print(f"include {name}: force")
            continue

        if item.get("upstream"):
            sha = resolve_upstream_sha(item["upstream"], item.get("upstream_ref") or "HEAD")
            entry["upstream_sha"] = sha
            last_sha = prev.get("upstream_sha") or ""
            last_status = prev.get("status") or ""
            if sha and sha == last_sha and last_status == "success":
                print(f"skip {name}: upstream unchanged ({sha[:12]})")
                continue
            selected.append(entry)
            print(f"include {name}: upstream={sha[:12] or 'unknown'} last_status={last_status or 'none'}")
            continue

        # No upstream repo: rebuild only when the local Dockerfile changed.
        last_df = prev.get("dockerfile_sha") or ""
        last_status = prev.get("status") or ""
        entry["upstream_sha"] = ""
        if entry["dockerfile_sha"] and entry["dockerfile_sha"] == last_df and last_status == "success":
            print(f"skip {name}: Dockerfile unchanged")
            continue
        selected.append(entry)
        print(f"include {name}: dockerfile changed or not yet built")

    out_path = Path(os.environ.get("GITHUB_OUTPUT", "/dev/null"))
    matrix_json = json.dumps(selected, separators=(",", ":"))
    has_work = "true" if selected else "false"
    with out_path.open("a", encoding="utf-8") as f:
        f.write(f"has_work={has_work}\n")
        f.write(f"matrix={matrix_json}\n")

    print(f"selected {len(selected)} / {len(matrix)} images")
    Path("/tmp/selected-matrix.json").write_text(matrix_json, encoding="utf-8")


if __name__ == "__main__":
    main()
