---
name: scummvm-tools
title: scummvm-tools
source: brew
category: take-things-apart
commitment: afternoon
tags: [adventure-games, afternoon, decompiler, game-formats, reverse-engineering, scummvm]
homepage: https://www.scummvm.org/
scout_score: 6
status: draft
---

# scummvm-tools

**TLDR;** About 44 utilities that unpack, convert and decompile the data files of classic adventure games, a hands-on way into how old games stored their assets.

scummvm-tools is a companion kit for ScummVM, the engine that replays old adventure games. It takes original game files such as archives, disk images and compiled scripts, and turns them into something readable. Outputs include extracted resources, recompressed audio (MP3, Vorbis or FLAC), rebuilt data packs, and decompiled or disassembled scripts.

The main entry point is `scummvm-tools-cli`. Give it an input file and it works out which tool to use, writing results to an `out/` directory next to the input. You can also name a tool with `--tool`. The extraction and compression tools also have a GUI wizard. The rest, including script decompilers such as `descumm`, `decine` and `degob`, are command-line only.

The idea underneath is that every game studio invented its own way of packing data. Sierra, LucasArts, Coktel Vision, Westwood and Delphine each did it differently. Each tool here encodes what someone learned about one of those formats, so reading what a tool does is a short course in file-format archaeology. The README describes the set as "a collection of various tools that may be useful to use in conjunction with ScummVM." It documents only some of the executables. Names like `grim_*`, `saga_unpack` and `msn_convert_mod` are not described there.

## Install

```
brew install scummvm-tools
# Most tools need original game data files, which you must supply yourself.
# Some shell scripts need extras: cdrdao and bchunk (Loom TG16), FFmpeg (convert_dxa.sh).
```

## Try this

```
scummvm-tools-cli --list
```
Prints the supported tools, which shows how many different games and formats the kit covers.

```
scummvm-tools-cli --help
```
Shows general usage. The brief says `--help <tool name>` gives each tool's options.

```
decine --help
```
Shows usage for the Delphine Cinematique script decompiler, which takes a type (-prc or -rel) and a version (-v1 for Future Wars, -v2 for Operation Stealth).

## What's unique

One command-line front end covers many unrelated games and picks the right tool from the input file. Few projects put this many old adventure-game formats in one place.

## Caveats

The README warns the tools are "not always in-sync with the latest STABLE version of ScummVM", its maintenance status is unclear, and almost everything needs original game files you must already own.

## Links

- [ScummVM homepage](https://www.scummvm.org/)
- [ScummVM Tools wiki page](https://wiki.scummvm.org/index.php?title=ScummVM_Tools)
- [scummvm-tools GitHub repository (README)](https://github.com/scummvm/scummvm-tools)
