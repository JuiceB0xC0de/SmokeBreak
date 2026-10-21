---
name: urweb
title: Ur/Web
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, language, sql, types, web]
homepage: http://www.impredicative.com/ur/
scout_score: 7
status: draft
---

# Ur/Web

**TLDR;** A statically typed functional language for web apps where the type system rules out injection, invalid HTML, dead links and bad SQL.

Ur/Web is a domain-specific language for web applications backed by SQL databases. Ur itself is pure, strict and statically typed, in the ML and Haskell tradition, but with what the README calls "a significantly richer type system". Ur/Web adds a standard library and compiler rules for web and SQL work. The compiler takes Ur/Web source and produces a standalone web server executable, plus JavaScript for the client-side code, so one language covers both sides.

The point is to make well-typed programs "not go wrong" in a broad sense. The README lists what the types are meant to rule out: code injection, invalid HTML, dead intra-application links, mismatches between forms and their handlers, invalid SQL, and improper marshaling between browser, server and database. The standard library's signatures are designed so that these mistakes fail to type-check instead of failing in production.

The larger idea is row types and type-level metaprogramming. Because a table's columns can be described in the type system, code can be written once and applied to any table. The README's example is a demo with an ML-style functor that builds an admin interface for an arbitrary SQL table, with its safety following from the types. The compiler also emits object code that does not use garbage collection, and the README says the demo server uses less RAM than the bash shell.

## Install

```
brew install urweb
```

## Try this

```
urweb demo/hello
```
Compiles the bundled Hello demo into a standalone server executable.

```
demo/hello.exe &
```
Starts the compiled server in the background.

```
wget http://localhost:8080/Hello/main -O -
```
Fetches the Hello app's main page from the local server and prints it.

## What's unique

Few languages try to make web-app safety a property of type signatures across HTML, SQL, links and forms all at once. The same language also compiles to a GC-free native server and to client-side JavaScript.

## Caveats

It is niche with a steep learning curve, and the brief could not confirm how actively it is maintained; the README's CI badge points to a retired domain.

## Links

- [Ur/Web project homepage](http://www.impredicative.com/ur/)
- [GitHub repository (source and README)](https://github.com/urweb/urweb)
- [Reference manual (PDF)](http://www.impredicative.com/ur/manual.pdf)
