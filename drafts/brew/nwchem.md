---
name: nwchem
title: NWChem
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [chemistry, days-off, mpi, science, simulation]
homepage: https://nwchemgit.github.io
scout_score: 5
status: draft
---

# NWChem

**TLDR;** An open-source computational chemistry package from a US national lab, built to run quantum and classical molecular simulations from one processor up to thousands.

NWChem is a computational chemistry package maintained by the Environmental Molecular Sciences Laboratory (EMSL) at Pacific Northwest National Laboratory in Washington State. Its homepage lists a wide scope: biomolecules, nanostructures and solid-state systems, quantum and classical methods and combinations of them, ground and excited states, Gaussian basis functions or plane waves, and properties and relativistic effects.

It exists to make good use of big machines. The homepage says the software was developed "to efficiently use the aggregate resources available on supercomputers or computer clusters", and the project's stated strategy targets chemical kinetics and dynamics, chemistry at interfaces and in the condensed phase, and scaling to architectures of tens of petaflops and beyond. It scales "from one to thousands of processors", so a small job on a single machine is within its design range.

The idea underneath is that you describe a molecule and a calculation in an input file, which the project calls an input deck, and the program works out the physics and writes an output deck. The pages read for this entry do not spell out the file format, so the documentation is the place to learn it. The maintainers also run EMSL Arrows, a web service for newcomers that helps generate input decks, checks output decks against a large database of calculations, and does simple thermochemistry plus NMR and IR spectra for modest-sized molecules. It is a way to see what the field's inputs and outputs look like before installing anything.

## Install

```
brew install nwchem
# Installs the nwchem executable. The formula pulls in gcc, open-mpi, openblas, scalapack, libxc and python. Source tarballs for release 7.3.1 are on the GitHub releases page.
```

## Try this

```
nwchem --help
```
Runs the installed executable with a help flag. The brief did not confirm what it prints, so check the documentation if it does not behave like a usual help screen.

```
git clone https://github.com/nwchemgit/nwchem.git
```
Clones the master branch of the source repository, so you can read the code and the release notes.

```
git clone -b hotfix/release-7-3-0 https://github.com/nwchemgit/nwchem.git nwchem-7.3.1
```
Clones the 7.3.1 release line into a directory named nwchem-7.3.1.

## What's unique

It is serious research-grade chemistry software from a national lab, designed to scale to supercomputers, with a web front end (EMSL Arrows) that lets beginners try input and output decks without installing it.

## Caveats

This is research software with a steep learning curve, the pages read gave no run instructions, and the EMSL Arrows API is described as in alpha testing.

## Links

- [NWChem homepage and documentation](https://nwchemgit.github.io)
- [GitHub repository](https://github.com/nwchemgit/nwchem)
- [Releases](https://github.com/nwchemgit/nwchem/releases)
- [Release 7.3.1 notes](https://github.com/nwchemgit/nwchem/blob/master/release.notes.7.3.1.md)
