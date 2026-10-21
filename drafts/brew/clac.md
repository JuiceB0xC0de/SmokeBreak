---
name: clac
title: clac
source: brew
category: languages-and-oddities
commitment: quick
tags: [calculator, forth, postfix, quick, rpn, stack]
homepage: https://github.com/soveran/clac
scout_score: 5
status: draft
---

# clac

**TLDR;** A postfix stack calculator that redraws the whole stack on every keystroke, so you watch Forth-style arithmetic happen instead of just getting an answer.

clac is a command-line calculator built on a stack and postfix (reverse Polish) notation. Numbers push onto the stack. Each operator pops the arguments it needs and pushes the result. Because of that, there are no parentheses and no precedence rules. The operations include arithmetic, modulo, exponentiation, logs, trig, erf, factorial, rounding, bitwise and/or/xor, stack manipulation and a stash.

In interactive mode the stack is always on screen and updates as you type each key. You can also pass an expression as an argument. It then prints the resulting stack, one value per line, top first.

The author likes Forth and other stack-based concatenative languages, and has used `dc` a lot. He found other calculators less capable than dc and dc's interface lacking. In his words: "That's why I decided to try this idea of an always-visible stack with realtime updates."

The idea underneath is concatenative programming: a program is a sequence of words that each transform a stack. You can define your own words as plain aliases in a words file. That file is not created by default. Once you have used it for a few minutes, Forth and dc make a lot more sense.

## Install

```
brew install clac
# Optional: define your own words in $CLAC_WORDS, $XDG_CONFIG_HOME/clac/words, or $HOME/.config/clac/words (not created by default)
```

## Try this

```
clac "3 4 +"
```
Pushes 3 and 4, adds them, and prints 7.

```
clac "2 3 4 +"
```
Prints 7 then 2, showing the leftover stack with the top first.

```
clac "1 2 3 4 count . sum , /"
```
Uses the stash to compute the average of the stack and prints 2.5.

## What's unique

The stack is the interface rather than a hidden detail, redrawn on every keystroke. Words are simple aliases in a plain text file, which gives this small tool a Forth-like feel.

## Caveats

The README gives no release dates or maintenance status. Subtraction and division take the second item from the top as the left operand, which can surprise you at first.

## Links

- [Homepage / GitHub repository](https://github.com/soveran/clac)
- [Releases](https://github.com/soveran/clac/releases)
- [Distribution packages (wiki)](https://github.com/soveran/clac/wiki/Distribution-Packages)
- [Demo animation (GIF)](http://files.soveran.com/misc/clac.gif)
