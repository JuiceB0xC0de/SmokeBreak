---
name: owfs
title: OWFS
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [1-wire, afternoon, filesystem, needs-hardware, protocol, sensors]
homepage: https://owfs.org/
scout_score: 7
status: draft
---

# OWFS

**TLDR;** A filesystem for the Dallas/Maxim 1-Wire bus, where cheap sensors and switches show up as files you can read and write from the shell.

OWFS puts a 1-Wire bus into a directory tree. Each device on the bus has a unique ID, and its readings and settings appear as files under that ID. A path such as `10.001122334/temperature` reads a value. Because it is just files, ordinary shell tools and scripts can read temperature, flip a switch, write to an LCD, or log and graph the results.

1-Wire is a low-speed bus from Dallas Semiconductor, now Maxim, where devices are individually addressed and can run on parasitic power. The hardware is cheap, and most people never meet it. OWFS is a way in without writing a driver.

The package is a set of programs rather than one tool. `owserver` shares the bus over the network. `owhttpd` serves it as a web page, and `owftpd` serves it over FTP. `owtap` and `owmon` are for watching and inspecting. There are also bindings for perl, python, php, tcl, Java and C. The homepage lists uses like home automation, server rooms, HVAC and weather stations.

The homepage describes the interface but not the internals, so the details are worth reading in the project docs.

## Install

```
brew install owfs
# Real use needs 1-Wire hardware: a bus master such as a USB DS9490R, serial or i2c adapter, plus sensors. The homepage also has a 'Testing without hardware' page.
```

## Try this

```
owserver --help
```
Shows the options for the server that shares a 1-Wire bus over the network.

```
owdir --help
```
Shows how to list the devices on a bus through an owserver.

```
owhttpd --help
```
Shows the options for serving the bus as a web page.

## What's unique

It turns a hardware bus into a plain filesystem, so a shell script can read a sensor the way it reads a text file. It also shares the bus over the network, web and FTP.

## Caveats

Needs 1-Wire hardware to do anything real, and the homepage is labelled a 'Development Site' with no visible release date, so its current maintenance is unclear.

## Links

- [OWFS homepage](https://owfs.org/)
