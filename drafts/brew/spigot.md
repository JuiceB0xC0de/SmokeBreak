---
name: spigot
title: spigot
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [calculator, exact-arithmetic, math, pi, quick]
homepage: https://www.chiark.greenend.org.uk/~sgtatham/spigot/
scout_score: 8
status: draft
---

# spigot

**TLDR;** A command-line calculator by Simon Tatham that prints digits of pi, e and other expressions one at a time, never rounding wrongly, until you stop it.

spigot takes a mathematical expression and prints the digits of the result as a stream. It keeps going until you interrupt it. It can also read numbers from a file or a pipe, and it starts producing output as soon as it has read enough input to know how the answer begins.

The usual problem with calculators is that they work to a fixed precision, and rounding errors pile up across successive operations, so the last digits can be wrong. spigot's author describes the opposite approach: "spigot, by contrast, does not output any digit of the answer until it's sure that the digit is right, and it will keep generating digits until you tell it to stop." That makes it useful when you need very many digits, or want a cross-check on other calculating systems.

The name comes from the core algorithm: "Jeremy Gibbons's unbounded spigot algorithm for the digits of \u03c0", which spigot extends to more output modes and many more input numbers. The idea underneath is exact real arithmetic, where a number is treated as a process that can be asked for more digits rather than as a fixed-size value. That is a door into a corner of computable analysis most programmers never see.

## Install

```
brew install spigot
```

## Try this

```
spigot --help
```
Lists the options and the kinds of expression spigot accepts, a safe first look before you try anything.

## What's unique

Most calculators hand back a fixed-precision answer with silent rounding error. spigot promises every digit it prints is correct and keeps streaming without a preset limit.

## Caveats

The homepage says spigot is very slow compared to ordinary computer arithmetic, which is the price of never printing a wrong digit.

## Links

- [spigot homepage](https://www.chiark.greenend.org.uk/~sgtatham/spigot/)
- [development git repository](https://git.tartarus.org/simon/spigot.git)
