---
name: twtxt
title: twtxt
source: brew
category: languages-and-oddities
commitment: quick
tags: [decentralised, microblogging, network, plain-text, protocol, quick]
homepage: https://github.com/buckket/twtxt
scout_score: 6
status: draft
---

# twtxt

**TLDR;** A microblogging format where your account is one plain text file at a URL, and the client merges the files you follow into a timeline.

twtxt is a command-line client and a small file format for microblogging. You publish by adding a line to a text file that is reachable over HTTP. Each line is a timestamp and a message. The URL of that file is your identity: in the README's words, "The URL pointing to this file is your identity, your account."

The client works like a feed reader. It polls the text files of the people you follow with asynchronous HTTP requests (the README names asyncio and aiohttp) and merges the lines into one timeline. There is no central server and no sign-up. Anyone who can host a static file can take part.

The author's stated reason is to offer an alternative to closed or regulated microblogging platforms, while staying simple, human readable, and easy to combine with UNIX tools. Because a post is just a line of text, the client is optional. The README says so directly: "Don't like the official client? Tweet using echo" followed by a one-line shell command.

The idea underneath is that a social network can be reduced to a file format and a convention. Following someone is a fetch, posting is an append, and discovery is left to community lists and registries. It is a good way to see how little a decentralised service needs.

## Install

```
brew install twtxt
# Python 3 is pulled in by the formula. To be readable by others, your feed file must be hosted at a publicly reachable URL.
```

## Try this

```
twtxt --help
```
Lists the client's subcommands so you can see how following, timelines, and posting are laid out.

```
echo -e "`date +%FT%T%:z`\tHello world!" >> twtxt.txt
```
Appends a tab-separated ISO timestamp and a message to twtxt.txt, which is a complete post in the format, no client needed.

## What's unique

Identity is nothing but a URL to a text file, with no server software or account, and a shell one-liner can write a valid post.

## Caveats

The brief could not confirm the project's release or commit recency, and the many third-party clients and registries it lists were not checked, so how active the community is today is unknown.

## Links

- [GitHub homepage and README](https://github.com/buckket/twtxt)
- [Documentation (readthedocs)](http://twtxt.readthedocs.org/en/latest/)
- [Demo recording (asciinema)](https://asciinema.org/a/1w2q3suhgrzh2hgltddvk9ot4)
- [Community list of active users (yarn.social)](https://git.mills.io/yarnsocial/we-are-twtxt)
