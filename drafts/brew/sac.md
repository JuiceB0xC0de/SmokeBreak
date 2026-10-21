---
name: sac
title: SAC: Seismic Analysis Code
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, needs-data, science, seismology, x11]
homepage: https://github.com/EarthScope/sac-community
scout_score: 7
status: draft
---

# SAC: Seismic Analysis Code

**TLDR;** A decades-old interactive program for filtering and inspecting seismometer recordings, with its own command language, now carried on by the community under Apache 2.0.

SAC reads and writes binary seismic data files that hold time series, typically ground motion recorded by seismometers. It runs as an interactive program with its own command language, built-in help and macros. It provides filtering and deconvolution for processing the waveforms. The helper executables cover related jobs: sacdiff, saclst and sacset inspect and edit SAC files, while sacswap, bbfswap and sgfswap handle byte order and graphics files.

The code has a long history. It was once distributed by LLNL as Fortran, later converted to C as SAC2000, and was generally difficult to obtain. After the LLNL and IRIS license agreement ended, EarthScope began releasing an open source derivative under Apache 2.0. This Community Edition is that derivative.

The idea underneath is that earthquake data is just long lists of numbers sampled over time, and a good deal of seismology is what you do to those lists: remove an instrument's response, filter out noise, pick out arrivals. SAC is a working example of a scientific tool shaped as a command shell rather than a library, which is how a generation of researchers learned to look at waveforms.

The README says: "If you have SAC working, use the help command from within SAC." The manual is the main documentation, and you need seismic data files of your own to get much out of it.

## Install

```
brew install sac
# SAC needs X11 (XQuartz on macOS). Set SACHOME and make sure SACAUX points to the aux/ data directory, or SAC exits with an error.
# Source the sacinit script for your shell from your startup file; brew puts configuration scripts in $HOMEBREW_PREFIX/opt/sac/share/sac
```

## Try this

```
sac --help
```
Prints the program's usage information, a quick check that the install and environment work.

```
echo $PATH ; echo $SACHOME ; echo $SACAUX
```
Checks that the environment variables SAC needs are set after editing your shell startup file.

```
sacdiff --help
```
Shows usage for the helper that compares SAC data files.

## What's unique

It is a long-running scientific tool with Fortran-to-C roots, kept alive by a community after its license changed. Its main interface is an interactive command shell with built-in help and macros, not a library API.

## Caveats

The README says EarthScope does not develop or maintain this software and that volunteer maintainers are still being sought, so activity is unclear; PNG output is off by default and needs a source build.

## Links

- [GitHub repository (homepage)](https://github.com/EarthScope/sac-community)
- [SAC Manual (HTML)](https://ds.iris.edu/files/sac-manual/index.html)
- [Releases (source and pre-built binaries)](https://github.com/EarthScope/sac-community/releases)
- [SAC Community mailing list](https://groups.google.com/a/earthscope.org/g/sac-community)
