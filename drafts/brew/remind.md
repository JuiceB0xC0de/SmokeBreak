---
name: remind
title: Remind
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, calendar, old-school, plain-text, scripting-language, unix]
homepage: https://dianne.skoll.ca/projects/remind/
scout_score: 5
status: draft
---

# Remind

**TLDR;** A decades-old command-line calendar and alarm program driven by its own small scripting language for recurring events, holidays and exceptions.

Remind keeps your calendar in plain text files. Each line is a reminder written in Remind's own scripting language, which covers recurring events, exceptions, holidays, and timed alarms. The program reads those files and prints what is due, pops up alarms, or renders whole calendars.

The helper programs take Remind's output and convert it. rem2ps and rem2pdf make printable calendars, rem2html makes HTML, and rem2ics converts to iCalendar. tkremind is an X Window front-end for people who would rather not write the language. The page also lists community front-ends, including a Go curses interface and a pure Bash text UI, plus CalDAV sync. It supports Gregorian and Hebrew calendars and 12 languages.

The author's stated motive is privacy: Remind is, in her words, "an integral part of my effort to avoid storing sensitive data on servers I don't control." She ties this to a De-Googling article about her contacts and calendar. The idea underneath is that a calendar can be a small program plus a text file you own, rather than a service. Rules like "every second Tuesday unless it is a holiday" are expressed as code, not clicked together in a form.

The homepage describes it as a reference-style tool: the man page is a full manual, not a tutorial. The author also has a book, a video, and slides, which I have not seen described beyond their mention.

## Install

```
brew install remind
# tkremind needs an X Window environment. The upstream project is distributed as source (./configure && make && sudo make install); the Homebrew formula avoids that build.
```

## Try this

```
man remind
```
Opens the full Remind manual, the main reference for the scripting language.

```
remind --help
```
Lists the command-line options so you can see what the program can do.

```
rem --help
```
Shows the options for the rem executable installed alongside remind.

## What's unique

Recurring rules, holiday and exception handling, and Hebrew calendar support all live in a plain-text scripting syntax. A large set of converters and front-ends surrounds it, and it is still getting new releases.

## Caveats

Built for UNIX and Linux; the homepage says nothing about macOS or Windows support, and the manual is a dense reference rather than an introduction.

## Links

- [Remind homepage](https://dianne.skoll.ca/projects/remind/)
- [Public git mirror (Debian Salsa)](https://salsa.debian.org/dskoll/remind)
