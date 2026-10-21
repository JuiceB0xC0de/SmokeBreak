---
name: nkf
title: nkf
source: brew
category: languages-and-oddities
commitment: quick
tags: [encoding, history, japanese, quick, unix-filter]
homepage: https://github.com/nurse/nkf
scout_score: 5
status: draft
---

# nkf

**TLDR;** A small Unix filter that converts Japanese text between encodings like Shift_JIS, EUC-JP, ISO-2022-JP and UTF-8, and guesses the input encoding so you never have to declare it.

nkf, the Network Kanji Filter, reads text from files or standard input and writes it back out in the encoding you choose: ISO-2022-JP, Shift_JIS, EUC-JP, UTF-8, UTF-16 or UTF-32. It also converts line endings, swaps half-width and full-width kana and alphabet forms, and decodes or encodes MIME, base64, quoted-printable, URL, hex and HTML numeric character references.

It exists because Japanese text was long stored in several incompatible encodings, and networks, hosts and terminals each preferred a different one. The README calls it "a yet another kanji code converter among networks, hosts and terminals." The history goes back to a 1987 Fujitsu original, later extended by The nkf Project.

The idea underneath is detection. In the README's words, "One of the most unique faculty of nkf is the guess of the input kanji encodings." It recognises ISO-2022-JP, Shift_JIS, EUC-JP, UTF-8, UTF-16 and UTF-32, "so users needn't set the input kanji code explicitly." That makes it a good way into why Japanese text has so many encodings, and why guessing among them is a real problem.

The defaults reflect that history. Half-width katakana (X0201) is converted to full-width (X0208) by default, and detection assumes Shift_JIS input has no half-width kana unless you pass -X, -x or -S.

## Install

```
brew install nkf
```

## Try this

```
nkf --guess yourfile.txt
```
Prints the encoding and newline type nkf guesses for the file. Use --guess=1 to print only the encoding.

```
nkf -h1 yourfile.txt
```
Converts katakana to hiragana and writes the result to standard output.

```
nkf --help
```
Lists the options, which are numerous and mostly single letters.

## What's unique

It guesses the input encoding across several Japanese encodings and Unicode forms, so you only say what you want out. It is a single-purpose Unix filter with a lineage back to 1987.

## Caveats

The README has no release date or version, and its copyright line runs only to 2012, so how actively it is maintained is unclear; --in-place also overwrites your original files.

## Links

- [Homepage and README (GitHub)](https://github.com/nurse/nkf)
