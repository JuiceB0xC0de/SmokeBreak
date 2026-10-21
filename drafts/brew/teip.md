---
name: teip
title: teip
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [cli, pipelines, quick, rust, text-processing, unix]
homepage: https://github.com/greymd/teip
scout_score: 5
status: draft
---

# teip

**TLDR;** A Rust filter that tapes over parts of a text stream so an ordinary command like sed, tr or awk only touches the bits you pick.

teip reads standard input, selects regions of it, and hands only those regions to a command you name after `--`. The selected regions are called holes. They can be picked by character position, field, line number, regex match, or the output of another command. Whatever the command prints is spliced back into the original positions, and everything outside the holes passes through unchanged.

Run with no command, teip just shows the selection: `echo ABCDEFG | teip -c 1,3,5,7` prints `[A]B[C]D[E]F[G]`. That preview is the masking-tape picture in action. You can see what the tool would hand to the command before you give it one.

The idea underneath is a different split of labour. Classic tools like sed and awk each carry their own way of saying where to act and what to do. teip separates the two: it handles where, and any filter that reads lines and writes lines handles what. The README puts it as helping a command "do one thing well". The `-e` option pushes this further by letting a shell pipeline such as `grep -n -A 2` decide which lines become holes. A second teip can also run inside the holes of the first.

## Install

```
brew install teip
# Linux .deb/.rpm packages and a Windows installer are on the GitHub releases page; `cargo install teip` also works.
# The optional -G Oniguruma regex option needs `cargo install teip --features oniguruma`, which requires cargo, clang and libclang.
```

## Try this

```
echo ABCDEFG | teip -c 1,3,5,7
```
Shows the selection without running anything: characters 1, 3, 5 and 7 appear as holes, `[A]B[C]D[E]F[G]`.

```
echo "100 200 300 400" | teip -f 3 -- awk '{print $1*2}'
```
Sends only the third field to awk, which doubles it. The other fields stay as they were.

```
echo -e 'AAA\nBBB\nCCC\nDDD\nEEE\nFFF' | teip -e 'grep -n -A 2 CCC'
```
Lets grep choose the holes: the CCC line and the two after it are selected by line number.

## What's unique

sed and awk apply one script to a whole stream, while teip lets plain tools like tr or sed work on only the chosen spans. Selections can be nested, and the selector can be any shell pipeline.

## Caveats

The targeted command must print exactly one output line per input line, or teip fails with an error; `-s` solid mode works around this but spawns a process per hole, so it is slow on large files, and the -A, -B, -C, --sed and --awk options are marked experimental.

## Links

- [GitHub repository and README](https://github.com/greymd/teip)
- [Author's write-up (dev.to)](https://dev.to/greymd/teip-masking-tape-for-shell-is-what-we-needed-5e05)
- [Benchmark (wiki)](https://github.com/greymd/teip/wiki/Benchmark)
- [Latest release](https://github.com/greymd/teip/releases/latest)
