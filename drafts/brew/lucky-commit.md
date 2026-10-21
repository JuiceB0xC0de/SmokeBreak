---
name: lucky-commit
title: lucky-commit
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [git, hashing, opencl, quick, rust, sha1]
homepage: https://github.com/not-an-aardvark/lucky-commit
scout_score: 5
status: draft
---

# lucky-commit

**TLDR;** Rewrites your latest git commit so its hash starts with a prefix you pick, by quietly padding the message with invisible whitespace.

lucky_commit takes the most recent commit and amends it so the hash begins with a hex prefix of your choosing. With no argument the prefix is 0000000. You can also use `_` as a wildcard, so `00_111` means two zeros, any hex character, then three ones. The visible commit message does not change.

The trick is that a git commit hash is just a SHA1 over the commit's contents, and the message is part of those contents. The tool appends a few characters of different kinds of whitespace, hashes the result, and tries again until the hash matches. The README puts it this way: "lucky-commit amends your commit messages by adding a few characters of various types of whitespace, and keeps trying new messages until it finds a good hash."

Speed comes from two things. Hashing runs on the GPU through OpenCL by default, with a multithreaded CPU fallback. For commits that are not GPG-signed, it caches the SHA1 state up to the final 64-byte block, so each attempt hashes only that one block. Signed commits are slower, because the whitespace goes at the end of the signature.

Underneath it is a small lesson in what a hash does and does not promise. Hashes identify content, but anyone who can vary a harmless part of that content can steer the first few hex digits. Short prefixes are cheap to search for, and each extra digit multiplies the work by 16. That is why a short hash on its own is a weak mark of authenticity.

## Install

```
brew install lucky-commit
# Alternative: cargo install lucky_commit --locked
# If the cargo build fails with 'cannot find -lOpenCL', add --no-default-features to use the CPU path.
```

## Try this

```
lucky_commit
```
Rewrites the latest commit so its hash starts with 0000000. Run `git log` before and after to see the change.

```
lucky_commit 00_111
```
Searches for a hash starting 00, then any hex character, then 111.

```
time lucky_commit --benchmark
```
Measures hashing speed on your machine so you can estimate how long a given prefix will take.

## What's unique

It leaves the visible commit untouched and searches over invisible whitespace in the message instead. It is also fast enough, with GPU hashing and cached SHA1 state, that short prefixes come back almost instantly.

## Caveats

It rewrites history, so only use it on a commit you can amend; GPG-signed commits and long messages are slower, and the CPU path is about 20x slower than the GPU by the author's own measurement.

## Links

- [Homepage / GitHub repository](https://github.com/not-an-aardvark/lucky-commit)
- [Arch Linux package (extra)](https://archlinux.org/packages/extra/x86_64/lucky-commit/)
- [Related project: every-git-commit-shorthash](https://github.com/not-an-aardvark/every-git-commit-shorthash)
