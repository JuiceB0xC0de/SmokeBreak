---
name: vhs
title: vhs
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ci, demos, gif, quick, terminal, testing]
homepage: https://github.com/charmbracelet/vhs
scout_score: 5
status: draft
---

# vhs

**TLDR;** Write a plain-text script of typed commands and VHS plays it in a hidden terminal and renders a GIF, so demos can be regenerated like code.

VHS reads a `.tape` file, a list of instructions such as Type, Enter, Sleep, Wait and Set. It runs them in its own virtual terminal, captures frames, and writes the result named by the tape's Output line. GIF is the default. The README also lists MP4, WebM, a directory of PNG frames, and `.txt` or `.ascii` text output.

The README frames the purpose as "Write terminal GIFs as code for integration testing and demoing your CLI tools." A demo kept as a versioned text file can be diffed, reviewed and regenerated in CI, instead of being re-recorded by hand every time the tool changes.

The idea underneath is that a terminal session is just a deterministic sequence of input and output, so it can be treated as a test fixture. The README points to a golden-file workflow: commit the `.ascii` or `.txt` output and compare it between runs. Wait takes a regex, so a recording can sync with a spinner or prompt, and Hide/Show keeps setup steps out of the frame.

If you would rather not write a tape from scratch, `vhs record` captures a live session into one that you can then hand-edit. There is also a built-in SSH server, so a tape can be sent to a remote VHS host and a GIF comes back.

## Install

```
brew install vhs
# needs ttyd and ffmpeg on PATH; the brew formula lists both as dependencies
# alternatively, the official Docker image bundles the dependencies
```

## Try this

```
vhs new demo.tape
```
Creates a starter tape file for you to edit.

```
vhs demo.tape
```
Runs the tape in a virtual terminal and renders the GIF named by its Output line.

```
vhs record > cassette.tape
```
Records what you do in your terminal into a tape file; type exit to stop.

## What's unique

It makes a terminal demo a text file you can version and regenerate, with Wait on a regex and text output for golden-file comparison, which most screen recorders cannot do.

## Caveats

It needs ttyd and ffmpeg on PATH, Linux and Windows need extra setup per the README, and the SSH server exposes the host's commands unless you restrict authorized keys.

## Links

- [VHS on GitHub](https://github.com/charmbracelet/vhs)
- [Examples directory](https://github.com/charmbracelet/vhs/tree/main/examples)
- [VHS GitHub Action](https://github.com/charmbracelet/vhs-action)
