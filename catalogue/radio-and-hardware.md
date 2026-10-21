# Radio and hardware

SDR, ISM-band decoding, USB and HID poking, serial, anything that talks to a physical thing. Often needs hardware, tag it.

85 entries. [Back to the shelf](README.md)

## quick

- **[ddcctl](../drafts/brew/ddcctl.md)**: A macOS command-line tool that changes an external monitor's brightness, contrast and input source by sending DDC/CI commands down the display cable.  
  `ddc, macos, monitor, needs-hardware`
- **[gnirehtet](../drafts/brew/gnirehtet.md)**: Gives an Android phone your computer's internet connection over USB, tethering in reverse, with no root and no UI on the phone.  
  `adb, android, needs-hardware, network, tunneling, usb`
- **[hidapitester](../drafts/brew/hidapitester.md)**: A command-line tool that finds USB HID devices and sends or reads raw reports as hex, so you can talk to keyboards, LEDs and gadgets from the shell.  
  `hid, needs-hardware, protocol, reports, usb`
- **[m1ddc](../drafts/brew/m1ddc.md)**: A tiny command-line tool that talks DDC/CI to external monitors on Apple Silicon Macs, so you can set brightness, volume or input from a script.  
  `ddc, macos, monitors, needs-hardware, protocol`
- **[mbpoll](../drafts/brew/mbpoll.md)**: A command-line Modbus master that reads and writes registers on PLCs and sensors over serial or TCP, a way into the protocol factories run on.  
  `industrial, modbus, needs-hardware, protocol, serial`
- **[mpremote](../drafts/brew/mpremote.md)**: A command-line tool that opens a Python prompt on a MicroPython board over USB serial, and copies files, runs scripts, and mounts folders.  
  `micropython, needs-hardware, python, repl, serial`
- **[usbtree](../drafts/brew/usbtree.md)**: A live, color-coded USB device tree in your terminal that flashes hot-plugged devices and shows unplugged ones as red ghosts.  
  `hot-plug, needs-hardware, rust, tui, usb`

## afternoon

- **[Aravis](../drafts/brew/aravis.md)**: A C library that speaks the GigE Vision and USB3 protocols of industrial cameras, with a built-in fake camera so you can try it without hardware.  
  `cameras, genicam, library, needs-hardware, protocol`
- **[avrdude](../drafts/brew/avrdude.md)**: A command-line tool that writes compiled programs into the flash memory of AVR microcontrollers, the chips inside Arduino boards, through a physical programmer.  
  `arduino, avr, flashing, microcontrollers, needs-hardware`
- **[Cahute](../drafts/brew/cahute.md)**: A C library and command-line tools for talking to Casio calculators over serial and USB, covering about three decades of hardware and wire protocols.  
  `calculators, library, needs-hardware, reverse-engineering, serial, usb`
- **[cdrdao](../drafts/brew/cdrdao.md)**: Burns CDs in disk-at-once mode from a plain-text description of the disc, giving control over pre-gaps and sub-channel data that most burners hide.  
  `ancient, burning, cd, cd-text, needs-hardware, optical`
- **[ddcutil](../drafts/brew/ddcutil.md)**: A Linux command-line tool that changes your external monitor's brightness, colour levels and input source over DDC/CI, the same settings the buttons on the bezel control.  
  `i2c, linux, monitors, needs-hardware, protocol`
- **[dfu-programmer](../drafts/brew/dfu-programmer.md)**: A command-line tool that flashes Atmel microcontrollers over USB using the DFU protocol, for chips that already carry a DFU bootloader.  
  `atmel, dfu, firmware, microcontrollers, needs-hardware, usb`
- **[DigiTemp](../drafts/brew/digitemp.md)**: Reads Dallas/Maxim 1-Wire temperature sensors from the command line, a hands-on way into a bus where many sensors share one wire.  
  `1-wire, needs-hardware, protocol, sensors, serial, usb`
- **[Dire Wolf](../drafts/brew/direwolf.md)**: A software modem that turns radio audio into AX.25 packets and APRS frames, replacing the 1980s hardware TNC with a soundcard and DSP.  
  `aprs, audio, ax25, ham-radio, modem, needs-hardware, sdr`
- **[dump1090-fa](../drafts/brew/dump1090-fa.md)**: Decodes the transponder messages airplanes broadcast overhead, turning a cheap SDR dongle into a live aircraft display in a terminal or browser map.  
  `adsb, aircraft, needs-hardware, radio, sdr`
