---
title: "Improving XBee Delivery Protocol"
date: 2021-07-02T20:34:43+01:00
draft: false
tags:
- Electronics
- Project Rover
---
I spent a bit of time today improving the data delivery protocol I have been using with the XBees. I noticed during various tests that it wasn’t very robust, and it also required the devices to be powered on in a specific order. So I have been meaning to improve this for a while.

Core problem was that the whole setup depended on reading a specific length of bytes with every iteration. If things got out of sync (either due to data corruption, or because the Rover came online before the controller node), then it simply didn’t work and started ignoring messages (since the first control byte could not match).

Solution was obvious: Add a start and end byte to the message, so the payload could always be confirmed. Basically I went with a 12-byte command, including start and stop bytes:

`$ COMMAND INT8 INT8 INT8 INT8 INT8 INT8 INT8 INT8 INT8 #`

This was very easy to setup on the Arduino side. On the Python side, however, I had to jump into iPython and test it out. Some of my assumptions around how things would work with `pyserial` simply didn’t work.

Here is a gist of what I ended up with:

```
INCOMING_MESSAGE_BEGIN = 24
INCOMING_MESSAGE_END = 23

payload = list(self.conn.read_until(expected=bytes([INCOMING_MESSAGE_END]), size=24))

for val in payload:
    if val == INCOMING_MESSAGE_BEGIN:
        message = []
    elif val == INCOMING_MESSAGE_END:
        if len(message) == 10:
            messages.append(message)
    else:
        message.append(val)
```

The big gotcha here was the way `read_until` could match the `expected` value. I initially tried to pass a `byte` value to it, but it simply didn’t work. It couldn’t match the message end bit when I passed it as `b'#'`. However when I converted from its integer representation to a bytes array, it worked as expected.

I also thought I could use the `split` method on `bytes` to split the message on the end bits. I couldn’t get this to work. I am still not fully clear how Python handles the difference between the 8-bit integer representations and character representations of bytes.

In the end, I went with converting it into a list of integers and looping over the list, checking for begin and end codes. This works fast enough for my purposes and is very reliable.

It’s also possible to implement a variable length message using this method, by removing the message length check.

I tested this with the Rover and it’s very reliable. I can now keep it on and kill and restart the script on the controller, or vice versa and it will always connect immediately and start transmitting.