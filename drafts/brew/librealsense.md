---
name: librealsense
title: librealsense
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, depth-camera, library, needs-hardware, robotics, visual]
homepage: https://github.com/realsenseai/librealsense
scout_score: 5
status: draft
---

# librealsense

**TLDR;** The open-source SDK for Intel RealSense depth cameras, with a viewer and dozens of small example tools that turn a camera into distances in meters.

librealsense is the RealSense SDK 2.0, a cross-platform C/C++ library for talking to Intel RealSense stereo depth cameras. It streams depth and color frames and provides intrinsic and extrinsic calibration information, which is the data you need to turn a pixel into a point in space. The README calls RealSense the "defacto-standard 3D stereo camera for robotics."

The Homebrew package installs the library along with a large set of command-line tools. The best known is `realsense-viewer`, a GUI for looking at the streams. There is also a depth-quality tool, and many `rs-*` programs that look like the SDK's examples: capture, align, point cloud, record and playback, measure, firmware update and more. The README describes only the viewer and the depth-quality tool, so the rest are best discovered by running them.

The idea underneath is the high-level pipeline API. In C++ (`rs2::pipeline`) or Python (`rs.pipeline`), you start the pipeline, call `wait_for_frames()` in a loop, pull the depth frame, and call `get_distance(x, y)` on a pixel to get meters. That is about a dozen lines to a working depth sensor, and it opens onto stereo vision, point clouds, alignment of depth to color, and robotics. Wrappers exist for Python, ROS 2, C#, Unity and a REST API.

## Install

```
brew install librealsense
# Needs a RealSense camera plugged in. Python bindings are separate: pip install pyrealsense2 (or pyrealsense2-beta, not both).
```

## Try this

```
realsense-viewer
```
Opens the GUI viewer, where you can enable depth and color streams from a connected camera.

```
rs-enumerate-devices
```
Lists the RealSense devices the SDK can see (listed among the installed executables; the brief does not describe its output).

```
rs-hello-realsense --help
```
Shows the options for the smallest example program, the sort of first step the pipeline API is built around.

## What's unique

One repository bundles the SDK, a viewer, a depth-quality measurement tool, and wrappers for many languages. The pipeline API keeps a first working program to about a dozen lines.

## Caveats

It is only useful with a RealSense camera attached, feature support varies by platform, and the project recently moved to the realsenseai GitHub org, so the old links may stop redirecting.

## Links

- [GitHub repository (homepage)](https://github.com/realsenseai/librealsense)
- [Releases (precompiled SDK bundles)](https://github.com/realsenseai/librealsense/releases)
- [Wiki and docs](https://github.com/realsenseai/librealsense/wiki)