- **[FreeIPMI](../drafts/brew/freeipmi.md)**: GNU command-line tools for talking to a server's baseboard management controller: read sensors, event logs, power state, and serial console, locally or over the network.  
  `bmc, ipmi, needs-hardware, network, protocol, servers`
- **[fwupd](../drafts/brew/fwupd.md)**: The Linux firmware update daemon: it finds devices in your machine, pulls vendor firmware metadata from LVFS, and flashes updates live or at next boot.  
  `firmware, linux, lvfs, needs-hardware, protocol`
- **[gammu](../drafts/brew/gammu.md)**: A command-line toolkit for controlling a mobile phone: read and send SMS, export contacts and calendars, and browse the phone's files from a terminal.  
  `daemon, library, needs-hardware, phones, sms`
- **[GNU Radio](../drafts/brew/gnuradio.md)**: A toolkit for building software radios by wiring signal-processing blocks into flowgraphs, drawn in a GUI or written in Python or C++.  
  `gui, needs-hardware, python, radio, sdr, signal-processing`
- **[gotpm](../drafts/brew/gotpm.md)**: A command-line tool for talking to your machine's TPM 2.0 chip, from the Go library that handles attestation, sealing and PCR reads.  
  `attestation, go, needs-hardware, security, tpm`
- **[gphoto2](../drafts/brew/gphoto2.md)**: A command-line program that talks to over 2700 digital cameras and media players through libgphoto2, built so free systems don't need vendor software.  
  `cameras, gpl, needs-hardware, ptp, usb`
- **[gpsd](../drafts/brew/gpsd.md)**: A daemon that reads GPS receivers on serial or USB and serves position, course and velocity as JSON on TCP port 2947, so many programs can share one sensor.  
  `daemon, gps, needs-hardware, network, protocol, serial`
- **[HackRF](../drafts/brew/hackrf.md)**: Command-line tools for HackRF, an open-source software-defined radio board that lets your computer transmit and receive across a wide slice of the radio spectrum.  
  `needs-hardware, open-hardware, radio, sdr, usb`
- **[Hamlib](../drafts/brew/hamlib.md)**: One shared API and a set of command-line tools for controlling ham radio transceivers, rotators and amplifiers over serial, USB or a plain TCP socket.  
  `ham-radio, library, needs-hardware, radio, serial, tcp`
- **[i2c-tools](../drafts/brew/i2c-tools.md)**: Command-line tools for scanning I2C buses, dumping chip registers, and decoding the EEPROMs inside your RAM sticks and monitor.  
  `eeprom, i2c, linux, needs-hardware, protocol`
- **[ifuse](../drafts/brew/ifuse.md)**: Mounts a USB-connected iPhone or iPad as an ordinary folder, using a reimplemented Apple protocol stack and no Apple software.  
  `fuse, ios, needs-hardware, protocol, usb`
- **[inspectrum](../drafts/brew/inspectrum.md)**: A desktop tool that opens recorded radio captures as zoomable spectrograms, so you can measure and decode signals long after they were received.  
  `gui, iq, needs-capture-file, sdr, signals, spectrogram`
- **[ios-webkit-debug-proxy](../drafts/brew/ios-webkit-debug-proxy.md)**: Bridges the debugging protocol iOS exposes over USB to websockets, so you can inspect Safari tabs on a real iPhone from a desktop.  
  `debugging, ios, needs-hardware, protocol, usb, websocket`
- **[Jaguar](../drafts/brew/jaguar.md)**: Jaguar pushes Toit programs to an ESP32 over WiFi and restarts them in under two seconds, with no reflashing or rebooting.  
  `embedded, esp32, live-reload, needs-hardware, toit, wifi`
- **[libbladeRF](../drafts/brew/libbladerf.md)**: Host driver and command-line tools for the bladeRF USB 3.0 software defined radio, which turns a computer into a transceiver from 47 MHz to 6 GHz.  
  `fpga, library, needs-hardware, radio, sdr, usb`
- **[libbtbb](../drafts/brew/libbtbb.md)**: A C library that decodes Bluetooth baseband packets and piconet details from Ubertooth or USRP sniffer captures, opening up the radio layer beneath Bluetooth.  
  `bluetooth, library, needs-hardware, protocol, sniffing`
- **[libcec](../drafts/brew/libcec.md)**: A library and command-line client for HDMI-CEC, the hidden control channel in HDMI cables that lets a computer talk to your TV and other devices.  
  `cec, hdmi, library, needs-hardware, protocol`
- **[libdivecomputer](../drafts/brew/libdivecomputer.md)**: An open source C library that talks to dive computers from Shearwater, Suunto, Scubapro and many other makers over serial, USB and Bluetooth.  
  `bluetooth, library, needs-hardware, protocol, reverse-engineering, usb`
