---
name: hashcash
title: hashcash
source: brew
category: fundamentals
commitment: quick
tags: [hashing, math, proof-of-work, protocol, quick, spam]
homepage: http://hashcash.org
scout_score: 6
status: draft
---

# hashcash

**TLDR;** A 1997 proof-of-work stamp: burn some CPU to mint it, check it with one hash. The idea behind Bitcoin mining, in its original small form.

Hashcash makes a sender do a tunable amount of computing before an action, such as sending an email. The input is a piece of text. The output is a stamp showing that someone searched for a value whose hash starts with a chosen number of zero bits. The homepage calls it "payment in burnt CPU cycles by calculating n-bit partial hash collisions on chosen texts."

The asymmetry is the point. Finding the stamp takes guesswork, and each extra bit of difficulty doubles the average effort. Checking it takes a single hash. The cypherspace page gives an example: a 20-bit collision takes about 6 seconds on a machine testing 180,000 hashes per second. For one email that is nothing. For a spammer sending millions it adds up.

The project was proposed as a denial-of-service counter-measure that costs honest users little and needs no central party or identity, so it preserves privacy. The homepage describes it as a stop-gap until electronic cash is widely used. It also notes that the proof-of-work idea is now best known through Bitcoin mining, which is how most people meet it today.

The verification is simple enough to do by hand. The homepage says it can be done "by a human eye (count leading 0s)" with ordinary tools like sha1sum. That makes it a good first look at hash-based puzzles, difficulty tuning, and why cost-based defences work.

## Install

```
brew install hashcash
```

## Try this

```
hashcash --help
```
Prints the tool's options, which is the quickest way to see how stamps are minted and checked.

```
sha1 --help
```
Shows the usage of the bundled sha1 executable. The brief does not document it, so expect a small hashing helper.

## What's unique

The scheme is tiny and checkable by eye, and it came years before Bitcoin made proof-of-work famous. You can reimplement it from scratch in a few lines.

## Caveats

The documentation dates from about 2002 to 2003, shows no recent activity, and gives no command examples, so you will be reading --help and experimenting.

## Links

- [Homepage (hashcash.org)](http://hashcash.org)
- [Original hashcash page with binaries, source, and related work (cypherspace.org)](http://www.cypherspace.org/hashcash/)
