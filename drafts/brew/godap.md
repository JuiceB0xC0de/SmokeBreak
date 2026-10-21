---
name: godap
title: godap
source: brew
category: fundamentals
commitment: afternoon
tags: [active-directory, afternoon, go, kerberos, ldap, protocol, tui]
homepage: https://github.com/Macmod/godap
scout_score: 5
status: draft
---

# godap

**TLDR;** A terminal UI that lets you browse and edit an LDAP directory, mostly Active Directory, as an expandable tree of objects.

godap connects to a directory server, usually an Active Directory domain controller, and shows its contents as a tree you expand with the keyboard. It can search, create, edit, move and delete objects and attributes. It can also inspect and edit DACLs and userAccountControl flags, edit ADIDNS records, view GPOs, and export subtrees or results to JSON.

The README calls it "A complete terminal user interface (TUI) for LDAP." The author says it "started as a fun side project, but has become a really useful tool since then." The main focus is Active Directory. For other LDAP servers, the README suggests setting the `--backend` flag.

The idea underneath is that a directory is a database of objects, attributes and access rules, and most developers only see it through a login prompt. Browsing it directly shows how identity, group membership and permissions are stored. It also shows how many ways a client can prove who it is. godap can bind with a password, an NT hash, Kerberos (CCACHE, password, hash, AES key or PKINIT), or a client certificate. It can switch between them at runtime from a connection panel.

It is a single Go binary. It talks LDAP, LDAPS or StartTLS, optionally through a SOCKS proxy, and loads objects on demand while caching them in memory.

## Install

```
brew install godap
# Needs an LDAP server to connect to, usually an Active Directory domain controller. No account or hardware is required for the tool itself. Kerberos binds need a reachable KDC.
```

## Try this

```
godap --help
```
Lists the bind, TLS, proxy and backend flags.

```
godap <hostname or IP> -u <username> -p <password> -d <domain>
```
Binds with NTLM by default and opens the directory as an expandable object tree. Add --simple for a simple bind.

```
godap <hostname or IP> [bind flags] -S -I
```
Uses LDAPS for the initial connection and ignores certificate validation, which suits a lab server with a self-signed certificate.

## What's unique

It puts Active Directory browsing, DACL and ACE editing, ADIDNS records, GPO viewing and several authentication methods into one terminal UI, in place of a pile of separate scripts.

## Caveats

The README calls it highly experimental and says it was tested mainly on Windows Server 2019. Point it only at directories you own or are authorised to edit, and expect slower progress because the author has limited time.

## Links

- [GitHub homepage and README](https://github.com/Macmod/godap)
- [Wiki (usage examples)](https://github.com/Macmod/godap/wiki)
- [Releases (prebuilt binaries)](https://github.com/Macmod/godap/releases)
