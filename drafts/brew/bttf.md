---
name: bttf
title: bttf
source: brew
category: languages-and-oddities
commitment: quick
tags: [datetime, quick, rust, text-filter, unix-pipes]
homepage: https://github.com/BurntSushi/bttf
scout_score: 5
status: draft
---

# bttf

**TLDR;** A Rust datetime tool that formats, shifts and converts times, and can find timestamps in any text and rewrite them in place.

bttf is a command-line datetime tool by BurntSushi, originally named Biff. Its subcommands cover formatting (`time fmt`), calendar-aware arithmetic (`time add`, which accepts inputs like `6mo` or `1 week, 12 hours ago`), time zone conversion (`time in`), rounding, sorting, spans between dates (`span since`), and sequences of dates. It reads datetimes from arguments or stdin, so the pieces chain together in a pipe.

The author built it mainly to expose the Jiff datetime library on the command line. He says the Unix `date` command is odd enough that he keeps re-reading its manual, and he wanted something more succinct. Nearly all the date logic is delegated to Jiff, with localization via ICU4X. The exception named in the README is bttf's own RFC 5545 implementation, used for recurrence rules in `time seq`. That is how a one-liner can produce the second Tuesday of every month.

The idea underneath is the `tag` command. It finds datetimes inside arbitrary text, such as a log file or git output, and wraps them as JSON lines. Anything downstream can then convert or reformat the timestamps, and `untag` turns the result back into plain text with the surrounding text intact. In the author's words: "It's unclear to me how broadly useful folks will find this functionality, but other datetime utilities don't seem to have it."

## Install

```
brew install bttf
```

## Try this

```
bttf time in Asia/Bangkok now | bttf time round -i 15 -s minute
```
Converts the current time to Bangkok, then rounds it to the nearest 15 minutes.

```
bttf time seq monthly -w 2-tue --until $(bttf time end-of year now) | bttf time fmt -f '%a, %F'
```
Lists the second Tuesday of each month until the end of the year, formatted as weekday and date.

```
bttf tag lines /tmp/access.log | bttf time in system | bttf time fmt -f '%c' | head -n3 | bttf untag -s
```
Finds timestamps in a log file, converts them to your time zone, reformats them in place, and strips the tags.

## What's unique

The `tag` and `untag` pair turns a date calculator into a filter that rewrites timestamps inside arbitrary text. It also does calendar-rule recurrence such as the second Tuesday of each month in a shell one-liner.

## Caveats

The README says it is not a drop-in replacement for `date`, and warns the author may ship "arbitrary and capricious breaking changes"; locale output only works if BTTF_LOCALE is set.

## Links

- [Homepage (GitHub repository)](https://github.com/BurntSushi/bttf)
- [User guide (GUIDE.md)](https://github.com/BurntSushi/bttf/blob/master/GUIDE.md)
- [Comparison with similar tools (COMPARISON.md)](https://github.com/BurntSushi/bttf/blob/master/COMPARISON.md)