- **[libfreefare](../drafts/brew/libfreefare.md)**: A C library and set of command-line tools for talking to MIFARE contactless cards, the chips inside many access badges and transit tickets.  
  `c-library, mifare, needs-hardware, nfc, protocol, rfid`
- **[libfreenect](../drafts/brew/libfreenect.md)**: A userspace driver that turns an original Xbox 360 Kinect into a USB depth camera, with demo viewers and a record-and-replay trick for working without the hardware.  
  `depth-camera, kinect, library, needs-hardware, usb, visual`
- **[libgphoto2](../drafts/brew/libgphoto2.md)**: A C library that lets programs talk to digital cameras over USB using PTP and other protocols, and the engine under gphoto2, digiKam and Darktable.  
  `cameras, library, needs-hardware, ptp, usb`
- **[libimobiledevice](../drafts/brew/libimobiledevice.md)**: A free C library and command-line toolkit that talks to iPhones and iPads over Apple's own protocols, no iTunes needed, so you can read device info, logs and screenshots from a terminal.  
  `c-library, ios, needs-hardware, protocol, usb`
- **[libirecovery](../drafts/brew/libirecovery.md)**: A library and command-line tool that talks to the iBoot bootloader of an Apple device in recovery mode over raw USB, below the operating system.  
  `bootloader, ios, library, needs-hardware, reverse-engineering, usb`
- **[libklvanc](../drafts/brew/libklvanc.md)**: A C library and set of small tools for decoding and generating VANC, the hidden ancillary data (captions, ad cues, timecode) carried inside broadcast SDI video.  
  `broadcast, library, needs-hardware, protocol, sdi, vanc, video`
- **[libnfc](../drafts/brew/libnfc.md)**: A C library and 21 command-line tools for talking directly to NFC readers, so you can list, poll, emulate and relay contactless tags yourself.  
  `c, library, needs-hardware, nfc, protocol`
- **[libplctag](../drafts/brew/libplctag.md)**: A small C library that reads and writes tags on Allen-Bradley and Omron PLCs over Ethernet, a way into how industrial controllers talk.  
  `c-library, ethernet-ip, industrial, modbus, needs-hardware, plc, protocol`
- **[libpointing](../drafts/brew/libpointing.md)**: A C++ library that reads raw mouse events and replicates the pointer acceleration curves of Windows, macOS and Xorg, so you can compare them on the same input.  
  `c++, hid, library, mouse, needs-hardware`
- **[librealsense](../drafts/brew/librealsense.md)**: The open-source SDK for Intel RealSense depth cameras, with a viewer and dozens of small example tools that turn a camera into distances in meters.  
  `depth-camera, library, needs-hardware, robotics, visual`
- **[librtlsdr](../drafts/brew/librtlsdr.md)**: Turns a cheap Realtek RTL2832 TV-tuner USB dongle into a software-defined radio receiver, with a set of small command-line tools.  
  `needs-hardware, radio, sdr, usb`
- **[liquidctl](../drafts/brew/liquidctl.md)**: One command-line tool and Python library that reads and controls PC liquid coolers, fan hubs, RGB lighting and memory from many vendors, without their own software.  
  `hid, needs-hardware, pc-hardware, python, rgb, usb`
- **[LuaRadio](../drafts/brew/luaradio.md)**: A tiny software-defined radio framework where you wire up receivers as plain Lua scripts: source, filters, demodulator, audio out, then run().  
  `dsp, flow-graph, lua, needs-hardware, sdr`
- **[lxi-tools](../drafts/brew/lxi-tools.md)**: Command-line and GUI tools for finding and talking to network-attached lab instruments like oscilloscopes and power supplies, using SCPI over LXI.  
  `lua, needs-hardware, network, protocol, scpi, test-equipment`
- **[minipro](../drafts/brew/minipro.md)**: A command-line driver for the cheap TL866 and T48/T56 chip programmers, for reading and writing AVRs, PICs, BIOS chips and EEPROMs from Linux or macOS.  
  `eeprom, firmware, needs-hardware, reverse-engineering, usb`
- **[nextpnr-ice40](../drafts/brew/nextpnr-ice40.md)**: An open-source place and route tool that turns a synthesized netlist into a configuration for Lattice iCE40 FPGAs, with a GUI that shows the layout forming.  
  `fpga, needs-hardware, open-source-toolchain, place-and-route, verilog`
- **[nmrpflash](../drafts/brew/nmrpflash.md)**: Rescues bricked Netgear routers by impersonating the recovery server their bootloader listens for, then pushing a firmware image over Ethernet.  
  `firmware, needs-hardware, network, protocol, reverse-engineering, router`
