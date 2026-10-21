---
name: gotpm
title: gotpm
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, attestation, go, needs-hardware, security, tpm]
homepage: https://github.com/google/go-tpm-tools
scout_score: 6
status: draft
---

# gotpm

**TLDR;** A command-line tool for talking to your machine's TPM 2.0 chip, from the Go library that handles attestation, sealing and PCR reads.

gotpm is the command-line tool that ships in the go-tpm-tools repository. The repo is mainly a Go library that sits on top of Go-TPM and offers simpler abstractions for a TPM 2.0 chip. Per its README, that library covers signing, attestation, reading PCRs, sealing and unsealing data, importing data and keys, reading NV data, and getting the TCG Event Log. The README does not list gotpm's subcommands, so the way in is `gotpm --help`.

Underneath is the idea that a small chip on the board can vouch for the state of the machine. It records measurements of what booted, and it can seal secrets so they open only when those measurements match. Most developers never touch this layer. This tool gives you a direct way to look at it.

The repo is split into a client side and a server side. The client package issues commands to the chip on the local machine. The server package never touches a TPM. It parses event logs, verifies attestations, and builds data to import into a TPM. The two exchange protocol buffer messages, so both ends of an attestation live in one codebase. A simulator package wraps Microsoft's TPM 2.0 simulator for testing.

The project supports TPM 2.0 only. Its README says to avoid TPM 1.2 because of its reliance on SHA1, "which is quite broken".

## Install

```
brew install gotpm
# Needs a TPM 2.0 device to do anything real. On Intel TDX confidential VMs you may also need the tdx_guest kernel module (sudo modprobe tdx_guest).
# Alternatives: go install github.com/google/go-tpm-tools/cmd/gotpm@latest, or a prebuilt binary from GitHub releases.
```

## Try this

```
gotpm --help
```
Lists the top-level commands. The README says to start here.

## What's unique

Most TPM tools are either low-level bindings or cloud attestation services. This one comes from a codebase with both a client that talks to the local chip and a server that verifies what it reports.

## Caveats

The README does not document gotpm's subcommands, so you rely on --help, and it needs a TPM 2.0 chip (or a simulator build that requires OpenSSL headers) to be useful; the README also says this is not an official Google product.

## Links

- [Homepage (GitHub repo)](https://github.com/google/go-tpm-tools)
- [Releases (prebuilt gotpm binaries)](https://github.com/google/go-tpm-tools/releases)
- [Go package docs](https://pkg.go.dev/github.com/google/go-tpm-tools)
