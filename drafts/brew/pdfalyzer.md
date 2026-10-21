---
name: pdfalyzer
title: pdfalyzer
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, forensics, pdf, python, reverse-engineering, visual, yara]
homepage: https://github.com/michelcrypt4d4mus/pdfalyzer
scout_score: 5
status: draft
---

# pdfalyzer

**TLDR;** Draws a PDF's hidden object tree in colour and scans its embedded streams with YARA, without ever executing the file's content.

A PDF is not a page of ink. It is a graph of numbered objects: dictionaries, streams, fonts and cross-references, all pointing at each other. pdfalyzer takes a file and renders that graph as a tree in the terminal, using Rich for the colour. Output can be exported as HTML, ANSI text, SVG or PNG. References that are not part of the tree show up as symlink-style nodes. Risky keys such as /OpenAction, /JavaScript and Type1 fonts are flagged in red.

It also pulls font information together from several objects, including character maps, and scans the embedded binary streams for suspicious byte patterns using YARA rules through the author's Yaralyzer library. It does not render or execute anything, so the README says it is safe to run on a malicious file. The author still suggests dangerzone for sanitising a suspect file before you open it.

The author built it because Didier Stevens's pdfid.py and pdf-parser.py are strong but lack visualisation and a data model you can write code against, and Peepdf was buggy and out of date. Under the hood, a Pdfalyzer class wraps PyPDF's objects in AnyTree nodes, so the same structure is available as a Python library. The README is candid: if its output disagrees with Stevens's tools, assume pdfalyzer is wrong.

Three helper commands come along: combine_pdfs, extract_pdf_pages, and extract_pdf_text, which also runs OCR on embedded images.

## Install

```
brew install pdfalyzer
# or: pipx install pdfalyzer
# optional extras for encrypted PDFs and text extraction: pipx install pdfalyzer[extract]
```

## Try this

```
pdfalyze -h
```
Shows the help screen listing the analysis-selection and output options.

```
pdfalyze martin_heidegger-being_illmatic.pdf
```
Runs the default analyses on a PDF: tree, rich tree, fonts and YARA scan, with the --streams scan left out.

```
extract_pdf_text martin_heidegger-being_illmatic.pdf
```
Forces extraction of all text, including text from embedded images via OCR.

## What's unique

It pairs a colourful tree view of PDF object relationships with YARA scanning and a Python data model, a combination the author found missing in older PDF forensics tools.

## Caveats

The author says edge cases are not extensively tested and some PDFs will fail to parse; PNG export relies on Inkscape or CairoSVG and can glitch.

## Links

- [GitHub repo and README (homepage)](https://github.com/michelcrypt4d4mus/pdfalyzer)
- [Homebrew formula](https://formulae.brew.sh/formula/pdfalyzer)
- [The Yaralyzer (YARA dependency)](https://github.com/michelcrypt4d4mus/yaralyzer)
