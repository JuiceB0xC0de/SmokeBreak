---
name: faketty
title: faketty
source: brew
category: take-things-apart
commitment: quick
tags: [pty, quick, rust, shell, tty, unix]
homepage: https://github.com/dtolnay/faketty
scout_score: 5
status: draft
---

# faketty

**TLDR;** Runs any command inside a pseudoterminal while your redirects still work, so programs keep their colors and progress bars and you still get separate stdout and stderr logs.

Many programs check whether their output is a terminal. If it is not, because you redirected it to a file or a pipe, they switch off colors, progress bars and other formatting meant for a human. faketty runs the command inside a pty, so the program sees what looks like a real terminal, while its stdout and stderr still go wherever your shell redirects them.

The README's example is `faketty bazel build :target >log/out 2>log/err`. The logs get written, and the output looks the way it would on screen. In the README's words, this allows "logging the stdout and stderr (separately) of a process, without the output being different from what you'd see in the terminal if you weren't logging anything."

The closest existing tool is script(1). The README says faketty is similar to `script --quiet --return --command '...' /dev/null`, but script uses a single pty, "which makes it impossible to demultiplex stdout and stderr to different places." faketty keeps the two streams distinct. The README does not explain how it does that internally.

The idea underneath is how programs decide they are talking to a person. Terminal detection is a small, ordinary check, and once you see a tool fool it, you start noticing where it matters: CI logs, pipes, and any output that changes shape when you redirect it.

## Install

```
cargo install faketty
# The README only documents Cargo, so a Rust toolchain is needed. The Homebrew formula also installs the faketty executable: brew install faketty
```

## Try this

```
faketty --help
```
Prints usage for the wrapper.

```
faketty bazel build :target >log/out 2>log/err
```
The README's example: runs the build inside a pty, writing stdout to log/out and stderr to log/err, with terminal-style formatting preserved.

## What's unique

script(1) can fake a terminal but merges everything into one pty. faketty keeps stdout and stderr separate while the program still believes it has a terminal.

## Caveats

The README does not state supported platforms or a maintenance status; since it relies on ptys it is probably Unix-only, and programs that check more than tty status may still behave differently.

## Links

- [GitHub repository (homepage)](https://github.com/dtolnay/faketty)
- [crates.io package](https://crates.io/crates/faketty)
- [script(1) man page](https://man7.org/linux/man-pages/man1/script.1.html)
