#!/usr/bin/env python3
"""Generate draft book notes in content/books/ from a Goodreads CSV export.

Usage: python3 scripts/import_goodreads.py <export.csv> --year 2026 [--write]
Without --write it only prints what it would create.
"""
import argparse
import csv
import datetime
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "content" / "books"
STOP_PREFIX = re.compile(r"^(the|a|an)\s+", re.I)


def parse_date(s):
    for fmt in ("%Y/%m/%d", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime((s or "").strip(), fmt).date()
        except ValueError:
            continue
    return None


def num(s):
    try:
        return int(float(s))
    except (TypeError, ValueError):
        return 0


def display_title(raw):
    t = re.sub(r"\s*\([^)]*\)\s*$", "", raw).strip()      # drop "(Series, #1)"
    t = re.split(r":\s|,\s+or,?\s+", t, maxsplit=1)[0]     # drop subtitle
    return re.sub(r"\s+", " ", t).strip()


def slugify(title):
    t = STOP_PREFIX.sub("", display_title(title))
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[’']", "", t)
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.csv, encoding="utf-8")))
    books = [
        r for r in rows
        if r["Exclusive Shelf"] == "read"
        and (d := parse_date(r["Date Read"])) and d.year == args.year
    ]
    books.sort(key=lambda r: parse_date(r["Date Read"]), reverse=True)

    for r in books:
        slug = slugify(r["Title"])
        path = BOOKS / f"{slug}.md"
        title = display_title(r["Title"])
        author = re.sub(r"\s+", " ", r["Author"]).strip()
        read = parse_date(r["Date Read"])
        isbn = (r["ISBN13"] or "").strip('="')
        pub = r["Original Publication Year"] or r["Year Published"] or ""
        body = f"""---
title: "{title}"
date: {read.isoformat()}T09:00:00+02:00
draft: true
slug: {slug}
tags:
- Books
bookAuthor: "{author}"
bookRating: {num(r['My Rating'])}
bookDateRead: {read.isoformat()}
bookYearPublished: {num(pub) or ''}
bookPages: {num(r['Number of Pages']) or ''}
bookISBN13: "{isbn}"
bookGoodreads: "https://www.goodreads.com/book/show/{r['Book Id']}"
cover:
    image: "covers/books/{slug}.jpg"
    alt: "Cover of {title}"
    hidden: true
---

<!-- TODO: one line on what this book actually is. -->

## What stuck

-
-
-

## Worth your time if

<!-- TODO -->
"""
        if path.exists():
            print(f"  skip   {slug} (exists)")
            continue
        if args.write:
            path.write_text(body, encoding="utf-8")
            print(f"  create {slug}")
        else:
            print(f"  would create {slug}  <- {r['Title'][:50]}")

    print(f"\n{len(books)} book(s) from {args.year}")


if __name__ == "__main__":
    main()
