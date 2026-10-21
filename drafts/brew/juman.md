---
name: juman
title: JUMAN
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, japanese, linguistics, nlp, tokenizer]
homepage: https://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN
scout_score: 6
status: draft
---

# JUMAN

**TLDR;** A Japanese morphological analyser from Kyoto University that splits text into words and tags each with reading, base form and part of speech, even for slangy spellings.

JUMAN reads Japanese text from stdin (UTF-8 since version 7.0) and prints one morpheme per line. Each line carries the surface form, its reading, the dictionary base form, part of speech and conjugation info. An `EOS` line closes each sentence. Japanese has no spaces between words, so this segmentation step is the first thing almost any computational work on the language needs.

The homepage says it was built so that many researchers studying computational analysis of Japanese could share one common tool. It also says school grammar suits computers poorly, so the grammar definitions and the connection rules between words are meant to be easy for the user to change. The repository tree includes `makemat` (connectivity rules), `makeint` (dictionary conversion) and `makepat` (a Patricia database), which hints at dictionary lookup combined with connection-rule scoring. The pages read for this entry do not describe the segmentation algorithm, so treat that as a guess.

The homepage sample shows the fun part: informal spellings such as ビミョーだ, ありがとー and 行きたぁぁぁい. Version 7.0 added automatic recognition of onomatopoeia, long-vowel marks and small kana, and some dictionary entries are auto-acquired from web text and Wikipedia. Output tags like 自動獲得:Wikipedia show up in the sample.

The door here is how a machine decides where one word ends and the next begins in a language with no word boundaries, and how much of that is linguistics you can edit rather than code.

## Install

```
brew install juman
```

## Try this

```
juman --help
```
Prints the available options for the analyser.

```
juman < sample.txt
```
Analyses your own UTF-8 Japanese text file, printing one token per line with reading, base form and part of speech, and EOS after each sentence.

## What's unique

The grammar and word-connection rules are designed to be edited by the user instead of being locked to a fixed school-grammar tagset. Version 7.0 also handles colloquial long-vowel and small-kana spellings.

## Caveats

The latest release noted on the homepage is 7.01 from December 2014, the homepage is in Japanese, and the GitHub README is thin and points to a PDF manual.

## Links

- [JUMAN homepage (Kyoto University NLP lab)](https://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN)
- [JUMAN GitHub repository (ku-nlp/juman)](https://github.com/ku-nlp/juman)
