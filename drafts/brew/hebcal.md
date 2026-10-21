---
name: hebcal
title: hebcal
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [astronomy, calendar, cli, dates, quick]
homepage: https://hebcal.github.io/
scout_score: 5
status: draft
---

# hebcal

**TLDR;** A command-line Jewish calendar that prints holidays, Hebrew dates, Torah portions, candle-lighting times and daily study cycles for any Gregorian year.

Hebcal prints the days of the Jewish calendar for a given secular year, month or date. You choose what to show: the Hebrew date, holidays, the weekly sedra, the days of the Omer, and more. Add a location and it can also give candle-lighting, havdalah, fast times, sunrise and sunset. Output is plain text, tab-delimited, or ISO dates, so it is easy to feed into other tools.

The author describes it as a perpetual Jewish calendar for the command line, originally meant for generating calendars for PDAs and personal calendars. The README says the original motivation for the algorithms was the Tur Shulchan Aruch. The key routines began as translations of Dershowitz and Reingold's calendar code for GNU Emacs. Candle-lighting times were later rewritten using Derick Rethans's timelib, and version 5 was ported from C to Go.

The idea underneath is that the Jewish calendar is lunisolar. Months follow the moon, years are kept in step with the sun, and a holiday's date has to be computed rather than looked up. Add the 1752 Julian-to-Gregorian switchover, which the program handles explicitly, and a calendar turns into a small, real calendrical-calculation problem. Reading the output next to the source algorithms is a good way into that world.

It also carries many daily learning cycles, such as Daf Yomi, Mishna Yomi, 929, Rambam and Psalms, so the same tool doubles as a study schedule generator.

## Install

```
brew install hebcal
```

## Try this

```
hebcal 10 1992
```
Prints the holidays in October 1992, the README's own usage example.

```
hebcal -ch --geo 44.0181,-88.6353 -z America/Chicago
```
Prints candle-lighting times for the current year at explicit coordinates and timezone (Oshkosh, Wisconsin).

```
hebcal info
```
Shows the version number and current default settings, including the default city.

## What's unique

A small, old-school program with a very large option set, covering many learning cycles and sunrise/sunset times from a single command. It is open about where its calculations are approximate.

## Caveats

The author calls candle-lighting and sunrise/sunset times approximations, guaranteed wrong above the arctic or below the antarctic circle, and says the tool should not be given any halachic authority.

## Links

- [Hebcal homepage](https://hebcal.github.io/)
- [GitHub repository (source, README, releases)](https://github.com/hebcal/hebcal)
- [Slackbuild for Slackware](https://slackbuilds.org/repository/15.0/office/hebcal/?search=hebcal)
