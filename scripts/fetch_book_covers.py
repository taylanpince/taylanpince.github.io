#!/usr/bin/env python3
"""Download cover art for every book note in content/books/ that lacks one.

Tries Open Library (by ISBN13, then ISBN10), then Google Books. Writes to
assets/covers/books/<slug>.jpg so Hugo's image pipeline can resize it.

Usage:  python3 scripts/fetch_book_covers.py [--force]
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "content" / "books"
COVERS = ROOT / "assets" / "covers" / "books"
UA = {"User-Agent": "kaizenmusings-cover-fetch/1.0 (+https://kaizenmusings.com)"}


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^(\w+):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip('"')
    return out


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
            return r.read() if r.status == 200 else None
    except Exception:
        return None


def openlibrary(isbn):
    # default=false makes it 404 instead of returning a 1x1 tracking GIF
    data = get(f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg?default=false")
    return data if data and len(data) > 3000 else None


def openlibrary_search(title, author):
    """No ISBN: resolve title+author to a cover_i via the search API."""
    q = urllib.parse.urlencode({"title": title, "author": author,
                                "limit": 3, "fields": "cover_i,title,author_name"})
    raw = get(f"https://openlibrary.org/search.json?{q}")
    if not raw:
        return None
    try:
        docs = json.loads(raw).get("docs") or []
    except json.JSONDecodeError:
        return None
    for doc in docs:
        if doc.get("cover_i"):
            data = get(f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-L.jpg?default=false")
            if data and len(data) > 3000:
                return data
    return None


def googlebooks(query):
    raw = get("https://www.googleapis.com/books/v1/volumes?q=" +
              urllib.parse.quote(query))
    if not raw:
        return None
    try:
        items = json.loads(raw).get("items") or []
    except json.JSONDecodeError:
        return None
    for item in items:
        links = item.get("volumeInfo", {}).get("imageLinks", {})
        for key in ("extraLarge", "large", "medium", "thumbnail", "smallThumbnail"):
            if key in links:
                url = links[key].replace("http://", "https://")
                url = re.sub(r"&zoom=\d+", "&zoom=1", url)
                data = get(url)
                if data and len(data) > 3000:
                    return data
    return None


def jpeg_size(data):
    """Width/height straight out of the JPEG SOF marker; no Pillow dependency."""
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h = int.from_bytes(data[i + 5:i + 7], "big")
            w = int.from_bytes(data[i + 7:i + 9], "big")
            return w, h
        i += 2 + int.from_bytes(data[i + 2:i + 4], "big")
    return 0, 0


def main():
    force = "--force" in sys.argv
    COVERS.mkdir(parents=True, exist_ok=True)
    missing = []
    for md in sorted(BOOKS.glob("*.md")):
        if md.name == "_index.md":
            continue
        fm = front_matter(md)
        slug = fm.get("slug") or md.stem
        dest = COVERS / f"{slug}.jpg"
        if dest.exists() and not force:
            continue
        title = fm.get("title", "")
        author = fm.get("bookAuthor", "")
        data = None
        for isbn in [i for i in (fm.get("bookISBN13"), fm.get("bookISBN")) if i]:
            data = openlibrary(isbn) or googlebooks(f"isbn:{isbn}")
            if data:
                break
        if not data and title:
            data = (openlibrary_search(title, author)
                    or googlebooks(f'intitle:"{title}" inauthor:"{author}"'))
        if data:
            dest.write_bytes(data)
            w, h = jpeg_size(data)
            flag = "  <- LOW RES, replace manually" if w and w < 300 else ""
            print(f"  ok    {slug}  ({len(data) // 1024} KB, {w}x{h}){flag}")
        else:
            missing.append((slug, fm.get("title", ""), fm.get("bookAuthor", "")))
            print(f"  MISS  {slug}")
    if missing:
        print(f"\n{len(missing)} cover(s) need a manual drop into assets/covers/books/:")
        for slug, title, author in missing:
            q = urllib.parse.quote(f"{title} {author} book cover")
            print(f"  {slug}.jpg   https://www.google.com/search?tbm=isch&q={q}")


if __name__ == "__main__":
    main()
