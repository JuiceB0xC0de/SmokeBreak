---
name: rdkit
title: RDKit
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, chemistry, library, machine-learning, python, science]
homepage: https://rdkit.org/
scout_score: 5
status: draft
---

# RDKit

**TLDR;** An open-source chemistry toolkit for Python: parse molecules, search substructures, compute fingerprints, and feed chemical structure into machine learning.

RDKit is a cheminformatics and machine-learning library. The core is written in C++, with Python 3 bindings generated through Boost.Python. You hand it molecules and it hands back molecule objects, computed properties, fingerprints, similarity scores, and substructure search results. It also handles 2D and 3D molecular operations.

The idea underneath is that a molecule can be treated as a data structure. Once a compound is a graph you can query, compare, and turn into a numeric fingerprint, chemistry starts to look like ordinary programming and ordinary machine learning. Questions like "which of these compounds contain this ring?" or "which two are most alike?" become function calls.

It reaches beyond Python. There is a PostgreSQL cartridge that brings chemical search into a database, plus wrappers for Java, C#, and JavaScript. The project describes itself plainly as "a collection of cheminformatics and machine-learning software written in C++ and Python." The code is BSD-licensed, and the project holds an annual user group meeting with materials published online.

This is a library, not a command-line tool. The Homebrew formula installs no executables, so you work from a Python session and the Getting Started in Python guide.

## Install

```
brew install rdkit
# You may need to set RDBASE:
export RDBASE=$HOMEBREW_PREFIX/opt/rdkit/share/RDKit
# The README's recommended route for Python users is conda:
# conda install -c conda-forge rdkit
```

## Try this

```
conda install -c conda-forge rdkit
```
Installs RDKit through conda, the route the README recommends for Python users, if you prefer it to Homebrew.

## What's unique

It is a library rather than an app, so the interesting part is what you build with it. That includes fingerprints, substructure search, and a PostgreSQL cartridge that puts chemical search inside a database.

## Caveats

It has no command-line tools, the homepage is mostly a list of links, and the Homebrew install may need RDBASE set by hand.

## Links

- [RDKit homepage](https://rdkit.org/)
- [Getting Started in Python](https://rdkit.org/docs/GettingStartedInPython.html)
- [GitHub repository](https://github.com/rdkit/rdkit)
- [Install guide (Docs/Book/Install.md)](https://github.com/rdkit/rdkit/blob/master/Docs/Book/Install.md)
