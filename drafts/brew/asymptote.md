---
name: asymptote
title: Asymptote
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, diagrams, language, latex, math, vector-graphics]
homepage: https://asymptote.sourceforge.io
scout_score: 6
status: draft
---

# Asymptote

**TLDR;** A programming language for technical drawings, where figures are code in a mathematical coordinate system and labels are typeset by real LaTeX.

Asymptote is a descriptive vector graphics language. You write a .asy file that describes a figure, run it through the `asy` command, and get vector output. The default is PostScript. It can also produce PDF, SVG, OpenGL, WebGL, V3D and legacy PRC, plus any format ImageMagick can produce. Labels and equations go through LaTeX, so the text in a figure matches the text in the paper around it.

The manual presents it as a standard for typesetting mathematical figures, much as TeX/LaTeX is the de facto standard for equations. It was inspired by MetaPost, but with a cleaner, C++-like syntax and more capability. Much of the language, including the graph module for scientific plots, is written in Asymptote itself, and figures are compiled to virtual machine code.

The idea underneath is that a drawing is a computation. In the manual's words, "one can use complex multiplication to rotate a vector". Geometry becomes something you calculate rather than something you drag around. A less obvious detail is deferred drawing. Labels and arrowheads have a fixed size, while the rest of the figure scales. Asymptote uses the simplex method to solve the size constraints between them, so the layout works out when the figure is finally sized.

The package also includes `xasy`, a rudimentary GUI for moving script-generated objects around. A web application lets you try the language without installing anything.

## Install

```
brew install asymptote
# Labels are typeset with LaTeX, so you will want a TeX installation for text-heavy figures. The brief did not verify this step. The web app at https://asymptote.ualberta.ca needs no install.
```

## Try this

```
asy --help
```
Lists the command-line options for compiling .asy source into figures.

```
xasy
```
Opens the rudimentary GUI for moving script-generated objects around.

## What's unique

Figures are programmed in a mathematical coordinate framework with real LaTeX labels. A simplex solver resolves layout between fixed-size labels and scaled geometry, which is unusual for a drawing language.

## Caveats

The homepage is nearly empty, so the manual is the place to learn it, and the manual calls the xasy GUI rudimentary and still under development.

## Links

- [Homepage](https://asymptote.sourceforge.io)
- [Manual (HTML)](https://asymptote.sourceforge.io/doc/index.html)
- [Gallery of examples and animations](https://asymptote.sourceforge.io/gallery/)
- [Asymptote Web Application](https://asymptote.ualberta.ca)
