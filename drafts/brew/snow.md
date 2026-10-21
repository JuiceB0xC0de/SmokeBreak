---
name: snow
title: snow
source: brew
category: languages-and-oddities
commitment: quick
tags: [encryption, quick, steganography, text, whitespace]
homepage: https://darkside.com.au/snow/
scout_score: 8
status: draft
---

# snow

**TLDR;** Hides a message in the invisible spaces and tabs at the ends of lines of ordinary text, with optional encryption on top.

SNOW is a small command-line steganography tool. It takes a message and appends spaces and tabs to the ends of lines in an ASCII text file. In most viewers those characters are invisible, so the text looks unchanged while carrying a payload. The name stands for the Steganographic Nature Of Whitespace.

The homepage presents it as concealment first and encryption second. The message can be encrypted with the built-in ICE algorithm, so even a reader who spots the trailing whitespace still faces ciphertext. In the author's words: "Locating trailing whitespace in text is like finding a polar bear in a snowstorm."

The idea underneath is that hiding is different from encrypting. Encryption makes a message unreadable but obviously present, while steganography tries to hide that a message exists at all. Whitespace is a good place to look because nobody reads it, and it is also why diff tools, editors, and linters that strip trailing spaces can destroy such a message. That makes it a quick way into questions about covert channels and how text gets handled.

The project is old. The newest source on the homepage is dated 2013, and the page also carries a 1998 history of encryption bugs that were fixed. The homepage also links a JavaScript version and a CGI script that hides messages in HTML pages, though I could not follow those links.

## Install

```
brew install snow
```

## Try this

```
snow --help
```
Prints the usage summary, so you can see the options for concealing and extracting a message and for setting a password.

## What's unique

It hides data in trailing whitespace, which almost nobody inspects, and pairs that with a real cipher so a discovered message is still unreadable.

## Caveats

The project is old: the newest source is from 2013, and I could not check the manual page or the 'How it works' page, so the exact encoding and flags are unverified here.

## Links

- [SNOW homepage](https://darkside.com.au/snow/)
- [Source tarball (snow-20130616.tar.gz)](https://darkside.com.au/snow/)
- [Documentation and manual page (linked from homepage, not fetched)](https://darkside.com.au/snow/)
