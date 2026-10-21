---
name: grex
title: grex
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [automata, cli, quick, regex, rust]
homepage: https://pemistahl.github.io/grex-js/
scout_score: 6
status: draft
---

# grex

**TLDR;** Give grex example strings and it prints one regular expression that matches exactly those strings, turning the usual regex workflow upside down.

grex takes the strings you want to match and returns a single regular expression. Run `grex a b c` and it prints `^[a-c]$`. The output is anchored with ^ and $, so by default it matches only the inputs you gave it and nothing else. Generalizing is opt-in: flags such as `-d`, `-w` and `-r` swap literal text for digit classes, word classes and repetition quantifiers.

The author calls writing regexes by hand an "often complicated and tedious task" and wants grex to produce a correct starting point. The project began as a Rust port of regexgen, a JavaScript tool by Devon Govett whose development had apparently ceased. The Homebrew package is the Rust command-line tool. The homepage is a demo site for grex-js, a WebAssembly build of the same library.

The interesting part is how it gets there. grex builds a deterministic finite automaton from your strings and shrinks it with Hopcroft's minimization algorithm. It then treats the minimized automaton as a system of linear equations and solves it with Brzozowski's algebraic method, and the solution is the regex. This is the formal-language link between automata and regular expressions, running as a practical tool.

The README says the result aims to be short but is often longer than needed. Treat the output as a draft to edit. The README's own answer to whether you still need to learn regexes is: "Definitely, yes!"

## Install

```
brew install grex
```

## Try this

```
grex a b c
```
Prints ^[a-c]$, a character class built from three single-letter examples.

```
grex -r b ba baa baaa
```
Prints ^b(?:a{1,3})?$, with the repeated a's collapsed into a {1,3} quantifier.

```
grex "I ♥ cake" "I ♥ cookies"
```
Prints ^I ♥ c(?:ookies|ake)$, factoring out the shared prefix and keeping the differing endings as alternatives.

## What's unique

It inverts regex writing: you supply the strings that must match and get a pattern back. The default is the most specific pattern possible, and you loosen it with flags.

## Caveats

Output targets PCRE and the Rust regex crate and only partly matches JavaScript RegExp, and turning on \w or \d conversion makes the pattern match much more than your inputs.

## Links

- [Demo website (homepage)](https://pemistahl.github.io/grex-js/)
- [grex CLI and Rust library source](https://github.com/pemistahl/grex)
- [grex-js source and README](https://github.com/pemistahl/grex-js)
