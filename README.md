# kaizenmusings.com

Source for [Kaizen Musings](https://kaizenmusings.com), the personal site of
Taylan Pince. Built with [Hugo](https://gohugo.io/) and the
[PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, deployed to
GitHub Pages.

## Running locally

The theme is a git submodule, so clone with it or initialise it afterwards:

```bash
git submodule update --init --recursive
```

Hugo must be the **extended** build (the theme compiles SCSS). On Arch:

```bash
omarchy pkg add hugo
```

Then:

```bash
hugo server                 # published content only
hugo server --buildDrafts   # include drafts
```

To check what will actually deploy, build the way CI does rather than trusting
the dev server:

```bash
hugo --gc --minify --destination /tmp/site-check
```

## Layout

```
content/post/     Long-form posts, grouped into subfolders by topic
content/books/    Short book notes (see below)
layouts/books/    List and single templates for the books section
layouts/partials/ book_cover, book_entry, book_rating
assets/covers/    Cover images, referenced by path from front matter
assets/css/extended/  Site CSS on top of the theme
scripts/          Goodreads import and cover fetching
```

## Books

Book notes live in `content/books/` and use `book*` front matter fields:

```yaml
bookAuthor: "Benjamín Labatut"
bookRating: 5            # 1-5, drives the star display
bookDateRead: 2026-03-15 # shown as "Read"; also groups the list page by year
bookYearPublished: 2020
bookPages: 193
bookISBN13: "9780771010422"
bookGoodreads: "https://www.goodreads.com/book/show/62069739"
```

Two helper scripts:

```bash
# Create draft notes for a year from a Goodreads CSV export
python3 scripts/import_goodreads.py ~/Downloads/goodreads_library_export.csv --year 2026 --write

# Fetch any missing cover art from Open Library / Google Books
python3 scripts/fetch_book_covers.py
```

Export the CSV from [goodreads.com/review/import](https://www.goodreads.com/review/import)
(desktop browser only). The Goodreads API has been dead since 2020.

## Deployment

Pushing to `main` triggers `.github/workflows/hugo.yaml`, which builds with Hugo
and publishes to GitHub Pages. Drafts are never included: the workflow runs
`hugo` without `--buildDrafts`.

Note the workflow pins **Hugo 0.153.2** while a current Arch install is 0.165.x.
The site builds on both, but 0.158 deprecated the `languageCode` config key in
favour of `locale`; that change can only land once the workflow is bumped.
