#!/usr/bin/env python3
"""Merge per-image build results into build-versions.json and regenerate README.md."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERSIONS_FILE = ROOT / "build-versions.json"
README_FILE = ROOT / "README.md"
RESULTS_DIR = Path(os.environ.get("RESULTS_DIR", "/tmp/build-results"))
BASE_DIR = "zouyq"
HISTORY_LIMIT = 500


def load_json(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def short_sha(sha: str, n: int = 10) -> str:
    return sha[:n] if sha else "-"


def upstream_label(item: dict) -> str:
    url = item.get("upstream") or ""
    if not url:
        return "-"
    return url.removeprefix("https://github.com/").removesuffix(".git")


def render_readme(state: dict) -> str:
    history = state.get("history") or []
    images = state.get("images") or {}

    lines = [
        "# 镜像构建记录",
        "",
        "本文件由 GitHub Actions 自动更新，请勿手动编辑。",
        "",
        "规则：若上游仓库 commit（或无上游时的 Dockerfile 内容）与上次成功构建一致，则跳过本次构建。",
        "",
        f"最近更新：{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
        "## 当前状态",
        "",
        "| 镜像 | 上游 | 上游 Commit | 上次构建 (UTC) | 状态 |",
        "|------|------|-------------|----------------|------|",
    ]

    for name in sorted(images.keys()):
        info = images[name]
        sha = info.get("upstream_sha") or ""
        built = info.get("built_at") or "-"
        status = info.get("status") or "-"
        if sha and info.get("upstream"):
            sha_cell = f"[`{short_sha(sha)}`]({info['upstream'].removesuffix('.git')}/commit/{sha})"
        elif sha:
            sha_cell = f"`{short_sha(sha)}`"
        else:
            sha_cell = "-"
        lines.append(
            f"| `{name}` | {upstream_label(info)} | {sha_cell} | {built} | {status} |"
        )

    lines.extend(
        [
            "",
            "## 构建历史（按时间倒序）",
            "",
            "| 构建时间 (UTC) | 镜像 | 拉取地址 | 上游 Commit | 平台 | 状态 | Workflow |",
            "|----------------|------|----------|-------------|------|------|----------|",
        ]
    )

    for row in history:
        ts = row.get("built_at") or "-"
        name = row.get("name") or "-"
        image = row.get("image") or "-"
        platforms = row.get("platforms") or "-"
        status = row.get("status") or "-"
        sha = row.get("upstream_sha") or ""
        run_url = row.get("run_url") or ""
        upstream = row.get("upstream") or ""

        if sha and upstream:
            sha_cell = f"[`{short_sha(sha)}`]({upstream.removesuffix('.git')}/commit/{sha})"
        elif sha:
            sha_cell = f"`{short_sha(sha)}`"
        else:
            sha_cell = "-"

        run_cell = f"[运行]({run_url})" if run_url else "-"
        lines.append(
            f"| {ts} | `{name}` | `{image}` | {sha_cell} | {platforms} | {status} | {run_cell} |"
        )

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    state = load_json(VERSIONS_FILE, {"images": {}, "history": []})
    state.setdefault("images", {})
    state.setdefault("history", [])

    if not RESULTS_DIR.exists():
        print(f"no results dir: {RESULTS_DIR}")
        README_FILE.write_text(render_readme(state), encoding="utf-8")
        return

    results = sorted(RESULTS_DIR.glob("*.json"))
    for path in results:
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"::warning::bad result {path}: {exc}")
            continue

        name = rec.get("name")
        if not name:
            continue

        history_row = {
            "name": name,
            "image": rec.get("image") or f"docker.io/*/{name}",
            "upstream": rec.get("upstream") or "",
            "upstream_sha": rec.get("upstream_sha") or "",
            "dockerfile_sha": rec.get("dockerfile_sha") or "",
            "platforms": rec.get("platforms") or "",
            "status": rec.get("status") or "failure",
            "built_at": rec.get("built_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "run_url": rec.get("run_url") or "",
            "error": rec.get("error") or "",
        }
        state["history"].append(history_row)

        # Only refresh "current" pointer on success, or first failure record.
        prev = state["images"].get(name) or {}
        if history_row["status"] == "success" or not prev:
            state["images"][name] = {
                "upstream": history_row["upstream"],
                "upstream_sha": history_row["upstream_sha"],
                "dockerfile_sha": history_row["dockerfile_sha"],
                "platforms": history_row["platforms"],
                "status": history_row["status"],
                "built_at": history_row["built_at"],
                "image": history_row["image"],
            }

    # Newest first, cap size
    state["history"].sort(key=lambda r: r.get("built_at") or "", reverse=True)
    state["history"] = state["history"][:HISTORY_LIMIT]

    with VERSIONS_FILE.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        f.write("\n")

    README_FILE.write_text(render_readme(state), encoding="utf-8")
    print(f"updated {VERSIONS_FILE} and {README_FILE}")
    print(f"history entries: {len(state['history'])}")


if __name__ == "__main__":
    main()