- **[NUT (Network UPS Tools)](../drafts/brew/nut.md)**: One naming scheme and one network protocol for talking to hundreds of brands of UPS, PDU and solar controller, with drivers for serial and USB.  
  `needs-hardware, network, power, protocol, serial, ups, usb`
- **[OLA (Open Lighting Architecture)](../drafts/brew/ola.md)**: A daemon and toolkit for talking to stage lighting gear over DMX, Art-Net and sACN, a protocol world most developers never touch.  
  `art-net, dmx, lighting, needs-hardware, protocol, sacn`
- **[OpenOCD](../drafts/brew/open-ocd.md)**: An open-source tool that talks to the debug port of a microcontroller over JTAG or SWD, so you can flash, halt and inspect a chip directly.  
  `boundary-scan, debugging, embedded, jtag, needs-hardware, swd`
- **[OpenCBM](../drafts/brew/opencbm.md)**: Command-line tools and a driver that let a modern PC talk to real Commodore 1541 floppy drives over the IEC serial bus.  
  `commodore, floppy, iec-bus, needs-hardware, retro, usb`
- **[openFPGALoader](../drafts/brew/openfpgaloader.md)**: One command-line tool that loads bitstreams onto FPGAs from many vendors, replacing a drawer of vendor-specific programmers.  
  `bitstream, fpga, jtag, needs-hardware, usb`
- **[OpenHMD](../drafts/brew/openhmd.md)**: An open C library with reverse-engineered drivers that reads head tracking from many competing VR headsets through one API. Unmaintained, but a clear look at USB HID hardware.  
  `c-library, needs-hardware, reverse-engineering, usb-hid, vr`
- **[OpenSC](../drafts/brew/opensc.md)**: A toolkit of about two dozen command-line tools and libraries for talking to cryptographic smart cards, from listing their files to signing with their keys.  
  `apdu, crypto, needs-hardware, pkcs11, protocol, smart-cards`
- **[Orbuculum](../drafts/brew/orbuculum.md)**: A crystal ball for microcontrollers: command-line tools that read the trace pins of an Arm Cortex-M chip and show printf text, profiles and instruction trace while firmware runs.  
  `arm, debugging, embedded, firmware, needs-hardware, tracing`
- **[OWFS](../drafts/brew/owfs.md)**: A filesystem for the Dallas/Maxim 1-Wire bus, where cheap sensors and switches show up as files you can read and write from the shell.  
  `1-wire, filesystem, needs-hardware, protocol, sensors`
- **[pcsc-lite](../drafts/brew/pcsc-lite.md)**: The open-source PC/SC daemon for smart card readers, with a spy mode that logs the raw APDU conversations between software and a card.  
  `apdu, needs-hardware, protocol, smartcard, usb`
- **[picotool](../drafts/brew/picotool.md)**: Raspberry Pi's official command-line tool for inspecting, flashing and reading back RP2040/RP2350 microcontroller binaries and the chips running them, over USB.  
  `firmware, microcontroller, needs-hardware, rp2040, rp2350, usb`
- **[powerman](../drafts/brew/powerman.md)**: Remote, parallel control of switched power distribution units, driven by expect-style scripts that teach it new hardware. A look at how clusters get power-cycled.  
  `datacenter, needs-hardware, network, pdu, power`
- **[probe-rs](../drafts/brew/probe-rs-tools.md)**: A Rust toolkit that flashes, runs and debugs microcontrollers through a hardware debug probe, streaming the chip's log output back to your terminal.  
  `debugging, embedded, jtag, needs-hardware, rust, swd`
- **[qdl](../drafts/brew/qdl.md)**: A command-line tool that talks to Qualcomm chips in USB Emergency Download mode, loading a programmer and flashing firmware even to devices that will not boot.  
  `firmware, flashing, needs-hardware, protocol, qualcomm, usb`
- **[qdmr](../drafts/brew/qdmr.md)**: A GUI and command-line tool that writes DMR radio configs as plain text files instead of vendor binaries, then uploads them to cheap handhelds over USB.  
  `cli, dmr, file-formats, gui, ham-radio, needs-hardware, usb`
- **[readsb](../drafts/brew/readsb.md)**: Decodes the radio chatter aircraft broadcast about their position and identity, turning a cheap RTL-SDR dongle into a live table of planes overhead.  
  `ads-b, aircraft, needs-hardware, network, radio, sdr`
