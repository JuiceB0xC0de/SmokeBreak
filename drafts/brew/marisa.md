---
name: marisa
title: marisa
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c++, compression, data-structures, library, trie]
homepage: https://github.com/s-yata/marisa-trie
scout_score: 5
status: draft
---

# marisa

**TLDR;** A static trie that squeezes millions of strings into a fraction of the usual space, with command-line tools for building and querying dictionaries.

MARISA, short for Matching Algorithm with Recursively Implemented StorAge, is a C++ library (libmarisa) for a static trie. You build a dictionary once from a set of keys, then query it. The package also installs seven command-line tools: `marisa-build`, `marisa-lookup`, `marisa-reverse-lookup`, `marisa-common-prefix-search`, `marisa-predictive-search`, `marisa-dump` and `marisa-benchmark`.

A dictionary answers four kinds of question. Is this string a key? Which key has this ID? Which keys are prefixes of this string? Which keys start with this string? That covers the core of autocomplete, spell-check dictionaries and word segmentation, which is why tries like this show up inside search and language software.

The author's stated advantage is size. The README benchmark uses all English Wikipedia page titles, about 9.8 million keys and 200 MB as plain text. It reports 50.8 MB for marisa-trie, against 376.6 MB for darts-clone and 127.7 MB for tx-trie. In the README's words: "The biggest advantage of libmarisa is that its dictionary size is considerably more compact than others."

The README says little about the mechanism beyond the name, which hints at a trie whose storage is itself built recursively. The detail is in the linked docs. That makes it a good door into succinct data structures: trading some query speed and the ability to update for a much smaller footprint.

## Install

```
The README does not mention Homebrew, but the formula exists: `brew install marisa`

To build from source instead, you need CMake and a C++ compiler:
git clone https://github.com/s-yata/marisa-trie.git
cd marisa-trie
cmake -S. -Bbuild-rel -DCMAKE_BUILD_TYPE=Release -DENABLE_NATIVE_CODE=ON -DBUILD_TESTING=OFF
cmake --build build-rel
sudo cmake --install build-rel
```

## Try this

```
marisa-build --help
```
Shows how to build a dictionary from a list of keys.

```
marisa-lookup --help
```
Shows how to check whether strings are keys in a built dictionary.

```
marisa-predictive-search --help
```
Shows how to find all keys that start with a given prefix.

## What's unique

Compared with double-array and LOUDS tries, it aims for a much smaller footprint while still supporting reverse lookup and both prefix-style searches.

## Caveats

The trie is static, so there are no incremental updates, and the size comparison is self-reported by the author on a single 2012 dataset; the library is the main artifact and the CLI tools are secondary.

## Links

- [Homepage / repository](https://github.com/s-yata/marisa-trie)
- [README (English)](https://www.s-yata.jp/marisa-trie/docs/readme.en.html)
- [README (Japanese)](https://www.s-yata.jp/marisa-trie/docs/readme.ja.html)
