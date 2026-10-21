---
name: erlang@27
title: Erlang/OTP 27
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [actors, afternoon, concurrency, functional, language, runtime]
homepage: https://www.erlang.org/
scout_score: 5
status: draft
---

# Erlang/OTP 27

**TLDR;** A functional language and runtime built around tiny isolated processes that talk by message, made for systems that must keep running.

Erlang is a programming language, its runtime, and OTP, a set of libraries and design principles for building services. The runtime has concurrency, distribution and fault tolerance built in. You write functional code with pattern matching and recursion, try it in an interactive shell, and spawn lightweight processes that share nothing and communicate only by sending and receiving messages.

The homepage says it is used in telecoms, banking, e-commerce, computer telephony and instant messaging, places where systems must stay up while handling huge numbers of concurrent activities. Its own line is "Practical functional programming for a parallel world". It describes the target as soft real-time, not hard real-time.

The idea underneath is that concurrency is the basic building block, not a library bolted on. On the homepage, a child process is created with spawn, sent a message with `Child ! go`, and handles it in a receive block. One example runs a parallel map-reduce by spawning a process per number and collecting the replies. OTP then builds on that with tooling for releases, debugging, and a distributed database.

This formula is the OTP 27 line. The homepage is pitched at OTP 29, so this is an older release series, which is fine for poking at the language but not the newest.

## Install

```
brew install erlang@27
# Man pages: erl -man, or add $HOMEBREW_PREFIX/opt/erlang@27/lib/erlang/man to MANPATH.
# Pulls in openssl, unixodbc and wxwidgets as dependencies.
```

## Try this

```
erl
```
Starts the interactive Erlang shell, where you can type expressions and define and run code.

```
> example:fact(10).
```
In the shell, calls a factorial function from the homepage's example module and prints 3628800. You need to compile that module first.

```
> Child ! go.
```
Sends the atom go as a message to a spawned child process, as in the homepage's process example.

## What's unique

Isolated lightweight processes that only exchange messages are the core of the language, not an add-on. OTP turns that into a toolkit for building fault-tolerant services.

## Caveats

This package is the older OTP 27 line while the site promotes 29.x, and the homepage is marketing-oriented, so expect to find deeper documentation elsewhere.

## Links

- [Erlang/OTP homepage](https://www.erlang.org/)
- [Downloads and install options](https://www.erlang.org/downloads)
