---
title: "Driving Straight with Rover"
date: 2021-05-05T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
I made some OK progress on the driving unit last night. I finally got the T connector for the LiPo battery, so I could hook everything up and power both the Arduino and the motors from a portable source. 

I was worried about powering them together but it turned out to be simple. I soldered a buck converter (voltage down) between the battery line and the motor shield. Set it up to give out a constant 4.5V, which should be more than enough for the 3V motors I have in there. 

Arduino specs say that the power jack can safely handle 7-12V input. This is perfect since the LiPo I’m using is 2S (7.4V). I hooked up the LiPo straight into the Arduino power jack and then split a line out to the buck converter. This also prevents any power backlash from the motor shield. I now have a mobile rover!

Things didn’t go so well on the ground though! Robot immediately swerved left and hit the wall. I suspected this might happen, since the encoders were showing that the right side was clocking half the turns of the left side. After looking (and listening) to the wheels and gears, I think the gear box on the right one is busted. 

I ordered some replacement gear boxes and will open up the one I have to see if I can fix it tomorrow. 

In the meantime I also hooked up an Xbee S1 module to the unit. Plan is to be able to remotely control it from the computer. Configuring the Xbees was easier than I remembered. X-CTU app is a dumpster fire but once you know how to do a few basic things configuration is fairly easy. 

Plan for tomorrow: Implement a simple serial protocol to control the driver unit. I’m imagining a couple of commands for starters: Direction + Distance and Rotation + Angle (ie. `F100`, `B50`, `R90`). 

![Rover](/content/project-rover/driving.jpg)
