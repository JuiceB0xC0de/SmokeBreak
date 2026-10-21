---
name: swaks
title: swaks
source: brew
category: fundamentals
commitment: quick
tags: [email, perl, protocol, quick, smtp, testing]
homepage: https://www.jetmore.org/john/code/swaks/
scout_score: 5
status: draft
---

# swaks

**TLDR;** A command-line SMTP test tool that walks a mail server through a transaction step by step, printing every line of the conversation and stopping wherever you choose.

Swaks connects to a mail server and sends a test message, showing the full SMTP conversation as it happens. You give it a recipient and optionally a sender, server, authentication, TLS settings, headers, body or attachments. If you leave out the server, it looks up the MX records for the recipient's domain and talks to whatever it finds there.

The author calls its primary design goal "a flexible, scriptable, transaction-oriented SMTP test tool." The word transaction matters. Email delivery is a short dialogue of connect, greeting, STARTTLS, AUTH, MAIL, RCPT, DATA. Swaks lets you stop at any of those points with `--quit-after` or `--drop-after`. That makes it useful for asking a server narrow questions, such as whether it accepts a given recipient, without ever sending a message.

It also reaches past TCP. It can speak SMTP, ESMTP or LMTP, connect to a UNIX-domain socket, or spawn a local program and talk to it over stdin and stdout. The docs show it driving Exim's test mode this way. Operators use it to check virus and spam scanners with the standard EICAR and GTUBE test strings, and to check recipient verification.

Options can come from a config file, from `SWAKS_OPT_name` environment variables, or from the command line, with later sources overriding earlier ones. Reading the printed conversation is a quick way to see what mail servers and clients actually say to each other.

## Install

```
brew install swaks
# Perl tool. TLS needs Net::SSLeay, and MX lookups need Net::DNS (without it, it falls back to localhost).
```

## Try this

```
swaks --help
```
Lists the options, a good map of what parts of an SMTP transaction you can control.

```
swaks --to user@example.com --server test-server.example.net
```
Delivers a standard test email to port 25 of the named server and prints the whole SMTP conversation.

```
swaks --to $E --server test-server.example.com --quit-after RCPT --hide-all
```
Stops the transaction after RCPT, so you learn whether the server accepts the recipient without sending a message. In the docs it runs inside a shell loop over a list of addresses.

## What's unique

It is built around the SMTP transaction rather than a single send, so you can halt at a named protocol step, drive a local MTA over a pipe, and carry your option set around as a config file or inside the script itself.

## Caveats

Maintained by one person as a hobby, so replies may be slow, and TLS and MX lookups depend on optional Perl modules being present.

## Links

- [Project homepage](https://www.jetmore.org/john/code/swaks/)
- [Reference documentation (plain text, latest release)](https://jetmore.org/john/code/swaks/latest/doc/ref.txt)
- [Source on GitHub](https://github.com/jetmore/swaks)
