---
name: htpdate
title: htpdate
source: brew
category: fundamentals
commitment: quick
tags: [http, network, protocol, quick, time]
homepage: https://www.vervest.org/htp/
scout_score: 5
status: draft
---

# htpdate

**TLDR;** Sets your computer's clock from the Date headers of ordinary web servers, a way to keep time over HTTP without NTP.

htpdate is a command-line tool that synchronizes the local clock with remote web servers. Instead of speaking NTP, it reads the Date header that web servers include in their HTTP responses and uses that as a time source. The Homebrew description reads: "Synchronize time with remote web servers."

The idea underneath is that time is leaking out of the network all the time. Every web server stamps its responses with the current time, so any HTTP server you can reach is a rough clock. That matters on networks where NTP's UDP port is blocked or filtered but web traffic still flows. The tradeoff is precision: HTTP Date headers carry whole seconds, so this is a coarser clock than NTP gives you.

The details of its options and output were not confirmed for this entry, because the project's own documentation could not be reached. Read `htpdate --help` after installing to see what it actually offers.

## Install

```
brew install htpdate
```

## Try this

```
htpdate --help
```
Prints the tool's usage and options, the quickest way to see how it picks servers and whether it sets the clock or only reports.

## What's unique

It treats the ordinary web as a time source, using the HTTP Date header instead of a dedicated time protocol like NTP.

## Caveats

The project homepage redirects to a GitHub page that could not be confirmed, so maintenance status and platform details are unverified, and setting the system clock normally needs root.

## Links

- [Project homepage (redirects to GitHub)](https://www.vervest.org/htp/)
