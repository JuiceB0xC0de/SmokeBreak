---
name: eccodes
title: eccodes
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bufr, file-formats, grib, library, science, weather]
homepage: https://confluence.ecmwf.int/display/ECC
scout_score: 6
status: draft
---

# eccodes

**TLDR;** ECMWF's toolkit for reading and writing GRIB and BUFR, the packed binary formats weather centres use to exchange forecasts and observations.

ecCodes is a package from ECMWF, the European weather forecasting centre. It provides command-line tools and C, Fortran 90 and Python interfaces for decoding and encoding WMO GRIB (editions 1 and 2) and BUFR (editions 3 and 4) messages. It can also decode, but not encode, the GTS abbreviated header.

The core idea is a key/value model. Each message is a set of named keys, and you ask for a key to read it or assign one to change it. The tools are thin layers over that idea: `grib_ls` lists messages, `grib_dump` shows every key, `grib_get` pulls out chosen values, `grib_set` rewrites them, and `grib_copy` filters messages into new files. The `bufr_` and `gts_` tools follow the same pattern.

The interesting part is what it exposes. Forecast fields and observation reports are not stored as friendly tables. They are tightly packed binary with compression and layered code tables, and ecCodes is how most people get at what is inside. Poking at a file with `grib_dump` is a quick way to see how a forecast is actually packed and described.

It is the successor to GRIB-API and the primary GRIB encoding and decoding package at ECMWF. The tools were built to mirror the old options and behaviour. The main difference is that `bufr_dump` emits JSON.

## Install

```
brew install eccodes
# you need your own GRIB or BUFR file to try the tools on; the brief does not name a sample dataset
# Python bindings come separately: pip3 install eccodes
```

## Try this

```
grib_ls --help
```
Shows the options for listing the messages in a GRIB file and choosing which keys to print.

```
bufr_dump --help
```
Shows how to dump a BUFR message, whose output is JSON.

```
codes_info
```
Prints information about the installed ecCodes build and its version.

## What's unique

It is the reference toolkit from the forecasting centre that works with these formats every day, and one key/value interface covers GRIB, BUFR and GTS headers. The tools stay compatible with GRIB-API's options.

## Caveats

You need GRIB or BUFR files of your own to work on, and GTS support is decode-only.

## Links

- [ecCodes homepage (Confluence)](https://confluence.ecmwf.int/display/ECC)
- [GitHub repository](https://github.com/ecmwf/eccodes)
- [Releases (source tarballs)](https://confluence.ecmwf.int/display/ECC/Releases)
- [ECMWF Support Portal](https://support.ecmwf.int)