- **[rpiboot](../drafts/brew/rpiboot.md)**: Turns a Raspberry Pi's boot ROM into a USB file server, so a Compute Module's storage shows up as a plain USB drive on your computer.  
  `bootloader, needs-hardware, protocol, raspberry-pi, usb`
- **[rtl_433](../drafts/brew/rtl_433.md)**: Decodes the radio chatter of weather stations, doorbells, tyre sensors and meters around you, using a cheap USB radio dongle and one command.  
  `ism-band, needs-hardware, radio, sdr`
- **[SDR-- (sdrmm)](../drafts/brew/sdrmm.md)**: A patch-cable style software-defined radio app that runs on your desktop or on a server beside the antenna, with a browser as the front panel.  
  `decoders, needs-hardware, network, sdr, server`
- **[ser2net](../drafts/brew/ser2net.md)**: A daemon that puts a serial port on the network, so a UPS, router console or old instrument can be reached with a TCP connection instead of a cable.  
  `gensio, needs-hardware, network, protocol, serial`
- **[sigrok-cli](../drafts/brew/sigrok-cli.md)**: A command-line front end to sigrok that captures and decodes signals from logic analyzers, oscilloscopes and multimeters, built with scripting in mind.  
  `logic-analyzer, needs-hardware, protocol-decoding, scripting`
- **[sispmctl](../drafts/brew/sispmctl.md)**: A small C tool that switches Gembird and Energenie USB power strips on and off from the command line, with schedules and a tiny web panel.  
  `http, libusb, needs-hardware, power-strip, usb`
- **[Snap7](../drafts/brew/snap7.md)**: An Ethernet library that speaks the Siemens S7 protocol, so your own code can read and write memory in real factory PLCs, or in a fake one it hosts.  
  `industrial, library, needs-hardware, network, plc, protocol`
- **[SoapyRemote](../drafts/brew/soapyremote.md)**: Turns any SoapySDR-supported radio into a network device, so software on one machine can tune and stream from an SDR plugged into another.  
  `needs-hardware, network, sdr, streaming, udp`
- **[stm32flash](../drafts/brew/stm32flash.md)**: A small command-line tool that programs STM32 microcontrollers through the chip's built-in serial bootloader, using only a USB-serial adapter and no debug probe.  
  `bootloader, firmware, microcontroller, needs-hardware, serial, stm32`
- **[tkey-ssh-agent](../drafts/brew/tkey-ssh-agent.md)**: An SSH agent that signs logins on a Tillitis TKey USB stick, deriving the key from the signer app's own binary so no key file exists.  
  `isolation, needs-hardware, security-key, ssh, usb`
- **[Ubertooth](../drafts/brew/ubertooth.md)**: Host tools for the Ubertooth One, an open 2.4 GHz board that sniffs Bluetooth LE traffic and feeds it into Wireshark.  
  `2.4ghz, ble, bluetooth, needs-hardware, radio, sniffer, wireshark`
- **[uhubctl](../drafts/brew/uhubctl.md)**: A command-line tool that cuts and restores power to individual ports on USB hubs, so you can reboot a stuck device from software.  
  `libusb, needs-hardware, power-control, raspberry-pi, usb`
- **[Universal Radio Hacker (urh)](../drafts/brew/urh.md)**: A GUI suite that turns raw SDR captures into readable bits, then helps you work out what the protocol fields mean.  
  `gui, needs-hardware, protocols, reverse-engineering, sdr`
- **[uuu](../drafts/brew/uuu.md)**: A command-line tool that talks to the i.MX boot ROM over USB and pushes bootloaders or whole disk images onto a bare NXP board.  
  `bootloader, embedded, needs-hardware, nxp, protocol, usb`
- **[VRPN](../drafts/brew/vrpn.md)**: A network layer that makes VR trackers, buttons and dials look identical to applications, wherever the hardware is plugged in.  
  `library, needs-hardware, peripherals, protocol, vr`
- **[wiiuse](../drafts/brew/wiiuse.md)**: A small C library that pairs Nintendo Wii Remotes over Bluetooth and hands their motion, IR, and expansion data to your own program.  
  `bluetooth, c, library, needs-hardware, wii`
- **[wmbusmeters](../drafts/brew/wmbusmeters.md)**: Decodes wired and wireless M-Bus utility meter telegrams from radio dongles into readable fields, so you can read your own water or heat meter.  
  `mqtt, needs-hardware, protocol, radio, sdr, utility-meters`
- **[xNVMe](../drafts/brew/xnvme.md)**: One C API and a set of command-line tools for talking to NVMe drives from user space, with the I/O backend picked at runtime.  
  `c-library, io_uring, needs-hardware, nvme, storage, user-space`
