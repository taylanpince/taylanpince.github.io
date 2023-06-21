---
title: "Project Rover: Intro"
date: 2021-04-05T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
I have been researching various ways to build a radar for robotic projects. I already have a [Garmin LIDAR Lite](https://buy.garmin.com/en-CA/CA/p/557294) I had bought years ago, so LIDAR seems to be the best way to go. However, my research shows that there are several additional parts that are also required:

- A slip ring, to keep the rotating LIDAR module in connection with the rest of the robot
- Some kind of pulley mechanism to rotate the unit
- A stepper motor or a brushed motor for rotation
- In the case of a brushed motor, an encoder would be needed to calculate exact position
- Wide metal bearing of some sort
- A timing belt or similar for pulley

I found several projects that show some level of success with this method:

- [LIDAR with ROS support for mapping](http://grauonline.de/wordpress/?page_id=1233)
- [3D Scanning like a Pro with LIDAR](https://www.kurokesu.com/main/2017/05/08/3d-scanning-like-a-pro/)

I couldn't get my head around how to design the pulley mechanism until I saw this project: [DIY Arduino LIDAR](http://electronoobs.com/eng_arduino_tut110.php). Basically, the slip ring attaches to the base plate and the rotating part is left to turn on its own. Aluminum bearing does the bulk of the work, since it's inserted between the large pulley wheel, and an extrusion from the base plate.

The Garmin LIDAR Lite can scan at a maximum rate of 500 scans _per second_! Even if I assumed half that speed, that would be amazing. Unfortunately, I will be limited by the mechanical aspects of the components. The slip ring is rated at 300 RPM. It could go higher, but would start introducing significant noise into the signal. Using a brushed motor with an encoder doesn't make sense in this scenario, since I wouldn't require the higher RPM provided by it.

It seems like using one of the NEMA-14 steppers I already have is the best way to go. I have smaller stepper motors from the flipclock project, but they only seem capable of 20-25 RPM at most. NEMA-14 is rated at 600 RPM, with 200 steps per revolution. So here is the plan:

1. Get NEMA-14 stepper working reliably, with continuous speed at 300 RPM and reporting its exact position
2. Design and print a pulley mechanism connected to the stepper, with the LIDAR attached to the large part
3. Have LIDAR scanning with every step and returning distance data, couple stepper position with distance data
4. Implement a simple visualizer to show the results

This should get me a simple, 2D live map of the environment. Once I have this, I can start getting into using [SLAM algorithms](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping) using the [ROS platform](https://www.ros.org).

![LIDAR module](/content/project-rover/lidar.jpg)