---
name: dotslash
title: DotSlash
source: brew
category: take-things-apart
commitment: quick
tags: [cli, executables, quick, reproducible-builds, rust, shebang]
homepage: https://dotslash-cli.com
scout_score: 5
status: draft
---

# DotSlash

**TLDR;** A shebang-driven tool that turns a small text manifest into a runnable file, fetching and verifying the right platform binary on first use.

DotSlash (`dotslash`) is a command-line tool that lets you represent a set of platform-specific, heavyweight executables with an equivalent small, easy-to-read text file. You put `#!/usr/bin/env dotslash` at the top of the file, mark it executable, and run it like any other program. The file itself is a JSON-like manifest (the README example uses `//` comments) listing, per platform, a download URL, size, hash digest, archive format and the path of the binary inside the archive.

On first run, DotSlash downloads the matching archive, decompresses it and checks it against the blake3 digest and size in the manifest. That is the small delay the README mentions. Later runs are near-instant. The README's example wraps Node.js, so `./node --version` behaves as if a real Node binary sat there.

The stated reason is source control. Checking large binaries into a repository bloats it, but depending on whatever the host machine has installed makes builds less repeatable. A manifest is small, readable in a diff, and pins exact hashes, so build toolchains and other tools can live in the repo without the weight. In the project's words, this reduces "dependencies on the host environment and thereby facilitating reproducible builds."

The idea underneath is what counts as an executable. Here it is a description of where a program lives and how to verify it, and the OS shebang mechanism does the rest. The homepage also mentions tools for generating DotSlash files from GitHub releases.

## Install

```
brew install dotslash
# Each user must chmod +x a manifest file before running it. No accounts or extra runtimes are mentioned. The README links an installation page but assumes `dotslash` is on your $PATH.
```

## Try this

```
dotslash --help
```
Lists the options the tool itself accepts.

```
chmod +x node
```
Marks a DotSlash manifest file as executable so the OS can hand it to dotslash via its shebang line.

```
./node --version
```
Runs the manifest-wrapped Node.js as if it were a normal binary, downloading and verifying it on first run.

## What's unique

A single text file is the executable, and it fetches the correct binary for each platform on demand. The repo stays small while still vendoring tools like Node.js.

## Caveats

The README's Node.js example pins v18.19.0 but shows v18.16.0 as output, which looks like a stale example, and the first run waits on a download.

## Links

- [DotSlash homepage](https://dotslash-cli.com)
- [GitHub repository (facebook/dotslash)](https://github.com/facebook/dotslash)
- [Installation instructions](https://dotslash-cli.com/docs/installation/)
- [How DotSlash works (execution docs)](https://dotslash-cli.com/docs/execution/)
