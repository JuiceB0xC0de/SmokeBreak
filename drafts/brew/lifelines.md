---
name: lifelines
title: LifeLines
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, curses, gedcom, genealogy, scripting, tui]
homepage: https://lifelines.github.io/lifelines/
scout_score: 6
status: draft
---

# LifeLines

**TLDR;** A 1990s terminal genealogy program with its own database and a scripting language that turns family trees into LaTeX books and PostScript charts.

LifeLines is a genealogy program that runs in a terminal. The main program, llines, is a curses-style interface for browsing and editing people and families. Data goes in as a GEDCOM file exported from other genealogy software, and is stored in LifeLines' own B-tree style database.

The homepage puts the draw plainly: "IMHO, the real power of lifelines is its scripting ability." Report scripts run against the database and produce ahnentafels, ancestor and descendant reports, groff and LaTeX books, and PostScript charts. llexec runs those reports non-interactively, so a family tree can feed a print pipeline.

Tom Wetmore wrote it circa 1991-1994 as a GEDCOM-driven tool. He has since released it under an MIT-style license and no longer works on it; the open source community maintains it now. That makes it a working look at how a genealogy tool was built before web apps: a data file format, a database, and a small language for asking questions of it.

The kit also ships dbverify to check a database and btedit to repair one. The project warns that btedit is only for use under the guidance of a LifeLines developer.

## Install

```
brew install lifelines
# needs a terminal with wide-character curses support; you will want a GEDCOM file to import
```

## Try this

```
llines --help
```
Lists the options for the interactive curses program, the place to start before creating or opening a database.

```
llexec --help
```
Shows how to run a report script non-interactively against a database.

```
dbverify --help
```
Shows the options for checking a LifeLines database for problems.

## What's unique

A 1990s genealogy program that is still maintained, with a scripting system that builds print-quality output like LaTeX books and PostScript charts, all from inside a terminal.

## Caveats

The original website and FTP repository are dead, the author has stepped away, recency of the latest release is unconfirmed, and you need your own GEDCOM data to get much out of it.

## Links

- [Homepage](https://lifelines.github.io/lifelines/)
- [Source code (GitHub)](https://github.com/lifelines/lifelines)
- [Install notes (INSTALL file)](https://github.com/lifelines/lifelines/blob/master/INSTALL)
- [LINES-L archives](http://listserv.nodak.edu/archives/lines-l.html)
