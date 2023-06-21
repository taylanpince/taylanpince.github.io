---
title: "Hosting a Personal Site – 2023 Edition"
date: 2023-01-04T13:15:43+01:00
draft: false
slug: hosting-personal-site-2023
tags:
- Software
---

I have been on the hunt for the easiest way to host a personal site and blog for a long time. Over the years, I: 
- developed several versions of my own CMS
- used various static hosting solutions like Jekyll
- built a simple static templating solution with Flask
- used Medium
- used a headless setup with AWS and Zappa
- tried [Micro Blog](https://micro.blog/)
- even gave WordPress a try.

There were pros and cons with each solution, but nothing really felt easy to setup and update. With this site, I feel like I finally settled on a configuration that is easy to maintain and update, with very low-cost hosting:
- Github Pages for hosting
- Github Actions for deployment
- [Hugo](https://gohugo.io/) as lightweight, configurable static CMS
- [PaperMod](https://github.com/adityatelange/hugo-PaperMod/tree/exampleSite) as the Hugo skin
- [CloudFlare](https://www.cloudflare.com/) for DNS and redirect management

Writing new posts is easy, because I can just type them up in Ulysses as Markdown, then paste them into a Hugo template. Hugo has built-in image resizing support and PaperMod makes everything looks nice.

I made some minor customizations, and those were easy too. I mostly followed the official Hugo documentation and PaperMod samples. The whole site is available as an open source repo.

One big gotcha for me was using CloudFlare for redirecting older domains to my new one. CloudFlare has a delightful redirect system built-in, with lots of options to configure custom redirects.

Finally I can focus on writing and publishing, what a delight! 🤓