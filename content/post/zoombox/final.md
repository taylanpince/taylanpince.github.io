---
title: "ZoomBox: Completed"
date: 2021-03-10T20:34:43+01:00
draft: false
tags:
- Electronics
- ZoomBox
---
ZoomBox is ready! I designed and printed the top part and fitted the arcade buttons in. I wanted the button icons to be extruded out, which presented a problem. If I extruded them, I couldn't print the top part upside down. Eventually I decided to print without them and then printed them separately in black filament. Then used a white acrylic pencil to contour the icons. I am pretty happy with the result.

Obviously, using an Arduino UNO for this project is overkill. My research eventually led me to the Arduino Pro Micro, which already has an ATMEGA32u4 in it. This means it's ready to be used as an HID and all keyboard and mouse control can be done with it.

I will get my hands on some Pro Micros to play with them, but in the meantime this version of the project is a success.

I published all STL models and the Arduino sketch [on the ZoomBox Github repo](https://github.com/taylanpince/ZoomBox).

![ZoomBox](/content/zoombox/final.jpg)
