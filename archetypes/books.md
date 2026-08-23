---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
slug: {{ .File.ContentBaseName }}
tags:
- Books
bookAuthor: ""
bookRating: 0
bookDateRead:
bookYearPublished:
bookPages:
bookISBN13: ""
bookGoodreads: ""
cover:
    image: "covers/books/{{ .File.ContentBaseName }}.jpg"
    alt: "Cover of "
    hidden: true
---

<!-- One line: what this book actually is. -->

## What stuck

<!-- 3-5 bullets. The ideas you'd still repeat a year from now. -->

-
-
-

## Worth your time if

<!-- Short paragraph: who should read it, what it changed. -->
