---
title: "LIDAR v2 Design"
date: 2021-07-21T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
Now that the Rover v2 base is working and driving well, I am turning my attention to the new LIDAR module. After reconsidering the previous GT2 pulley based design, I decided to redesign it completely on the new Rover base, using a gear based approach.

Reasoning behind using a geared drive is fairly simple: Pulley and timing belt approach didn’t necessarily create a smooth drive mechanism like I had imagined. It also takes up a lot of space and it’s a nightmare to calculate for. Finally, printing GT2 pulleys doesn’t generate very clean results on the 3D printer, which in turn contributes to lack of smoothness.

So there are lots of reasons to simplify the design with this version. I kept the bearing the same, but learning from the previous version, made an extrusion that can be detected by the QRD1114, which will be placed conveniently underneath. I also have a nice little lid for the LIDAR. 

![LIDAR Rover Design](/content/project-rover/lidar-v2.gif)

After a few nights of printing and tinkering, I got a successful implementation of the new LIDAR, completely integrated with the Rover!

New design worked really well. Gear based integration with the motor is really smooth, and the sensor placement is perfect. The only issue was having the sensor detect the PLA extrusion. I ended up solving this by gluing a small piece of white printer paper with a thin black line printed on it. QRD1114 detects the switch from white to black on the paper, and nothing else. 

![LIDAR Rover Design](/content/project-rover/lidar-v2.jpg)
<img src="https://www.makerdad.io/uploads/2021/b42a8a46e0.jpg" width="500" style="border-radius: 5px; max-width: 100%; height: auto;" alt="" />

Bigger issue was the motor. 6V encoder motors I got from Banggood didn’t have enough torque to drive the gears. I could get them to work at max PWM, but then it could only capture 24 scans per revolution. That’s not enough resolution for mapping. 

Thankfully I had another set of encoder motors I had bought on sale. These are tiny 6V motors but they come with a gear reducer attached. I thought this might give me enough torque and I was right. Once I printed a custom holder for the small motor and attached it, it could drive the whole mechanism at 40 PWM range. As a bonus, the motor is four times lighter. 

Once I ran this setup, to my delight I got 360 scans per revolution. That’s a one degree resolution per scan and it’s pretty amazing. I can also visualize the laser scan array in Rviz:

![LIDAR RViz](/content/project-rover/lidar-rviz.png)
