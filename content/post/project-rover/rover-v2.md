---
title: "Designing Rover v2"
date: 2021-06-22T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
I made some solid progress on the v2 design of the rover during last week and finally assembled an initial test version last night. The difference is incredible. Even with no PID implementation, it drives in an almost perfect straight line. I believe the added weight of the motors and bearings help, but the real star are the new encoded motors.

I found a couple of cheap 12V brushed motors with magnetic encoders on Amazon and designed a custom chassis around them in Fusion 360. Now that I understand the concepts behind Fusion better, I was able to make very quick progress on the design. I kept it as large as possible, within the limitations of the printer bed.

![Rover Wheels](/content/project-rover/rover-wheels.png)

I had a few leftover 42mm bearings from the LIDAR, so I decided to use them for the front wheels. I believe this was a good decision, since it contributes to the base weight considerably, making the vehicle more stable. It also ensures smooth motion on front wheels.

I designed the base level with mounting holes for an Arduino Mega, two L298N motor drivers, and a LiPo holder. There are also mounting holes for a second level, which I am planning to mount the LIDAR on.

![Rover Chassis](/content/project-rover/rover-chassis.jpg)

Printing went fairly smooth, though I had a small adhesion issue on the large base level. One of the corners lifted during the 9 hour print and warped considerably. On a whim, I decided to use the heat gun on it to try and flatten the piece. To my surprise, it worked quite well. I heated up the corner for 15 seconds, then pressed on it with a heavy wooden box. It’s not perfectly flat but it’s workable.

After assembling the whole unit, I took it for a test ride and I was very pleased with the results. Before doing any automated driving, I decided to hook up the XBee module and implement a simple remote control for the rover. I think it’s a good idea to make sure it runs smoothly with manual controls before trying to automate driving. That way I can be sure that there are no mechanical issues before focusing on software.

![Rover v2 Base](/content/project-rover/rover-base.jpg)