---
title: "Encoding LIDAR Position"
date: 2021-04-18T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
I finally ran into an issue that I have been dreading for a while: Encoding the actual position of the LIDAR pulley mechanism. Now that the LIDAR scan works, I need accurate position data alongside the measurements. As reliable as my ridiculously powerful stepper is, it’s not a servo and doesn’t know which position it starts from.

There are various ways of solving this, with varying levels of budget and difficulty:

- Absolute encoders use code wheels alongside optical or magnetic sensors that have a unique pattern per step. Whatever orientation the wheel is in, the sensors are always able to determine the exact angle.
- Quadratic encoders use two coupled sensors (either magnetic Hall effect sensors or optical ones) to determine wheel direction. They cannot determine absolute position.
- Single optical encoder wheels that rely on a chip such as `LM393` are able to determine incremental movement, but not direction. They also cannot determine absolute position.

Unfortunately, among these options, the only one that could work is the absolute encoder. These are hard to find and as far as I can tell quite expensive. One can probably DIY it, but it wouldn’t be a simple implementation.

As I was thinking through this, it occurred to me that all I care about is the starting position. I had initially thought that the stepper motor wouldn’t be reliable, but some quick testing showed that it’s *very* reliable. Stepper motor is very effective at counting its steps, since that’s literally the main thing it’s good at. So as long as I positioned the starting point properly, I could get accurate positional data.

This is obviously not a novel idea, since all stepper motors work like this. In a 3D printer or CNC machine, the steppers move until they hit the stop switch, which tells the device that it found the starting position. Then it can count its steps from that position and know its exact location.

I really didn’t want to use a physical stop switch, even though I have quite a few lying around from the flip clock project. This got me thinking: Could I use an optical switch instead? I started looking into line tracking robots, since that’s a very similar use case.

Research led me to the [QRD1114 Optical Detector](https://learn.sparkfun.com/tutorials/qrd1114-optical-detector-hookup-guide/all) module. The device is a bit of a weird mashup of a phototransistor coupled with an IR detector. The result is that it’s very good at detecting black and white on non-reflective (i.e. standard printer paper) surfaces.

Device looked familiar, so I looked in my sensors box, and got lucky! I already had one. I got to work prototyping it out and got it working very quickly. The Sparkfun guide above was very helpful.

After some trial and error, I ended up preparing a circular drawing with the exact dimensions of the pulley extension in Illustrator. Then I printed this with the laser printer and cut it out. Sensor could detect it very efficiently.

![LIDAR with makeshift encoder](/content/project-rover/encoder.jpg)

To make the code just as efficient, I used a hardware interrupt whenever the sensor triggers on black:

```
attachInterrupt(digitalPinToInterrupt(2), detectMark, RISING);
```

Every time the LIDAR starts running, I run a calibration cycle, determining where the line is. Then I can start scanning from that position and increment with the stepper. Every time the line is detected, position is reset since that means we completed a full circle scan.

Early testing showed very promising results today. I will attempt to create a [Processing.org](https://processing.org) sketch that can visualize the results tomorrow.

{{< youtube cNZ5pbnqbJM>}}
