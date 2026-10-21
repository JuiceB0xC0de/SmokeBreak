---
name: svgbob
title: svgbob
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ascii-art, diagrams, quick, rust, svg]
homepage: https://ivanceras.github.io/svgbob-editor/
scout_score: 7
status: draft
---

# svgbob

**TLDR;** Turns ASCII diagrams drawn with dashes, pipes and plus signs into clean SVG, reading each character in the context of its neighbours.

Svgbob is a converter. You sketch a diagram with ordinary keyboard characters (dashes, pipes, plus signs, slashes, periods) and it outputs an SVG image. In the README's words, "Svgbob provides a cli which takes text as an input and creates an svg image as an output."

The reason to want this is that a diagram stays plain text. It is easy to write, easy to diff, and lives happily inside a README or a source comment, but you still get vector graphics out of it. The project's own framing: "Svgbob can create a nice graphical representation of your text diagrams."

The interesting part is that no character means one thing on its own. Each is interpreted according to its neighbours. A period becomes a rounded corner when lines meet it from below and from the right. A plus sign becomes a sharp corner or a full intersection depending on how many perpendicular lines touch it. A letter v turns into an arrowhead when a line arrives from above. Double quotes act as an escape, so text inside them is drawn as text rather than read as geometry.

It appears to be used in real documentation toolchains: the brief lists asciidoctor, zola, kroki, discourse, typst's bob-draw, and mdbook-svgbob. The homepage is a browser editor where you can try the same idea.

## Install

```
brew install svgbob
```

## Try this

```
svgbob --help
```
Prints the command-line options, which is the place to start since the README gives no usage examples.

```
svgbob_cli --help
```
Shows the help for the second installed executable, so you can compare it with svgbob.

## What's unique

The same character changes meaning depending on which lines touch it, so rough ASCII sketches come out as tidy curves, arrows and intersections instead of literal glyphs.

## Caveats

The README shows no command examples and the brief could not confirm release dates or maintenance status, so expect to learn the CLI from --help and the specification page.

## Links

- [Homepage (browser editor demo)](https://ivanceras.github.io/svgbob-editor/)
- [GitHub repository](https://github.com/ivanceras/svgbob)
- [Specification](https://ivanceras.github.io/content/Svgbob/Specification.html)
