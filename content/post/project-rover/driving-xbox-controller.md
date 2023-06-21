---
title: "Driving Rover with an Xbox Controller"
date: 2021-07-09T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
Before jumping to the PID implementation and eventually autonomous driving, I wanted to make sure that the Rover v2 could drive and turn with stability. I could have done a simple keyboard implementation but I really wanted to integrate an old Xbox controller I had lying around. 

What I have seems to be an Xbox One controller and it connected to my Mac over Bluetooth with no issues. After some research, I found out that pygame is actually the best way to work with these game pads. 

I had never used pygame before but it felt very natural. It has a great abstraction layer for the various controls on the gamepad so I could easily extract axis data from joysticks relatively easily:

```
import pygame

pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

while True:
    left_power = controller.get_axis(1)
    right_power = controller.get_axis(3)
    left_speed = int(abs(left_power) * MAX_POWER)
    right_speed = int(abs(right_power) * MAX_POWER)
```

I then coupled this with the previous XBee implementation I had done and hooked it up with `pyserial`. To Python, XBee looks like just another USB port and thanks to the magic XBees all the remote control part is taken care of.

After some tinkering, I had a sweet little Python script that got the control values from the Xbox controller and passed them on to the Arduino on the rover. Here it is in action:

{{< youtube v7xwdQopwBI >}}

Overall I’m very happy with this. I think the crappy tires are causing issues with traction though. I will have to swap them out or print new ones using the new direct drive extruder I got. 

Next step: PID implementation, two way data transfer, and eventually ROS integration for control. I also need to redesign the LIDAR piece to fit on the rover. Instead of pulleys, I’m planning to do a gear based implementation. 

![XBox](/content/project-rover/xbox.jpg)
