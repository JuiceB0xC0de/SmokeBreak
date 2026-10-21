---
name: dnstwist
title: dnstwist
source: brew
category: fundamentals
commitment: quick
tags: [dns, phishing, python, quick, security, unicode]
homepage: https://dnstwist.it
scout_score: 5
status: draft
---

# dnstwist

**TLDR;** Give it a domain and it generates lookalike typo and homoglyph variants, then checks which ones are actually registered and what they serve.

dnstwist takes a domain name and runs it through a set of fuzzing algorithms: homoglyphs, hyphenation, and others. It can also add words from a dictionary file. Each permutation is then resolved over DNS to see whether someone has registered it, and the records come back in the terminal, as CSV, or as JSON. A passive mode skips the lookups and just prints the permutations.

The README frames the purpose as seeing "what sort of trouble users can get in trying to type your domain name". It is built for defenders, such as SOC and incident response teams, who want to find lookalike domains before an attacker uses them. The homoglyph fuzzer draws on Unicode characters that can actually be registered, so the list reflects what an attacker could really buy.

Two optional modes go past DNS. With `--lsh`, it fetches each live page, normalizes the HTML, and compares a fuzzy hash against the original site, reporting a similarity percentage. With `--phash`, it takes headless Chromium screenshots and compares perceptual hashes. Both are attempts to tell a parked domain from a copied login page.

Underneath is a good way into how DNS, internationalized domain names, and phishing infrastructure fit together. You see how easily one name fans out into hundreds of near-neighbors, and how few of them need to resolve to cause trouble. It also works as a Python library through `dnstwist.run()`, which returns a list of dictionaries.

## Install

```
brew install dnstwist
# Optional: --phash needs Chromium installed; GeoIP needs a MaxMind-style database with its path in $GEOLITE2_MMDB
```

## Try this

```
dnstwist --format list example.com
```
Prints the bare permutations with no DNS lookups, so you can see what the fuzzers produce without touching anyone's servers.

```
dnstwist --registered example.com
```
Runs the fuzzers, resolves each variant, and shows only the ones that are registered.

```
dnstwist --fuzzers "homoglyph,hyphenation" example.com
```
Limits generation to the named algorithms, which makes it easy to compare what each one contributes.

## What's unique

Most lookalike-domain tools stop at listing permutations. This one also fetches the live pages and compares fuzzy HTML hashes and screenshot perceptual hashes against the original site.

## Caveats

Large runs can overwhelm your DNS resolver, so the README advises a fast external one, and `--phash` needs a full Chromium install and a lot of memory.

## Links

- [Homepage (web scanner)](https://dnstwist.it)
- [Source code (GitHub)](https://github.com/elceef/dnstwist)
- [README with full usage notes](https://github.com/elceef/dnstwist/blob/master/docs/README.md)
