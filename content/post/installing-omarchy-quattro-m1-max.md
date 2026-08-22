---
title: "Installing Omarchy Quattro on a 2021 M1 Max MacBook Pro"
date: 2026-08-22T18:55:00+00:00
draft: false
slug: installing-omarchy-quattro-m1-max
tags:
- Technology
---

I wanted to run Omarchy on an old 2021 MacBook Pro with an M1 Max chip.

The normal Omarchy ISO is not the right path for Apple Silicon. The
setup that worked for me was:

**macOS → Asahi Arch Minimal → Omarchy MX Mac**

This gives you a normal dual boot. macOS stays intact and you can choose
Linux from Apple's startup menu.

This guide is for the 2021 14-inch and 16-inch MacBook Pro with M1 Max.

## Before you start

Back up anything important first.

I gave Linux about **200 GB** on the internal SSD. 100 GB should be
enough for a basic setup.

Do not manually partition the disk with Disk Utility. Let the Asahi
installer handle it.

Keep the Mac connected to power during the install.

## 1. Check the Mac model

Open Terminal in macOS:

``` bash
system_profiler SPHardwareDataType | grep -E "Model Identifier|Chip"
```

The two M1 Max models are:

-   14-inch: `MacBookPro18,4` / `apple,j314c`
-   16-inch: `MacBookPro18,2` / `apple,j316c`

## 2. Install Asahi

From macOS Terminal:

``` bash
curl https://asahi-alarm.org/installer-bootstrap.sh | sh
```

When the installer asks which system to install, choose **Asahi Arch
Minimal**.

Do not choose the desktop version. Omarchy will provide the desktop.

Set the Linux disk size when prompted. I used about 200 GB.

Follow the Apple boot and recovery steps shown by the installer. These
can change, so use the instructions on screen rather than an old guide.

When finished, reboot and choose the new Linux entry from Apple's
startup options.

## 3. Boot into Asahi

The first login is the Asahi root account.

If you are using the standard Asahi Alarm image, use the credentials
shown by the installer. On the setup I used, this was `root`.

Once logged in, connect to Wi-Fi:

``` bash
nmtui
```

Then test it:

``` bash
ping -c 3 archlinux.org
```

## 4. Update the base system

``` bash
pacman -Syu --needed curl gnupg linux-asahi-headers networkmanager iwd
```

Let this finish completely.

## 5. Check the Asahi system

``` bash
uname -m
pacman -Q linux-asahi
tr '\0' '\n' </proc/device-tree/compatible
```

Architecture should be `aarch64`. Your M1 Max device ID should include
`apple,j314c` or `apple,j316c`.

## 6. Install Omarchy Quattro

``` bash
curl -fLO https://raw.githubusercontent.com/maralcbr/omarchy-mx-mac/main/install-omarchy-mx-mac.sh
bash install-omarchy-mx-mac.sh
```

The installer downloads and verifies the current signed Omarchy Mac
release.

It will ask for the username and password for your normal Omarchy
account. This is the account you will use every day.

Let the installer finish. Do not interrupt package installs or builds.

## 7. Reboot

``` bash
reboot
```

Choose the Linux entry from Apple's startup options. You should now land
in Omarchy.

## 8. Check the basics

Test display and brightness, keyboard and backlight, trackpad, Wi-Fi,
Bluetooth, audio, microphone, webcam, battery status, suspend and
resume, and the SD card.

External displays are a separate issue on Apple Silicon. Check your
exact dock and monitor setup before relying on it.

## 9. Check the installed version

``` bash
cat /usr/share/omarchy/version
omarchy-migrate --pending
```

The migration command should normally return nothing after a clean
install.

## 10. Keep it updated

``` bash
omarchy update
```

Stick to the Omarchy update path rather than manually replacing the
Asahi kernel, firmware, or repositories.

## If the install fails

A failed Omarchy install does not mean the Mac is broken. macOS is
separate and can still be booted from Apple's startup options.

Do not reboot immediately. Wait for the installer to return to a shell.

Check that no package process is still running:

``` bash
ps aux | grep -E 'pacman|makepkg|dart|flutter' | grep -v grep
```

Check for a stale Pacman lock:

``` bash
test -e /var/lib/pacman/db.lck && echo LOCK_EXISTS || echo NO_LOCK
```

If no `pacman` or `makepkg` process is running and the lock exists:

``` bash
rm /var/lib/pacman/db.lck
```

Bring the base system back to a clean state:

``` bash
pacman -Syu
```

Then download a fresh installer and try again:

``` bash
rm -f install-omarchy-mx-mac.sh
curl -fLO https://raw.githubusercontent.com/maralcbr/omarchy-mx-mac/main/install-omarchy-mx-mac.sh
bash install-omarchy-mx-mac.sh
```

The installer is designed to be rerun. I recovered from a failed package
build this way without reinstalling Asahi or touching macOS.

## If Linux stops booting

Shut down the Mac. Hold the power button until **Loading startup
options...** appears, then boot macOS.

Do not start deleting partitions. In particular, do not delete the Apple
recovery partition.

## Final setup

``` text
MacBook Pro M1 Max
│
├── macOS
│
└── Asahi Linux
    └── Omarchy Quattro
```

That is the whole setup. No VM, no Docker layer, and no changes to macOS
beyond giving Asahi its own space on the internal SSD.

### References

-   [Asahi Alarm](https://asahi-alarm.org/)
-   [Omarchy MX Mac](https://github.com/maralcbr/omarchy-mx-mac)
-   [Asahi device
    support](https://asahilinux.org/docs/hw/devices/device-list/)