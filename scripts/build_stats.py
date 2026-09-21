#!/usr/bin/env python3
"""Regenerate the open-source contribution block in README.md.

Queries the GitHub search API for PRs authored by USER, drops PRs opened
against the user's own repositories, and renders two tables (merged and
in-review) sorted by upstream star count.

Output is deterministic: no timestamps, stable sort. Running it twice in a
row produces no diff, so the nightly workflow only commits real changes.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

USER = "hsdfat"
README = os.path.join(os.path.dirname(__file__), os.pardir, "README.md")
START = "<!-- OSS-STATS:START -->"
END = "<!-- OSS-STATS:END -->"
TITLE_MAX = 72


def api(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-stats",
    })
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_MCP_PAT")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_prs():
    """All PRs authored by USER, across every public repo."""
    items, page = [], 1
    while True:
        url = (
            "https://api.github.com/search/issues"
            f"?q=author:{USER}+type:pr&per_page=100&page={page}"
        )
        data = api(url)
        batch = data.get("items", [])
        items.extend(batch)
        if len(items) >= data.get("total_count", 0) or not batch:
            break
        page += 1
    return items


def repository(repo, cache):
    if repo not in cache:
        try:
            cache[repo] = api(f"https://api.github.com/repos/{repo}")
        except urllib.error.HTTPError:
            cache[repo] = None
    return cache[repo]


def fmt_stars(n):
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def shorten(title):
    title = " ".join(title.split())
    if len(title) > TITLE_MAX:
        return title[: TITLE_MAX - 1].rstrip() + "…"
    return title


def table(rows):
    out = ["| Project | ★ | PR | Contribution |", "|---|---:|---|---|"]
    for r in rows:
        out.append(
            f"| [{r['repo']}](https://github.com/{r['repo']}) "
            f"| {fmt_stars(r['stars'])} "
            f"| [#{r['number']}]({r['url']}) "
            f"| {shorten(r['title'])} |"
        )
    return "\n".join(out)


def build():
    star_cache = {}
    merged, open_ = [], []

    for it in fetch_prs():
        repo = "/".join(it["repository_url"].split("/")[-2:])
        # Own repos are not upstream contributions.
        if repo.split("/")[0].lower() == USER.lower():
            continue
        info = repository(repo, star_cache)
        # A profile README is public. Never expose private repositories when
        # the generator is run with a personal token that can see them.
        if not info or info.get("private"):
            continue
        row = {
            "repo": repo,
            "number": it["number"],
            "title": it["title"],
            "url": it["html_url"],
            "stars": info.get("stargazers_count", 0),
        }
        if it.get("pull_request", {}).get("merged_at"):
            merged.append(row)
        elif it["state"] == "open":
            open_.append(row)

    key = lambda r: (-r["stars"], r["repo"], r["number"])
    merged.sort(key=key)
    open_.sort(key=key)

    upstreams = {r["repo"]: r["stars"] for r in merged}
    projects = len(upstreams)
    total_stars = sum(upstreams.values())

    parts = [
        f"**{len(merged)} merged pull requests** across **{projects} upstream projects** "
        f"totalling **{fmt_stars(total_stars)} stars** · **{len(open_)}** in review",
        "",
        "<details>",
        "<summary>Browse every merged and open upstream pull request</summary>",
        "",
        "### Merged",
        "",
        table(merged),
    ]
    if open_:
        parts += ["", "### In review", "", table(open_)]
    parts += ["", "</details>"]
    return "\n".join(parts)


def main():
    with open(README, encoding="utf-8") as fh:
        readme = fh.read()

    if START not in readme or END not in readme:
        sys.exit(f"markers {START} / {END} not found in README.md")

    block = build()
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n\n{block}\n\n{END}",
        readme,
        flags=re.DOTALL,
    )

    if new == readme:
        print("no change")
        return
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)
    print("README.md updated")


if __name__ == "__main__":
    main()
