---
name: latexml
title: LaTeXML
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, documents, latex, mathml, perl, xml]
homepage: https://math.nist.gov/~BMiller/LaTeXML/
scout_score: 5
status: draft
---

# LaTeXML

**TLDR;** Converts LaTeX documents into XML, HTML and MathML by emulating TeX in Perl, built so a math library could keep the meaning of its formulas.

LaTeXML reads a LaTeX or TeX document and writes it out as its own XML format. That XML is modelled on typical LaTeX document structure and takes ideas from HTML, MathML and OpenMath. From there it can be turned into HTML (in several flavors, with MathML and SVG), JATS, ePub and other formats. Math comes out as both content and presentation MathML.

It began during work on the Digital Library of Mathematical Functions at NIST. The DLMF needed its LaTeX sources turned into XML, for further manipulation and for building the web site. The authors wanted the library to focus on the semantics of the material, and in their words: "At the time, we found no software suitable to our needs, so we began development of LaTeXML in-house."

The unusual part is the method. Instead of rewriting LaTeX markup into HTML with pattern matching, LaTeXML emulates TeX's processing, in Perl, and builds a semantic document from what TeX would have understood. Because of that intermediate form, one source can feed several outputs. The idea underneath is that a typeset page is only one rendering of a document, and that the structure of a formula can be recovered and kept.

The project is honest about the difficulty. arXiv has offered experimental HTML preprints built with it, which shows how far it reaches in practice.

## Install

```
brew install latexml
```

## Try this

```
latexml --help
```
Prints the options for the core converter, which turns TeX or LaTeX source into LaTeXML's XML.

```
latexmlc --help
```
Shows the options for latexmlc, the front end that the brew package installs alongside the other tools.

```
latexmlmath --help
```
Shows the options for latexmlmath, one of the five installed executables.

## What's unique

It emulates TeX and builds a semantic XML intermediate rather than translating markup directly, and it emits both content and presentation MathML for math.

## Caveats

The homepage itself admits that "there are gaps in fidelity and coverage", so some LaTeX packages and documents will not convert faithfully.

## Links

- [LaTeXML homepage](https://math.nist.gov/~BMiller/LaTeXML/)
- [LaTeXML manual (DLMF-hosted copy)](https://dlmf.nist.gov/LaTeXML/)
- [Online editor and showcase](https://latexml.mathweb.org/editor)
- [arXiv HTML preprints (experimental, built with LaTeXML)](https://arxiv.org/)
