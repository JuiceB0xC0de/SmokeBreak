---
name: cspice
title: cspice
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, library, math, orbital-mechanics, science, space]
homepage: https://naif.jpl.nasa.gov/naif/toolkit.html
scout_score: 6
status: draft
---

# cspice

**TLDR;** NASA JPL's SPICE toolkit, the library and utilities real space missions use to compute where spacecraft, planets and instruments are and how they relate.

SPICE is built by NASA's NAIF group at JPL to compute observation geometry for space science missions: positions, orientations, clocks and instrument pointing for spacecraft and bodies. The Toolkit is a set of user-level subroutines, a library built from them, and a small collection of ready-built utility programs such as `brief`, `chronos`, `mkspk` and `spkmerge`. The C version is the one this formula packages.

The inputs are ancillary data files called kernels. They describe where things are, how they are oriented, how clocks map to time scales, and what instruments look like. The toolkit reads those files and returns geometry and time results. The brief does not detail the kernel format or what each utility reads and writes, so the utilities' own User's Guides are the place to start.

The idea underneath is that mission geometry is data plus a shared, well-tested library, not bespoke code per project. The same software that serves flight projects can be run by anyone, and the documentation is organised as tutorials, lessons and technical references per functional area. That makes it a real door into orbital mechanics, time systems and reference frames.

## Install

```
brew install cspice
# The official NAIF packages are source code to build, and the homepage points to its tutorials '07_installing toolkit' and '11_preparing_for_programming'. The brew-level steps were not confirmed from the pages. You will also need kernel data files from NAIF to do anything useful.
```

## Try this

```
brief --help
```
Shows usage for the utility that summarises the contents of kernel files.

```
chronos --help
```
Shows usage for the time conversion utility.

```
spkmerge --help
```
Shows usage for the tool that merges ephemeris kernel files.

## What's unique

It is mission-grade geometry software used by real flight projects, and a hobbyist can run it at home. It comes with tutorials and per-area technical references.

## Caveats

Official packages are source code, NAIF warns against porting to unsupported environments because of numeric and optimization problems, and the utilities need kernel files you have to fetch separately.

## Links

- [SPICE Toolkit homepage](https://naif.jpl.nasa.gov/naif/toolkit.html)
- [About SPICE](https://naif.jpl.nasa.gov/naif/aboutspice.html)
