---
name: libfreenect
title: libfreenect
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, depth-camera, kinect, library, needs-hardware, usb, visual]
homepage: https://openkinect.org/
scout_score: 8
status: draft
---

# libfreenect

**TLDR;** A userspace driver that turns an original Xbox 360 Kinect into a USB depth camera, with demo viewers and a record-and-replay trick for working without the hardware.

libfreenect is the OpenKinect community's userspace driver for the Microsoft Kinect. It talks to the sensor over libusb and exposes RGB and depth images, motor tilt, accelerometer, LED, and audio. It runs on Linux, macOS, and Windows, with wrappers for C, C++, C#, Python, Ruby, ActionScript, and Java. The README says the wrappers are not guaranteed to be API stable or up to date.

The Homebrew formula installs a set of small demo programs alongside the library. `freenect-glview` shows the camera streams, `freenect-tiltdemo` moves the motor, `freenect-micview` and `freenect-wavrecord` handle the microphone array, and `freenect-regview` looks at depth-to-colour registration. They work as a quick tour of what the device exposes, and as example code.

The interesting part is fakenect. `fakenect-record` saves a live Kinect session into a directory. Later you launch an unmodified program with `LD_PRELOAD` pointing at `libfakenect.so` and `FAKENECT_PATH` pointing at the recording. The program believes a Kinect is attached and gets the recorded frames. That is a neat way to develop and test vision code without the sensor, and it shows how library interposition can stand in for hardware.

This covers only the original Xbox 360 Kinect. The README sends owners of the newer Kinect v2 (Xbox One) to the separate libfreenect2 project.

## Install

```
brew install libfreenect
# Needs an original Xbox 360 Kinect plugged in over USB (the README also mentions `brew install --HEAD libfreenect` for the latest code).
# On Linux, the README says to install the udev rules from platform/linux/udev.
```

## Try this

```
freenect-glview
```
Opens the demo viewer showing the live RGB and depth streams from a connected Kinect.

```
mkdir session && fakenect-record ./session
```
Records a live Kinect session into the session directory for later playback.

```
LD_PRELOAD="/usr/local/lib/fakenect/libfakenect.so" FAKENECT_PATH="./session" freenect-glview
```
Replays the recorded session through the viewer with no Kinect attached.

## What's unique

Fakenect records a real sensor session and replays it into unmodified programs by swapping the driver with LD_PRELOAD. The library also covers the whole device (motor, LED, accelerometer, audio), not only the video.

## Caveats

Needs a first-generation Kinect to do anything live. Audio and some motor and LED features need firmware uploaded to the device, which the README warns may not be legal to redistribute in some jurisdictions. The homepage returned an error when checked, and recent project activity could not be confirmed.

## Links

- [GitHub repository and README](https://github.com/OpenKinect/libfreenect)
- [Homepage (was unreachable, HTTP 525)](https://openkinect.org/)
- [OpenKinect wiki, Getting Started](http://openkinect.org/wiki/Getting_Started)
- [Kinect v2 successor, libfreenect2](https://github.com/OpenKinect/libfreenect2)
