---
title: "Project LED Rainbow: Prototype"
date: 2021-02-03T20:34:43+01:00
draft: false
tags:
- Electronics
- Project LED Rainbow
cover:
    image: "covers/project-led-rainbow/prototype.jpg"
---
I have been working on an LED rainbow project for M. It's really coming along and I also managed to get an RTC module soldered on to the board tonight. Everything was going well until the sketch upload to the Trinket failed.

Apparently Adafruit Trinket has this issue where it’s easy to override the bootloader by mistake. I think it happened because I was using 99% of progmem. 

Solution is easy, you just hook up the Trinket to another Arduino and use a little sketch to burn a fresh bootloader. Problem was: Trinket was already soldered on the prototype board!

What followed was two hours of frustrating desoldering and attaching headers. 

Lesson learned: Solder headers for core components instead of soldering them directly on prototype boards. You never know when you have to get them out again.

After much tinkering, I gave up on the Trinket and hooked in an Arduino Nano. The memory limitations of the Trinket were being too annoying, and as I much as I like those tiny units, they are more trouble than they are worth.