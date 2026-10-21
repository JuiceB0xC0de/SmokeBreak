---
name: c-kermit
title: C-Kermit
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, file-transfer, modem, protocol, scripting, serial]
homepage: https://www.kermitproject.org/
scout_score: 5
status: draft
---

# C-Kermit

**TLDR;** A single portable binary that handles serial lines, modems, Telnet and SSH, transfers files with a protocol from 1981, and automates it all with its own scripting language.

C-Kermit is a command-line communications program for Unix-family systems and OpenVMS. It opens a serial port, a dialed modem, or a Telnet, SSH or SSL/TLS connection, then runs the same terminal, file-transfer and scripting features over whichever transport you picked. Input is typed commands or Kermit script files. Output is a live terminal session, transferred files, or script results.

The Kermit protocol is what the project is named for. The homepage calls it "a robust and portable platform-and-transport-independent file-transfer protocol" that has been in use since 1981. It was built to move files between very different machines over unreliable lines. The idea underneath is that file transfer and session automation should not care what the wire is, whether a phone line, a serial cable or a TCP socket.

The scripting language is the other half. The project describes C-Kermit as an alternative to a long list of separate tools: cu, tip, minicom, telnet, ssh, expect, wget and more, and "to some extent even Lisp, your shell, and/or Perl". You can script a dial-up dialog, a login, or a file-management job in the same language you use interactively.

It is a way into the world of serial and modem communication, and a look at how much of it was solved before the modern internet. The stable release is 9.0.302 from 2011, and 10.0 is in beta, with a beta dated March 2025 on the homepage.

## Install

```
brew install c-kermit
# Installs kermit, kermit-sshsub and ckermit.ini. Serial or modem use needs a real device. The project also documents building from source with make, such as make linux or make macos, then make install.
```

## Try this

```
kermit --help
```
Prints the command-line options, a first look at what the program can do.

```
sudo apt install ckermit
```
On Ubuntu, installs the distro package instead of building from source, as the project's 9.0 page shows.

```
make macos
```
From the unpacked source directory, builds C-Kermit for macOS 2020 and later; make install then installs it.

## What's unique

It folds serial, modem, Telnet and SSH access, file transfer and a full scripting language into one binary, built on a protocol older than most terminal tools.

## Caveats

The last stable release is from 2011 and the active line is the 10.0 beta; dial-out can need manual owner and permission setup, and Homebrew marks the formula deprecated even though the homepage shows active beta work.

## Links

- [Kermit Project homepage](https://www.kermitproject.org/)
- [C-Kermit 9.0 page (download, build and install instructions)](https://www.kermitproject.org/ck90.html)
- [Kermit Software Archive 1981-2023](http://kermitproject.org/archive.html)
