---
name: logstalgia
title: Logstalgia
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [generative, gui, logs, quick, visual, web]
homepage: https://logstalgia.io/
scout_score: 6
status: draft
---

# Logstalgia

**TLDR;** Logstalgia turns a web server access log into a Pong game where each request is a ball and failed requests slip past the paddle.

Logstalgia reads web-server access logs and draws each request as a coloured ball that flies across the screen to the resource it asked for. Balls are coloured by the requesting host. It understands Apache and Nginx formats (NCSA Common, Combined, and virtual-host variants), a pipe-delimited custom format, or live input on STDIN. The output is an animation in a window, not a report or a file.

The Pong framing carries information. Successful requests are hit by the paddle, while failures such as 404 File Not Found are missed and pass through. A burst of misses is visible at a glance without reading a line of the log. The project's own description is "a pong-like battle between the web server and an never ending torrent of requests."

To keep a busy site readable, paths are summarised by finding common prefixes, and related paths are grouped under headings. By default anything ending in png, gif or jpg goes under 'Images' and everything else under 'Miscellaneous'. You can replay a saved log or follow a live one by piping tail -f into it.

The idea underneath is that a log is a stream of events, and a stream can be watched instead of searched. Once you see traffic as motion, patterns like crawlers, scans and broken links become things you notice rather than things you grep for.

## Install

```
brew install logstalgia
Needs a machine with OpenGL, so run it on a workstation rather than on the web server itself. Read logs from a file, or pipe them in over ssh.
```

## Try this

```
logstalgia data/example.log
```
Plays the bundled example access log with default settings.

```
tail -f /var/log/apache2/access.log | logstalgia -
```
Follows a live Apache log, starting from the most recent entries. The trailing '-' means read from STDIN.

```
ssh user@yourserver.com tail -f /var/log/apache2/access.log | logstalgia -g "Ad Clicks,/adclick.php,30" -
```
Watches a remote log over ssh and groups URLs containing /adclick.php under the heading 'Ad Clicks'.

## What's unique

It borrows the rules of Pong to encode request outcomes, so a 404 visibly gets past the defence. Prefix-based path grouping keeps a busy site's URLs legible on one screen.

## Caveats

It needs OpenGL and is not for headless servers, and the README says it only looks interesting with a fairly busy log, hundreds of requests per minute.

## Links

- [Logstalgia homepage](https://logstalgia.io/)
