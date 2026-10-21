---
name: libpostal
title: libpostal
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [addresses, afternoon, c, library, nlp, openstreetmap]
homepage: https://github.com/openvenues/libpostal
scout_score: 5
status: draft
---

# libpostal

**TLDR;** A C library that parses street addresses from any country into labeled parts, trained on a billion addresses built from OpenStreetMap data.

libpostal takes a free-form address string and does one of two things. It splits it into labeled components such as house_number, road, city and postcode, or it returns a set of normalized expansions, with abbreviations spelled out and numbers written as digits. It is not a geocoder: it never turns an address into latitude and longitude, and it does not verify that an address exists. Bindings exist for Python, Ruby, Go, Java, PHP and NodeJS.

It came out of the OpenVenues project, which needed to dedupe venues drawn from millions of places found in Common Crawl data. Road versus Rd, California versus CA, New York City versus NYC: these defeat simple string matching and MinHash. The stated goal is to "understand location-based strings in every language, everywhere."

The parser is a Conditional Random Field trained on about a billion synthetic and real addresses built from OpenStreetMap, OpenAddresses and GeoPlanet, formatted with OpenCage templates. Random abbreviations and dropped components are added so it copes with messy input. A separate language classifier works out which language an address uses, so the right abbreviation dictionaries apply.

The idea underneath is that addresses are a language problem, not a string problem. Every country orders and abbreviates things differently, and a statistical model trained on open data can learn those habits. The authors publish the whole training pipeline, so the model is reproducible rather than a black box.

## Install

```
brew install libpostal
# Homebrew installs the library only. The README's CLI examples (./libpostal, ./address_parser) assume a source build under src/.
# Source build needs curl, autoconf, automake, libtool and pkg-config, then ./bootstrap.sh, ./configure --datadir=<dir with a few GB free>, make -j4, sudo make install.
# The model data (about 1.8GB) downloads on first make. Apple ARM Macs need --disable-sse2 on configure.
```

## Try this

```
./libpostal "Quatre vingt douze Ave des Champs-Élysées"
```
Run from src/ after a source build, it prints the normalized expansions of the French address, with the abbreviation spelled out and the number written as digits.

```
./address_parser
```
Starts an interactive shell where you type an address and see it split into labeled components.

```
cat some_file | ./libpostal --json
```
Reads one address per line from stdin and prints the expansions as JSON.

## What's unique

The model is trained entirely on open data, and the full training pipeline and roughly 100GB of training files are published. Normalization covers 60+ languages through plain dictionary files you can extend without writing C.

## Caveats

Installation is heavy, with a multi-GB data download, and the Homebrew install does not give you the CLI binaries the README shows; I could not confirm how actively it is maintained.

## Links

- [GitHub repository and README](https://github.com/openvenues/libpostal)
- [Releases page](https://github.com/openvenues/libpostal/releases)
- [pypostal (Python binding)](https://github.com/openvenues/pypostal)
