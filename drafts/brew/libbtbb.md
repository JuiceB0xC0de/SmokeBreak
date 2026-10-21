---
name: libbtbb
title: libbtbb
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bluetooth, library, needs-hardware, protocol, sniffing]
homepage: https://github.com/greatscottgadgets/libbtbb
scout_score: 8
status: draft
---

# libbtbb

**TLDR;** A C library that decodes Bluetooth baseband packets and piconet details from Ubertooth or USRP sniffer captures, opening up the radio layer beneath Bluetooth.

libbtbb is the Bluetooth baseband decoding library, forked from the GR-Bluetooth project. It takes raw captures from sniffer hardware, either an Ubertooth device or GR-Bluetooth with a USRP, and turns them into decoded Bluetooth packets and piconet information.

It exists as a shared decoding layer. Rather than each sniffer project reimplementing the baseband logic, the Ubertooth and GR-Bluetooth/USRP sources can lean on one library. It is not presented as an end-user application. Other tools build on it, and you link against it or use what those tools expose.

The door it opens is the air interface most people never see. Bluetooth devices hop between channels and talk in small networks called piconets, and a decoder like this is where raw radio samples start to become something readable. The README does not explain the decoding mechanism, so the details are a matter for reading the source.

Homebrew installs one executable, `btaptap`. The README does not mention it, so what it does is not confirmed here. Start with its `--help`.

## Install

```
brew install libbtbb
# Capturing packets needs an Ubertooth device or a GR-Bluetooth/USRP setup.
# Upstream builds from source with CMake: mkdir build && cd build && cmake .. && make && sudo make install
```

## Try this

```
btaptap --help
```
Prints usage for the one executable Homebrew installs, which the README does not document.

## What's unique

It is the decoding core shared by Ubertooth and GR-Bluetooth/USRP, turning raw radio captures into Bluetooth packet and piconet data that other tools build on.

## Caveats

The README calls the code incomplete and tested only on Linux, the latest release found is from December 2020, btaptap is undocumented, and capturing needs supported sniffer hardware.

## Links

- [Homepage and README (GitHub)](https://github.com/greatscottgadgets/libbtbb)
- [Releases](https://github.com/greatscottgadgets/libbtbb/releases)
- [Issue tracker](https://github.com/greatscottgadgets/libbtbb/issues)
