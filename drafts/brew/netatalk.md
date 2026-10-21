---
name: netatalk
title: netatalk
source: brew
category: fundamentals
commitment: afternoon
tags: [afp, afternoon, apple, file-server, network, protocol, retro]
homepage: https://netatalk.io
scout_score: 6
status: draft
---

# netatalk

**TLDR;** A free file server that speaks Apple's old AFP protocol, so anything from Classic Mac OS to modern macOS can mount shares from it.

Netatalk is a file server for the Apple Filing Protocol (AFP), the network file sharing protocol Macs used for decades. It runs on UNIX-like systems and by default shares each authorized user's home directory. Per the project, most macOS, Mac OS X and Classic Mac OS systems can connect without extra software because it follows the AFP specification.

The executables list shows the package is more than one daemon. Alongside `afpd` there are CNID database daemons (`cnid_dbd`, `cnid_metad`), test tools (`afp_speedtest`, `afp_logintest`), and a set of names such as `atalkd`, `nbplkup`, `papd` and `timelord`. They look like pieces of the older AppleTalk network stack and printing support, though the brief does not explain them, so treat that as a lead rather than a fact.

The project's stated reason to exist is that AFP is still in use: its homepage says millions of Macs and NAS devices, archives, studios, labs and retro-computing setups still speak it. The homepage also says macOS 27 is the first Apple OS in 35 years without an AFP client. Release 4.6.0 ships Netatalk Client 1.0.0, so the project now covers both ends of an AFP connection, according to the page.

The door here is a network protocol with a long history, one you can run yourself and watch work. The project's own warning applies: "Netatalk has a dizzying amount of options which can be daunting initially."

## Install

```
brew install netatalk
# To authenticate as system users, set up PAM by hand (from the brew caveats):
sudo install -d -o $USER -g admin /usr/local/etc
mkdir -p /usr/local/etc/pam.d
cp $(brew --prefix)/etc/pam.d/netatalk /usr/local/etc/pam.d
# Basic sysadmin skills are assumed. Packages and Docker/Podman images are the project's other routes.
```

## Try this

```
afpd --help
```
Prints the options of the main AFP file server daemon, a first look at what can be configured.

```
afp_speedtest --help
```
Shows the options of one of the bundled test tools for measuring AFP performance.

```
cp $(brew --prefix)/etc/pam.d/netatalk /usr/local/etc/pam.d
```
Installs the PAM config so Netatalk can authenticate system users. Run it after creating the directories from the install notes.

## What's unique

It is a maintained, open source AFP server that also ships a matching AFP client, for a protocol Apple is dropping from macOS.

## Caveats

Setup assumes sysadmin skills, the option set is large, very old AFP clients need extra configuration, and Homebrew installs need a manual PAM step to authenticate system users.

## Links

- [Netatalk homepage](https://netatalk.io)
