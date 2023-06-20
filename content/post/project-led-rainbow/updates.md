---
title: "Project LED Rainbow: Bluetooth Support"
date: 2021-02-12T20:34:43+01:00
draft: false
tags:
- Electronics
- Project LED Rainbow
---
Added some logic to the LED rainbow so it dims slowly over the course of the hour before turning off for the night, and same in the morning. With that, I call this project complete!
 

![LED Rainbow dimming](/content/project-led-rainbow/dimming.jpg)

* * *

Decided to add Bluetooth control to the LED Rainbow. Every once in a while we need to change the go to sleep and wake up times and M wants to be able to control the colours from her iPad. 

Got my old RedBearLab BLE units out. Unfortunately RedBearLab seems to have gone out of business in the last few years. But the units are still working well and thankfully their [GitHub repos](https://github.com/RedBearLab) are still up. 

Spent a few hours converting and old BLE library into a working Swift implementation. Next step will be writing a simple protocol to control time and colour settings on the rainbow.

![LED Rainbow Bluetooth](/content/project-led-rainbow/bluetooth.jpg)

* * *

Made surprisingly good progress on the Bluetooth implementation tonight. Built a simple iOS app that can connect to the Arduino and read existing device settings. I’m pretty happy with the [clean Swift implementation](https://github.com/taylanpince/led-rainbow/blob/bluetooth-support/ios/LEDRainbow/ViewController.swift) and the object oriented [Arduino controller](https://github.com/taylanpince/led-rainbow/blob/bluetooth-support/rainbow/BLEController.h). 

Protocol design ended up being very simple: A command byte, then three optional argument bytes. It’s enough to cover all cases. Same commands can be used for both reading and writing, which is nice. 

This also ended up being a nice little recap for me on Swift 5 data types and advanced use of enums. Porting the same code over to Arduino was much easier than I anticipated. 

Next step: Writing configuration changes to the device!

![Flipclock assembled](/content/project-led-rainbow/bluetooth2.jpg)

* * *

Wrapped up the weekend with a successful test of the Bluetooth controls on LED Rainbow. M changed the colours to her choices (mostly purple). Apparently she is going to draw an app icon for it 😀

![Flipclock assembled](/content/project-led-rainbow/final1.jpg)

![Flipclock assembled](/content/project-led-rainbow/final2.jpg)