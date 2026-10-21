---
name: calc
title: calc
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, arbitrary-precision, language, math, primes, quick]
homepage: http://www.isthe.com/chongo/tech/comp/calc/
scout_score: 6
status: draft
---

# calc

**TLDR;** An arbitrary-precision calculator with its own C-like language, exact fractions, and a lineage tied to hunting huge prime numbers.

Calc is an interactive calculator that does not run out of digits. Type an expression and it prints the result. Values are stored as fractions with arbitrarily large numerators and denominators, reduced to lowest terms, so there is no floating-point rounding hiding in the middle. It also handles complex numbers, transcendental functions, and output as fractions, hex, octal, or binary. You can pass a single command as an argument and it will run it and exit.

Under the calculator is a programming language. Each input line is treated as the body of a procedure in a C-like syntax, so a line can hold declarations, conditionals, labels, and loops. Every expression that is not an assignment is printed automatically. Functions can be written C-style with `define`, or with an `=` shorthand. Variables are untyped and can be global, local, or static. The README includes a `help unexpected` page for C programmers, because the language looks like C but does not always behave like it.

The homepage says the authors wrote it "because they wanted to write it, because it was fun writing it, and because we wanted you to use and enjoy it." It also has a mathematical pedigree: the bundled `lucas.cal` script holds methods used to find a very large prime, and the homepage links a tutorial on finding new largest known primes. That makes it a small door into number theory, where big exact integers are the whole point.

## Install

```
brew install calc
```

## Try this

```
calc
```
Starts interactive mode, where each line you type is evaluated and its result printed.

```
3 * 19^43 - 1
```
Typed inside calc, it does large-integer arithmetic and prints a 56-digit result.

```
define sc(a,b) = a^3 + b^3
```
Defines a one-line function inside calc; sc(31, 61) then returns 256772.

## What's unique

It pairs exact fraction arithmetic with a full C-like language, and ships with scripts descended from real large-prime searches.

## Caveats

Very old systems may fail to build the master branch, which needs a C17 compiler, and the v3 branch is labeled experimental.

## Links

- [Homepage (Landon Curt Noll)](http://www.isthe.com/chongo/tech/comp/calc/)
- [GitHub repository](https://github.com/lcn2/calc)
- [calc v3 discussion](https://github.com/lcn2/calc/issues/103)
