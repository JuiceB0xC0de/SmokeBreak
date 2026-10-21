---
name: tkey-ssh-agent
title: tkey-ssh-agent
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, isolation, needs-hardware, security-key, ssh, usb]
homepage: https://tillitis.se/
scout_score: 5
status: draft
---

# tkey-ssh-agent

**TLDR;** An SSH agent that signs logins on a Tillitis TKey USB stick, deriving the key from the signer app's own binary so no key file exists.

tkey-ssh-agent is an OpenSSH-compatible agent that runs as a daemon on a Unix socket (a named pipe on Windows). OpenSSH finds it through `SSH_AUTH_SOCK`. When asked to sign, the agent loads a small signer app onto the TKey, a compact USB-C security token, and the stick does the signing. The agent keeps no key material of its own. `--show-pubkey` prints the public key for pasting into `~/.ssh/authorized_keys`.

The interesting part is where the key comes from. There is no key file to generate or back up. The key pair is derived from the signer app binary, an optional User-Supplied Secret (USS), and a unique secret inside the stick (the UDS). Change any of the three and you get a different key pair. By default, each signature needs a physical touch on the stick.

The underlying idea comes from the TKey itself. The Tillitis homepage describes it as providing a secure, isolated environment for specialized apps, with authentication as one named use. In its words: "Applications are loaded onto TKey and run one at a time in complete isolation, preventing access to the secrets of other applications." This agent is one such application. The signer app's identity becomes part of your SSH identity, which is a different trust model from a key file on disk.

## Install

```
brew install tkey-ssh-agent
# then add to ~/.zshrc and/or ~/.bashrc:
export SSH_AUTH_SOCK="$HOMEBREW_PREFIX/var/run/tkey-ssh-agent.sock"
# requires a Tillitis TKey device; brew also pulls in pinentry-mac
```

## Try this

```
tkey-ssh-agent --help
```
Lists the agent's options, including the socket path and serial port flags.

```
./tkey-ssh-agent -a ./agent.sock --port /dev/pts/1
```
Starts the agent on a local socket using a specific port, needed when several TKeys are plugged in or when running under QEMU.

```
SSH_AUTH_SOCK=/path/to/agent.sock ssh -F /dev/null localhost
```
Tests a login to localhost through the agent, ignoring your ssh config.

## What's unique

The SSH key is derived from the signer app binary plus the device's secrets, so the exact app and firmware versions are part of the identity. There is no stored key file.

## Caveats

Needs a TKey device; the README says to use tagged releases for real use because changes on main can change your key pair, and older versions had a vulnerability, so keep it current.

## Links

- [Tillitis homepage](https://tillitis.se/)
- [GitHub repository and README](https://github.com/tillitis/tkey-ssh-agent)
- [Release notes](https://github.com/tillitis/tkey-ssh-agent/blob/main/docs/release_notes.md)
- [Tillitis app page for the agent](https://tillitis.se/app/tkey-ssh-agent/)
