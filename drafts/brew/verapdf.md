---
name: verapdf
title: veraPDF
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, archival, file-formats, java, pdf, validation]
homepage: https://verapdf.org/home/
scout_score: 5
status: draft
---

# veraPDF

**TLDR;** A validator that checks PDF files against the PDF/A archival and PDF/UA accessibility standards, and reports exactly which structural rules a file breaks.

veraPDF takes a PDF and parses its internal structure, then checks it against the PDF/A standard (all parts and conformance levels) and PDF/UA accessibility parts 1 and 2. The output is a machine-readable validation report saying whether the file conforms and, if not, which rules failed. The suite also includes a metadata fixer that makes limited repairs, a policy checker, and a reporter that converts reports into other formats.

It was built for digital preservationists who need a definitive checker for files going into long-term archives. The homepage describes it as industry-supported, developed by a consortium led by the Open Preservation Foundation and the PDF Association, and funded by the EU's PREFORMA project.

The interesting part is the policy checker. It reads a PDF features report and compares it against a policy profile. Per the project, it "can be used to check for almost any quality in a PDF; for example, the use of annotations, irrespective of PDF/A." That makes it a way to see what is actually inside a PDF, not just a pass/fail verdict, and a door into how the format is put together and why archival standards exist.

## Install

```
brew install verapdf
# installs the verapdf CLI and verapdf-gui; depends on openjdk
```

## Try this

```
verapdf --help
```
Lists the command-line options for validation, reporting and policy checks.

```
verapdf-gui
```
Opens the desktop interface, where you can pick a PDF and run a conformance check.

```
docker run --rm -it -v "$(pwd):/data" ghcr.io/verapdf/cli:latest a.pdf
```
Runs the latest dev build of the CLI in Docker against a.pdf in the current directory, without a local install.

## What's unique

It covers PDF/UA accessibility alongside PDF/A, and its policy checker can enforce arbitrary rules about PDF features. Most validators stop at pass or fail, while this one exposes a full structural features report.

## Caveats

It is an industry compliance tool rather than a general PDF utility, the homepage text is sparse on commands, and the Docker default may lag the latest release.

## Links

- [veraPDF homepage](https://verapdf.org/home/)
- [veraPDF documentation site](https://docs.verapdf.org/)
- [GitHub repository (veraPDF-apps)](https://github.com/veraPDF/veraPDF-apps)
- [GUI manual (PDF)](https://github.com/veraPDF/veraPDF-apps/raw/integration/veraPDFPDFAConformanceCheckerGUI.pdf)
