---
title: "ZoomBox: Designing with Fusion 360"
date: 2021-03-05T20:34:43+01:00
draft: false
tags:
- Electronics
- ZoomBox
---
Despite my initial aversion to it, Autodesk Fusion 360 is truly an amazing tool. The combination of sketching on faces and timeline editing makes it incredibly powerful. Following the great [Layer by Layer tutorials form Adafruit](https://www.youtube.com/watch?v=VVmOtM60VWw&t=88s) I designed a simple case for the ZoomBox. I was able to import the official DXF files from Arduino right into Fusion 360 and map the screw holes exactly.

![Fusion 360 Design](/content/zoombox/zoombox1.jpg)

Surprisingly, there was no good information available on component heights. I had to manually measure them. For reference, the USB-A port is `12mm by 11mm` and the power jack is `9mm by 11mm`. They are respectively `9mm` and `4mm` inset from the edges of the board. These two drawings were also good references but they didn't provide all the information I needed:

- [Arduino Hole Dimensions Drawing from Adafruit](https://blog.adafruit.com/2011/02/28/arduino-hole-dimensions-drawing/)
- [Arduino Dimension Specs on Arduino Forums](https://forum.arduino.cc/index.php?topic=392447.0)

After adding some simple snap fit joints to the bottom part of the box, I sent it to print and went to bed. To my mild surprise, I found a perfectly fitting box in the morning!

Next step: Design the top part with button inserts.

![Printed Arduino box](/content/zoombox/zoombox2.jpg)
![Printed Arduino box from top](/content/zoombox/zoombox3.jpg)
