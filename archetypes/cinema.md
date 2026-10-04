---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
slug: {{ .File.ContentBaseName }}
tags:
- Cinema
movieDirector: ""
movieRating: 0
movieDateWatched:
movieYearReleased:
movieRuntime:
movieIMDb: ""
cover:
    image: "covers/cinema/{{ .File.ContentBaseName }}.jpg"
    alt: "Poster for "
    hidden: true
---

<!-- One line: what this movie actually is. -->

## What stuck

<!-- 3-5 bullets. The things you'd still bring up a year from now. -->

-
-
-

## Worth your time if

<!-- Short paragraph: who should watch it, what it is. -->
