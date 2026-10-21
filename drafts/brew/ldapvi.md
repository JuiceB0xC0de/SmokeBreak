---
name: ldapvi
title: ldapvi
source: brew
category: fundamentals
commitment: quick
tags: [editor, ldap, protocol, quick, tui]
homepage: http://www.lichteblau.com/ldapvi/
scout_score: 6
status: draft
---

# ldapvi

**TLDR;** ldapvi pulls entries from an LDAP directory into your text editor and writes your edits back on save, like vipw for LDAP.

ldapvi is an interactive LDAP client for Unix terminals. You point it at a directory, it fetches the entries you ask for and opens them in your editor. You change the text, save, and the differences are sent back to the server.

The homepage sums it up in one line: "Think of it as vipw(1) for LDAP." vipw is the old Unix tool for editing the password file in a normal editor, with a safety net around it. ldapvi applies the same idea to a directory server. A live directory entry becomes something you edit like a file, rather than something you change through an admin GUI or a string of separate LDAP operations.

The idea underneath is that a protocol most developers only meet through login and identity systems has a plain, readable shape. Entries are names with attributes and values. Seeing them as text in your own editor is a quick way to learn what a directory holds and how it is structured.

## Install

```
brew install ldapvi
# you need access to an LDAP server to do anything useful with it
```

## Try this

```
ldapvi --help
```
Prints the available options, including how to point it at a server and what to fetch.

## What's unique

It treats live directory entries as a file in your own editor, in the spirit of vipw, instead of a dedicated admin tool or a series of LDAP command-line operations.

## Caveats

The homepage shows no release dates and gives no install instructions or usage examples, so whether it is actively maintained is unconfirmed, and you need an LDAP server to try it on.

## Links

- [ldapvi homepage](http://www.lichteblau.com/ldapvi/)
