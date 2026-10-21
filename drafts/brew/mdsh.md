---
name: mdsh
title: mdsh
source: brew
category: languages-and-oddities
commitment: quick
tags: [ci, documentation, markdown, quick, rust, shell]
homepage: https://zimbatm.github.io/mdsh/
scout_score: 5
status: draft
---

# mdsh

**TLDR;** mdsh reruns shell commands embedded in a Markdown file and rewrites the results in place, so README examples never drift from reality.

mdsh is a small Rust preprocessor for Markdown. It reads a file (README.md by default, or stdin with `-i -`), looks for special blocks, HTML comments or links, runs the shell commands or file reads they describe, and writes the output back into the same document. Pass `-o` to send the result to another file or stdout instead.

The author kept pasting command output and file snippets into READMEs, and the pasted copies went stale. The aim was to keep the Markdown looking natural and to make the update idempotent: run mdsh again and the generated blocks refresh in place. In the project's words, "Most other tools would produce a new file but we really want a sort of idempotent operation here."

Each command has the form `[langname] <out_cmd> <in_cmd> [data_line]`, followed by optional data. The input side picks the source: `<` reads a file, `$` runs a shell command, and an empty in_cmd uses the data as written. The output side picks the result: a language name gives a fenced code block, `>` gives raw Markdown wrapped in comment tags, and `!` expands the data into shell variables. The commands can live in inline code, fenced blocks, HTML comments or link syntax. The small grid of input and output choices covers a lot of ground.

Adding `--frozen` to CI turns the tool into a check: it fails if the output would differ from the input, so docs must be updated along with the code. mdsh finds its blocks with regular expressions, not a Markdown parser, so it is a pragmatic tool, not a rigorous one.

## Install

```
brew install mdsh
# also available via: cargo install mdsh
# or, with Nix flakes: nix profile install github:zimbatm/mdsh
```

## Try this

```
mdsh --help
```
Prints the option list: -i, -o, -w, --frozen, --clean and -V.

```
mdsh --frozen
```
Fails if running mdsh would change the file. This is the suggested CI check that docs are current.

```
<!-- >< LICENSE.md -->
```
Put this hidden comment in a Markdown file. When mdsh runs, it includes LICENSE.md as raw Markdown at that spot.

## What's unique

It updates the Markdown file in place instead of producing a new one, so the source stays readable as a README. The closest relatives, such as Pandoc-based active code and Jupyter, generate new output.

## Caveats

mdsh executes whatever shell commands the Markdown contains, so only run it on files you trust; it also matches blocks with regexes, and the brief could not confirm recent maintenance (the homepage shows a 2019 copyright).

## Links

- [mdsh homepage](https://zimbatm.github.io/mdsh/)
- [Chris Warbo, activecode essay (closest related project, per README)](http://chriswarbo.net/essays/activecode/)
- [Issue #57 referenced for stdin handling](https://github.com/zimbatm/mdsh/issues/57)
