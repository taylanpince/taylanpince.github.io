---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
slug: {{ .File.ContentBaseName }}
tags:
- Films
filmDirector: ""
filmRating: 0
filmDateWatched:
filmYearReleased:
filmRuntime:
filmIMDb: ""
cover:
    image: "covers/films/{{ .File.ContentBaseName }}.jpg"
    alt: "Poster for "
    hidden: true
---

<!-- One line: what this film actually is. -->

## What stuck

<!-- 3-5 bullets. The things you'd still bring up a year from now. -->

-
-
-

## Worth your time if

<!-- Short paragraph: who should watch it, what it is. -->
