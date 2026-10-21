---
name: gnu-units
title: GNU Units
source: brew
category: languages-and-oddities
commitment: quick
tags: [calculator, cli, math, quick, units]
homepage: https://www.gnu.org/software/units/
scout_score: 5
status: draft
---

# GNU Units

**TLDR;** A unit converter that treats units as algebra, tracking dimensions through whole expressions, with a big editable text file of odd units and constants behind it.

GNU Units converts a quantity in one system of measurement to another. Give it a quantity such as a mile and a target unit, and it prints the multiplier in both directions. It also handles conversions a plain multiplier cannot, such as Fahrenheit to Celsius and wire gauge, and it accepts sums of units like feet plus inches.

Underneath, it is a small calculator that keeps track of units through sums, products, quotients, powers and roots. Expressions are checked for dimensional consistency as they are evaluated, so mixed units do not silently go wrong in a long calculation. That is the idea worth taking away: units are a type system for physical quantities, and a tool can enforce it.

The vocabulary is not hard-coded. Units are defined in an external text data file that ships with the program (the README says the definitions are generally found in /usr/share/units/). You can read it, add your own definitions, or supply a whole different file. Browsing that file is a good way to find out which strange units and constants someone thought worth writing down.

## Install

```
brew install gnu-units
# Homebrew installs the commands with a g prefix (gunits, gunits_cur). For the plain name `units`, add to your shell rc:
# PATH="$HOMEBREW_PREFIX/opt/gnu-units/libexec/gnubin:$PATH"
```

## Try this

```
gunits --help
```
Prints a brief summary of usage.

```
man units
```
Opens the manual page. It may only resolve to the GNU one if you have put gnubin on your PATH.

```
info units
```
Opens the full manual, the documentation route the project names.

## What's unique

Most converters are lookup tables with a multiplier. This one does dimensional arithmetic, accepts sums like 17 yards + 2 feet + 5 inches, and can print results as sums too.

## Caveats

The homepage gives no version or release date, and under Homebrew the commands are installed as gunits unless you change your PATH.

## Links

- [GNU Units homepage](https://www.gnu.org/software/units/)
- [Source distribution (GNU FTP)](http://ftp.gnu.org/gnu/units/)
- [Windows binary (GNU FTP)](http://ftp.gnu.org/gnu/units/windows/)
