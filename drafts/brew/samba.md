---
name: samba
title: Samba
source: brew
category: fundamentals
commitment: afternoon
tags: [active-directory, afternoon, cifs, file-sharing, network, protocol, smb]
homepage: https://www.samba.org/
scout_score: 6
status: draft
---

# Samba

**TLDR;** Samba is the open source implementation of Windows file sharing (SMB) and Active Directory protocols, shipped with dozens of tools for poking at both.

Samba implements SMB/CIFS, the protocol Windows uses for file and print sharing, along with the Active Directory pieces around it, including LDAP and Kerberos. It lets a Linux or UNIX machine serve shares to Windows clients, join a domain as a member server, or act as a full Active Directory domain controller.

The formula installs far more than the server daemons (smbd, nmbd). It also ships a large set of client and admin tools: smbclient for browsing shares, rpcclient for talking to Windows-style RPC services, net for domain and share administration, testparm for checking config, smbstatus for seeing who is connected. There are also registry tools (regshell, regtree, regdiff) and LDB database tools (ldbsearch, ldbedit).

The idea underneath is a protocol that runs quietly in most offices and homes and is rarely looked at directly. Samba exists to integrate Linux and UNIX servers and desktops into Windows and Active Directory environments, and in doing so it has had to reimplement a great deal of Windows networking in the open. Its tool list works as a map of that territory.

## Install

```
brew install samba
# Homebrew installs smbd as $HOMEBREW_PREFIX/sbin/samba-dot-org-smbd and profiles as $HOMEBREW_PREFIX/bin/samba-dot-org-profiles, to avoid clashing with macOS system binaries.
```

## Try this

```
smbclient --help
```
Lists the options for the command-line SMB client, which can browse and transfer files on any SMB share.

```
testparm --help
```
Shows how to validate a Samba configuration file and dump the settings it resolves to.

```
net --help
```
Prints the subcommands of Samba's general-purpose administration tool for shares, users, and domains.

## What's unique

Samba is one of the few open source projects that lets a non-Windows machine sit inside an Active Directory domain as a full domain controller, not just a file share. Its toolkit of more than 40 executables covers server, client, registry, and LDAP-style database work.

## Caveats

The project is actively maintained, but the brief shows no example commands and the docs note that the man pages come from the development version, so they may differ from what Homebrew installs. Running a server also means writing your own configuration.

## Links

- [Samba homepage](https://www.samba.org/)
- [Samba documentation index](https://www.samba.org/samba/docs/)
