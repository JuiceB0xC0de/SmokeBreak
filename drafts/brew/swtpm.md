---
name: swtpm
title: swtpm
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, protocol, security, simulation, tpm, virtualization]
homepage: https://github.com/stefanberger/swtpm
scout_score: 6
status: draft
---

# swtpm

**TLDR;** A software TPM emulator that gives virtual machines a trusted platform module with no hardware, and lets you see how TPM identity certificates get made.

A TPM is a small chip that holds keys and measures what a machine boots. Secure boot, disk encryption and remote attestation all lean on it. swtpm fakes one in software. It wraps libtpms, which implements both TPM 1.2 and TPM 2, and serves TPM commands to clients over TCP, Unix sockets, or on Linux through CUSE, which creates native /dev/vtpm* devices.

The stated goal is a TPM emulator "that can be integrated into virtualized environments, such as virtual machines and containers." It has been integrated into QEMU and, as a prototype, into RunC. A guest OS can then see a TPM without the host owning one, which is useful for testing firmware, bootloaders and attestation code.

The package also ships tools that simulate how a TPM is made. swtpm_setup, swtpm_cert and swtpm_localca generate an endorsement key and the certificates that vouch for it, much as a manufacturer would. That is the door into the larger idea: a hardware root of trust is mostly a chain of signed claims, and you can build a toy version of that chain and read it.

State is kept in files, protected by ownership and permissions, and can optionally be encrypted with a secret you supply. The wiki also describes a confidential-computing migration model where TPM state moves between hosts using firmware-held keys.

## Install

```
brew install swtpm
# Brew installs the binaries and dependencies, including libtpms. Linux-only features such as CUSE (/dev/vtpm*) are not available on macOS. Most usage documentation lives in the project wiki and the per-tool READMEs under src/.
```

## Try this

```
swtpm --help
```
Lists the emulator's options, including the socket and CUSE interfaces, and how state is stored and encrypted.

```
swtpm_setup --help
```
Shows how the tool provisions a fresh emulated TPM, including generating its endorsement key and certificates.

```
swtpm_cert --help
```
Shows the options for creating EK and platform certificates, the step that simulates TPM manufacturing.

## What's unique

It is built to plug into virtualization stacks so a VM gets a vTPM without hardware. It also simulates TPM manufacturing, with EK and platform certificates, which is unusual for an open-source emulator.

## Caveats

As the README says, "Since the swtpm is fully implemented in software its security is not as strong as that of a hardware TPM"; root or a debugger can reach secrets, and the README is thin, so most usage is in the wiki.

## Links

- [GitHub repository (homepage)](https://github.com/stefanberger/swtpm)
- [Project wiki](https://github.com/stefanberger/swtpm/wiki)
