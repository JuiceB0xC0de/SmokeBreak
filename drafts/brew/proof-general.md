---
name: proof-general
title: Proof General
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, coq, emacs, formal-methods, math, theorem-proving]
homepage: https://proofgeneral.github.io
scout_score: 5
status: draft
---

# Proof General

**TLDR;** An Emacs front end for interactive theorem provers like Coq: you write a proof in one buffer and the prover checks it step by step.

Proof General is a set of Emacs Lisp modes that sit between your editor and a proof assistant. Open a file with a matching extension, such as `.v` for Coq, `.ec` for EasyCrypt, `.qrhl` for qrhl-tool or `.phx` for PhoX, and the right mode loads. The editor drives the prover's process and shows its responses next to your proof script.

A proof assistant is a program that checks mathematical arguments one step at a time. You state a theorem, then give tactics that reduce it to smaller goals until none remain. The prover rejects any step that does not hold. Proof General lets you advance and retract through that script from the editor. The project's own description: "a generic interface for proof assistants (also known as interactive theorem provers), based on the extensible, customizable text editor Emacs."

The idea is one interface for many provers, so the editing habits carry over. It was developed at the LFCS in the University of Edinburgh, mainly by David Aspinall. It is old enough to have dropped several provers over the years, including Twelf, Isabelle, LEGO and HOL98, so the current list is short. The Homebrew formula also installs a `coqtags` executable, which the README does not mention.

## Install

```
brew install proof-general
# Requires Emacs 25.2 or later (brew installs emacs as a dependency).
# Proof General does not install a prover. You need Coq, EasyCrypt, PhoX or qrhl-tool separately.
# Docs: $HOMEBREW_PREFIX/share/doc/proof-general
# The README's recommended route is MELPA or NonGNU ELPA: M-x package-install RET proof-general RET
```

## Try this

```
coqtags --help
```
Shows usage for the one executable the formula puts on your PATH.

```
M-x package-install RET proof-general RET
```
Inside Emacs, installs and byte-compiles Proof General from MELPA, the README's recommended route.

```
(load "~/.emacs.d/lisp/PG/generic/proof-site")
```
Added to your .emacs after a manual clone and make, so .v files open in Proof General's Coq mode.

## What's unique

One editor interface serves several proof assistants rather than one tool per prover. It has been around long enough to have outlived many of the provers it once supported.

## Caveats

It installs only the interface, so you need a prover such as Coq installed separately, and manual builds can fail with a version mismatch if make picks up the wrong Emacs.

## Links

- [Homepage](https://proofgeneral.github.io)
- [Proof General user manual](https://proofgeneral.github.io/doc/master/userman/)
- [GitHub repository (README source)](https://github.com/ProofGeneral/PG)
