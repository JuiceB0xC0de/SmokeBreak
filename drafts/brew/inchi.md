---
name: inchi
title: InChI
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c-library, cheminformatics, chemistry, identifiers, science]
homepage: https://www.inchi-trust.org/
scout_score: 5
status: draft
---

# InChI

**TLDR;** Turns a molecule's structure into a canonical text string and a 27-character hash, so chemical structures can be searched and compared like words.

InChI is the IUPAC International Chemical Identifier. It takes a chemical structure, described by atoms, bond connectivity, tautomers, isotopes, stereochemistry and charge, and produces a text string that names that structure. The same molecule should always give the same string, whichever program drew it.

The string is built in layers. The connectivity layer comes first, then separate parts for tautomeric, isotope, stereochemistry and charge information. Each layer adds detail, so two records can match on the basic skeleton and differ only in, say, stereochemistry. The README also describes the InChIKey, a hashed, fixed-length form of the InChI, which is what databases and search engines use for lookup.

The project exists because chemistry data needs a shared, non-proprietary way to say "this is the same compound." The README calls InChI "strictly unique, non-proprietary, open source, and freely accessible" and ties it to linking chemistry on the web and to the FAIR data principles. The idea underneath is canonicalization: reducing a graph of atoms to one agreed-upon string, which is a doorway into graph theory and cheminformatics.

The package ships the `inchi-1` command-line program and `libinchi`, a C library with an `inchi_main` demo. The README points to MOLfile and SDfile as the main inputs, but it does not spell out the full input and output workflow, so expect to read the docs.

## Install

```
brew install inchi
# No account or runtime needed. Release binaries and source builds are also available from the GitHub releases page.
```

## Try this

```
inchi-1 --help
```
Prints the command-line options, the quickest way to see what input and output the tool supports.

```
inchi_main --help
```
Runs the demo program that ships with the C library; the brief does not confirm its options, so this may only show usage.

## What's unique

It is an open standard rather than one program's private format, and the README says fuzzing (OSS-Fuzz) and static analysis (Coverity) run continuously. The 27-character InChIKey gives every structure a short, searchable fingerprint.

## Caveats

Beta features such as EnhancedStereochemistry and MolecularInorganics produce strings that are not stable across releases, so do not store them as persistent identifiers.

## Links

- [InChI Trust homepage](https://www.inchi-trust.org/)
- [GitHub repository (IUPAC-InChI/InChI)](https://github.com/IUPAC-InChI/InChI)
- [Web demo](https://iupac-inchi.github.io/InChI-Web-Demo/)
- [Generated source documentation](https://iupac-inchi.github.io/InChI/docs/index.html)
- [Latest release binaries](https://github.com/IUPAC-InChI/InChI/releases/latest)
