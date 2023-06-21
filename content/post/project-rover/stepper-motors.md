---
title: "Driving LIDAR with Stepper Motors"
date: 2021-04-10T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
I got the stepper motor working tonight. This was significantly harder than I expected. I had several motor driver boards lying around, and thought I would make my job easier and use an [Arduino Motor Shield](https://store.arduino.cc/usa/arduino-motor-shield-rev3). As it turns out, running steppers with it is not that straightforward. I tried several libraries, everything from the standard [Stepper](https://www.arduino.cc/en/reference/stepper) library to the [AccelStepper](https://www.airspayce.com/mikem/arduino/AccelStepper/index.html), which is supposed to be state of the art.

There are a few things that threw me off, in no particular order:

The NEMA-14 I am using is a 4-cable bipolar motor. I tried to initialize the libraries with pins for all 4 coil cables, and this doesn't work. Apparently what you are supposed to do is to use the 2-cable setup, but then set the PWM pins to `HIGH` in setup:

```
Stepper stepper(stepsPerRevolution, DIR_A, DIR_B);

void setup() {
  pinMode(PWM_A, OUTPUT);
  pinMode(PWM_B, OUTPUT);
  pinMode(BRAKE_A, OUTPUT);
  pinMode(BRAKE_B, OUTPUT);

  digitalWrite(PWM_A, HIGH);
  digitalWrite(PWM_B, HIGH);
  digitalWrite(BRAKE_A, LOW);
  digitalWrite(BRAKE_B, LOW);

  stepper.setSpeed(400);
}
```

Same idea applies to `AccelStepper`. Brake pins are needed only because of the Arduino Motor Shield's setup.

I eventually got the motor to run with the `AccelStepper` library, but it was very unreliable. Even though I wanted it to run at a constant speed, motor would continuously accelerate or decelerate, and eventually would stall. In addition, I noticed that trying to use Serial during operation was a big problem with `AccelStepper`. It would change the way the motor was running.

I also ran some tests on the [Adafruit Motor Shield rev1](https://learn.adafruit.com/adafruit-motor-shield/overview) I had from many years ago. Again, I could get the motor to run, but it was unreliable. In addition the board started smelling funny and I noticed that the `L293D` H-bridge driver getting very hot.

Finally, I decided to get back to basics. I hooked the Arduino Motor Shield up, loaded up the `Stepper` library again and wrote the simplest stepper program:

```
void setup() {
    stepper.setSpeed(400);
}

void loop() {
  stepper.step(1);
}
```

After fiddling with the speed a bit, this actually worked! I elaborated on it a bit more to confirm the RPM:

```
void loop() {
  stepper.step(1);
  currentStep += 1;

  if (millis() - lastCheckTime >= 60000) {
    Serial.print("RPM: ");
    Serial.println(currentStep / stepsPerRevolution);

    currentStep = 0;
    lastCheckTime = millis();
  }
}
```

And sure enough, I got an RPM reading of 398. It's good enough for the LIDAR, and I can safely print things out to the Serial.

Next step will be designing the pulley system. I got the 42mm bearing and the timing belt today. It's going to be fun to hook up the whole mechanism.

![Stepper motors](/content/project-rover/steppers.jpg)