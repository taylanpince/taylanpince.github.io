# Working in this repo

Notes for AI agents. Read this before writing prose or touching the build.

## Verify with a clean build, not the dev server

`hugo server` has repeatedly served **truncated or stale content** here while the
files on disk were correct, and once returned HTTP 500 on every page after a
single bad rebuild. `--disableFastRender` reduces but does not eliminate it.

Never confirm output by reading from the dev server. Build to a temp directory
and inspect that:

```bash
hugo --gc --minify --buildDrafts --destination /tmp/site-check
```

Two known causes, both avoidable:

- **Non-atomic writes.** `open(path, 'w')` truncates before writing, and Hugo's
  watcher can read the file mid-write and cache the fragment. Write to a temp
  file and `os.replace()` it over the target.
- **`sed -i`** leaves temp files like `sedXk3l9a` beside the target. Hugo treats
  one dropped in `content/` as a content file and the rebuild breaks. Use Python
  with an atomic replace instead.

Anything under `content/`, `assets/`, `layouts/` or `archetypes/` is watched,
including partially-downloaded files (`.crdownload`).

## Voice

Posts are written in Taylan's voice. He has corrected drafts on all of the
following, so treat them as rules rather than preferences.

**Use contractions.** "I don't", "it's", "doesn't". Not "I do not".

**No em-dashes or en-dashes in prose.** Use commas, or split the sentence.
Dashes inside a quotation stay as the author wrote them.

**No punchy fragment triads.** Constructions like "It is not X. It is Y." or
"They are not two books. They are one argument." read as LinkedIn thought
leadership and get rejected. Nothing in his existing writing does this.

**No empty sentences.** "I don't think this tension has gone anywhere. It has
just moved." was cut with the note: either give it a clear explanation or don't
write sentences like these. Every claim should land somewhere concrete.

**Be plain, narrative and hedged.** His posts move chronologically, admit
confusion openly ("apparently I had no idea how the Arduino UNO boards actually
worked"), and hedge constantly with "I think", "as far as I know", "arguably".
Enthusiasm is stated simply: "like catnip", "This is genius".

**Headers should be plain and concrete.** "Labatut vs. Biographers", "Podcast vs.
book", "Highlights from the book". He rejected "The parts that stuck" and "Why
this beats a biography" as styles he hates. Short notes of three or four
paragraphs use no headers at all.

Read `content/post/satisfactory.md`, `content/post/zoombox/intro.md` and
`content/post/about.md` for the register before drafting anything.

## Never invent his opinions

The Goodreads export contains **no reviews and no private notes** for any of 221
read books, only ratings and dates. Kindle highlights show what a book said, not
what he thought of it.

When there is no source for an opinion, ask him. Do not write a plausible-sounding
take and do not build a bridge between a book and his work that he has not made.
Draft skeletons with explicit `TODO(taylan)` markers where his judgment belongs.

## Quotes

Book notes quote copyrighted text, so:

- Use markdown block quotes, with **no attribution line under each quote**.
- Put one footnote at the bottom: `All quotes are from *Title* by Author.`
- Do not reproduce every highlight verbatim. Engage with all of them, quote the
  ones that carry weight.
- **A close paraphrase of a verbatim quote is worse than either option.** If the
  source text is his own note, paraphrase freely. If it is the book's wording,
  either quote it properly or restate it genuinely differently. Ask which it is
  when it is not obvious.

## Books section

Front matter uses flat `book*` fields. **Do not use `author`** — PaperMod already
uses that param for the post byline, hence `bookAuthor`.

`mainSections` in `hugo.yaml` is set explicitly to `[post, books]`. Hugo defaults
it to the single largest section, so removing this silently drops book notes from
Archives and the site RSS.

Slugs drop a leading article, which reads well for "The Anthropocene Reviewed"
but badly for "The Loser". Check the result; `the-loser` was fixed by hand.

`layouts/partials/book_cover.html` falls back to a titled placeholder when the
cover file is missing, and never emits a 2x srcset it would have to upscale to.

## Goodreads and Kindle data

**`Date Read` is empty for 127 of 221 read books.** `import_goodreads.py` filters
on it, so those are silently skipped. Taylan says the undated ones are mostly old
reads logged in bulk, but Brooklyn was a current-year read that nearly went
missing this way.

**The Kindle account is shared with his daughter.** Last-accessed dates from
read.amazon.com/notebook are authoritative for a book, but some annotated books
are hers, not his. Never use Kindle dates as a blanket fallback for a missing
`Date Read`.

**Open Library returns a 1x1 tracking GIF, not a 404**, when it has no cover for
an ISBN. Always pass `?default=false`. `fetch_book_covers.py` handles this and
prefers the widest result across sources; anything under 300px is flagged for
manual replacement.

read.amazon.com/notebook needs an interactive login. Ask him to sign in; never
enter credentials.

## Deployment

CI builds without `--buildDrafts`, so `draft: true` files never reach the public
site. They are still visible in the public GitHub repo. Do not flip a draft to
published without being asked.
