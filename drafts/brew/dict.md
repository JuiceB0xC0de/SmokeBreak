---
name: dict
title: dict
source: brew
category: fundamentals
commitment: quick
tags: [ancient, dictionary, network, protocol, quick, rfc]
homepage: https://dict.org/bin/Dict
scout_score: 5
status: draft
---

# dict

**TLDR;** A command-line client for RFC 2229, the old dictionary protocol, with a live public server and tools to host or build your own dictionaries.

dict speaks the DICT protocol, defined in RFC 2229. You ask a server for a word, name a database, and get definitions back as plain text over a network connection. The Homebrew description calls it a client for exactly that.

The public server behind dict.org is still live. Its web form, which is the project's homepage, offers search strategies such as exact headword, prefix, substring, suffix, regular expression, SOUNDEX, and Levenshtein distance one. The brief says it serves many dictionaries, including WordNet, the Jargon File, the Free On-line Dictionary of Computing, and CC-CEDICT. Version dates on that page run into 2026, so the server looks maintained.

The formula installs more than a client. The executable list includes dictd (a server), dictfmt and dictunformat (for building and converting dictionary data), and dictzip (a compression tool). That makes it a small door into the whole idea: a lookup service with its own wire protocol, dictionary file format, and server, all from an era when each such service got its own protocol.

The brief found no README or docs for the client itself, so the details of usage are left to the tool's own help output.

## Install

```
brew install dict
# also installs the dictd server and dictfmt tools; the client needs network access to a DICT server
```

## Try this

```
dict --help
```
Lists the client's options, including how to choose a server, database, and match strategy.

```
dictd --help
```
Shows the options for the bundled dictionary server.

```
dictfmt --help
```
Shows how the dictionary-building tool is used to turn text into a dictd database.

## What's unique

It is a client, a server, and a dictionary-compiling toolkit for a niche protocol, and a public server is still online to try it against.

## Caveats

The brief found no docs, release dates, or maintenance notes for the client package itself, only the public server's web form, so usage details are unconfirmed.

## Links

- [DICT homepage (search form for the public server)](https://dict.org/bin/Dict)
- [dict.org root (same search form)](https://www.dict.org/)
