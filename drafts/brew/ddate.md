---
name: ddate
title: ddate
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [c, calendar, discordian, oddity, quick]
homepage: https://github.com/bo0ts/ddate
scout_score: 6
status: draft
---

# ddate

**TLDR;** A tiny C program that converts today's date into the Discordian calendar, with five seasons, odd weekday names and a leap day for Saint Tib.

ddate is a perpetual date converter from the Gregorian calendar to the Discordian one, which the README calls the POEE calendar. Run it and you get the date in a calendar from Discordian tradition: five seasons of 73 days each, named Chaos, Discord, Confusion, Bureaucracy and The Aftermath. The weekdays are Sweetmorn, Boomtime, Pungenday, Prickle-Prickle and Setting Orange.

The calendar has its own holidays. The 5th day of each season is an apostle holyday and the 50th is a season holyday. Every four years Saint Tib's Day is inserted between the 59th and 60th days of Chaos, a leap-day rule the README sums up as '1 + 4 = 5'. The README includes a large table mapping Gregorian dates to Discordian ones.

The code is the ddate source from util-linux 2.20, kept in its own repository because util-linux no longer builds ddate by default. The README says it is exactly that version. It is a single C file built with CMake, so it is effectively frozen.

The underlying idea is that a calendar is just a mapping from a day count to names and rules, and you can swap one for another with a small amount of arithmetic. ddate is a joke calendar, but it is a compact example of that mapping, with seasons, leap days and named holidays in about one source file.

## Install

```
brew install ddate
```

## Try this

```
ddate --help
```
Prints the usage text so you can see which options and date arguments this build accepts.

## What's unique

It is a whole fictional calendar system packed into one small C program, rescued from util-linux and kept alive on its own.

## Caveats

The code is frozen at the util-linux 2.20 version, and the README does not show example input or output, so expect to rely on the help text.

## Links

- [GitHub repository (homepage)](https://github.com/bo0ts/ddate)
