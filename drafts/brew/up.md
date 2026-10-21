---
name: up
title: up (the Ultimate Plumber)
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [pipes, quick, shell, tui, unix]
homepage: https://github.com/akavel/up
scout_score: 5
status: draft
---

# up (the Ultimate Plumber)

**TLDR;** A terminal UI where you type a shell pipeline and see its output update live, so you can build grep, awk and sort chains against real data.

up, the Ultimate Plumber, sits at the end of a pipe. You send any text-emitting command into it, type a pipeline into the input box at the top, and press Enter. up runs your pipeline with `bash -c` and shows the result in a scrollable preview underneath. Change the pipeline, press Enter again, and the preview is replaced.

The usual way to build a long pipeline is to run a command, squint at the output, add a stage, and run it all again, often re-running the slow upstream command each time. up reads the input once into a buffer and reruns only what you typed against it. The README describes the goal as helping people interactively and incrementally explore textual data, using tools like grep, sort, cut, paste, awk, wc and perl. It credits Bret Victor's talks as an influence, and the author writes: "I was surprised no one seemed to write a similar tool before, that I could find." It also points to Pipecut as earlier prior art.

When the pipeline does what you want, Ctrl-X exits and saves it to an `up1.sh` file (or `up2.sh` and so on if that name is taken). Ctrl-C quits without saving. For input that never ends, Ctrl-S freezes the buffer and injects a fake EOF, so commands like wc or sort print results before the stream finishes. Ctrl-Q unfreezes.

The idea underneath is the Unix pipeline as something you can explore rather than compose blind. Watching each stage reshape real data is a good way to learn the classic text tools.

## Install

```
brew install up
# The README says the author has no Mac and cannot confirm it works there. Linux binary: https://github.com/akavel/up/releases/latest/download/up. Also on the AUR (aur/up) and FreeBSD (pkg install up). Needs bash.
```

## Try this

```
lshw |& ./up
```
Pipes the output of lshw into up so you can start typing pipelines against it. If installed via brew, run it as `up` instead of `./up`.

```
grep network -A2 | grep : | cut -d: -f2- | paste - -
```
Typed into up's input box on lshw output, this is the README's example. It reduces the output to two lines of wireless and ethernet interface names.

## What's unique

It reruns your pipeline against a buffered copy of the input each time you press Enter, so you build a pipeline one stage at a time against real data. It then saves the result as a script.

## Caveats

The README calls it a hobby project, signed October 2018. Pipelines run for real, so typing rm or dd is dangerous. The input buffer is fixed at 40 MB, the Mac build is untested, and there is no --help yet.

## Links

- [Project homepage and README (GitHub)](https://github.com/akavel/up)
- [Demo recording on asciinema](https://asciinema.org/a/208538)
- [Latest Linux release binary](https://github.com/akavel/up/releases/latest/download/up)
- [Pipecut, the earlier similar project](http://pipecut.org/index.html)
