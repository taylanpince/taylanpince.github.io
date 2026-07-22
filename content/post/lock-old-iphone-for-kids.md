---
title: "How to Lock an Old iPhone Down to Just a Few Apps for Your Kid"
date: 2026-07-22T17:04:20+00:00
draft: false
slug: lock-old-iphone-for-kids
tags:
- Software
---

I set up an old iPhone for my daughter. I wanted it to show only a few apps and nothing else. No App Store. No web browser. No way to wander off into the rest of the phone.

Newer iPhones have a built-in setting for this, called Assistive Access. It needs a recent version of iOS. My old iPhone only went up to iOS 16, so I couldn't use it. If your phone is a few years old, you are probably in the same spot.

Here is the method that worked instead. It takes about 20 minutes. You do not need to be technical to follow it. Just go slowly and do the steps in order.

## What you need

- A Mac computer.
- The iPhone you want to set up.
- A cable to connect the iPhone to the Mac.
- A free Apple app called Apple Configurator.

If you don't have a Mac, this exact method won't work. There are other tools that do the same job from a Windows PC, but this guide is for the Mac.

## Read this first

This process erases the iPhone. Everything on it gets deleted.

So do this before you put any of your child's apps, photos, or accounts on the phone. Set up the lock first, then hand the phone over.

## Step 1: Install Apple Configurator

On the Mac, open the App Store. Search for "Apple Configurator." Install it. It is free.

## Step 2: Connect the phone

Plug the iPhone into the Mac with the cable.

A message appears on the iPhone asking if you trust this computer. Tap Trust. Type the phone's passcode if it asks.

## Step 3: Start the setup

Open Apple Configurator. The phone shows up on the screen. Click it once, then click the Prepare button at the top.

## Step 4: Work through the options

A window opens with setup choices. Go through them like this:

1. Choose Manual Configuration. Click Next.
2. Tick the box that says "Supervise devices." Also tick "Allow devices to pair with other computers." Leave everything else unticked. Click Next.
3. On the next screen, choose "Do not enroll in MDM." Click Next.
4. If it asks you to sign in to Apple Business Manager or Apple School Manager, skip it. You do not need an account. This is the step that confuses most people. You can ignore it.
5. Create an organization. This is just a name that will show on the phone. I used "Home." Type a name and click Next.
6. Choose "Generate a new supervision identity." Click Next.
7. It asks which setup screens to show. The defaults are fine. Click Prepare.

The phone now erases itself and sets back up. This takes a few minutes. Do not unplug it.

When people talk about a "supervised" phone, all it means is that your Mac is allowed to manage it. That is what lets you lock it down.

## Step 5: Build the lock

Now you tell the phone which apps to show.

In Apple Configurator, click File at the top, then New Profile. An editor opens. Think of a profile as a short list of rules for the phone.

Add these rules:

1. In the list on the left, find Restrictions and click Configure. Look for the apps section. Set it to allow only the apps you want to keep, for example Phone, Messages, and Maps. Every other app disappears from the phone. This is the fiddliest step, so take your time.
2. Find Web Content Filter and click Configure. Set it to "Specific Websites Only" and leave the list empty. This blocks the web browser, and it also blocks web pages that try to open inside other apps. Skip this step if you actually want the web available.
3. If you want to choose where the icons sit on the screen, find Home Screen Layout and set it up. This part is optional.

When you are done, click File, then Save. Save the file somewhere easy to find, like the Desktop.

## Step 6: Put the lock on the phone

The phone should still be connected to the Mac.

In Apple Configurator, click the phone, click Add, then Profiles. Pick the file you just saved. It installs onto the phone.

That's it. The phone now shows only the apps you chose.

## Optional: limit who your child can message and call

You can also limit the phone to a short list of contacts. This uses a separate Apple feature called Screen Time.

1. First, put your allowed contacts in iCloud. On the phone, go to Settings, tap your name, tap iCloud, and turn on Contacts. Then add the people you want. This step matters. The limit does not work with contacts saved only on the phone.
2. Go to Settings, then Screen Time, and turn it on.
3. Tap Communication Limits, then During Screen Time. Choose "Contacts Only."
4. Turn off "Allow Contact Editing" so your child can't add new people.
5. Set a Screen Time passcode that only you know, so none of this can be changed.

Now your child can only call and message the people you added. Emergency calls still work no matter what.

## Changing things later

If you want to add or remove an app later, plug the phone back into the Mac, open the profile in Apple Configurator, make the change, and put it back on the same way.

I hope this helps. It made a real difference for us. My daughter has a phone she can use for the few things she needs, and I don't have to worry about the rest.
