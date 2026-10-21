---
name: kim-api
title: kim-api
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, library, molecular-dynamics, science, simulation]
homepage: https://openkim.org
scout_score: 5
status: draft
---

# kim-api

**TLDR;** A shared interface and curated catalogue of interatomic potentials, so one model ID runs unchanged in LAMMPS, ASE, DL_POLY and other molecular simulation codes.

Atomistic simulation needs a description of how atoms push and pull on each other. These descriptions are called interatomic potentials, or force fields. Historically each simulation code had its own format, so a potential written for one program had to be reimplemented for another, often with subtle bugs. OpenKIM is a curated repository of these models. The site lists about 1,532 models, 40 model drivers and 26 test drivers.

The kim-api package is the software layer underneath. It defines a Portable Model Interface (PMI), so a model is written once and can be loaded by any compatible simulator. A Simulator Model Interface (SMI) packages a model's native simulator input, parameters and metadata such as supported species and units. A model can carry its own code and parameters, or carry only parameters and lean on a shared model driver library. Bindings exist for C++, C, Fortran, Python and Julia.

The idea underneath is reproducibility in computational science. If a model has a stable ID like `SW_StillingerWeber_1985_Si__MO_405512056662_006`, two labs can be sure they simulated the same physics. The site also checks each potential for coding integrity and benchmarks it against material properties, which helps you choose between models.

This is a door into real research software rather than a toy. You need a simulator such as LAMMPS or ASE to do anything interesting with it.

## Install

```
brew install kim-api
# Models are obtained separately; see 'Obtaining KIM Models' in the KIM API docs.
# To use it, you also need a simulator that supports KIM, such as LAMMPS or ASE.
```

## Try this

```
kim-api-collections-management --help
```
Shows the options of the tool that manages your local collections of KIM models. The brief did not see this tool documented, so the help text is the guide.

```
kim init         SW_StillingerWeber_1985_Si__MO_405512056662_006 metal
```
In a LAMMPS input script, loads the Stillinger-Weber silicon model by its KIM ID and sets the unit style.

```
kim query        a0 get_lattice_constant_cubic crystal=["diamond"] species=["Si"] units=["angstrom"]
```
In the same LAMMPS script, asks the knowledgebase for the diamond silicon lattice constant under that model and stores it in the variable a0.

## What's unique

It is neither a single potential nor a simulator. It is a curated catalogue with a standard interface, so one model ID works across several codes, with benchmark results attached to each potential.

## Caveats

This is infrastructure for researchers: the Homebrew executables are undocumented in the pages the brief covered, models are installed separately, and you need a compatible simulator to get anything out of it.

## Links

- [OpenKIM homepage](https://openkim.org)
- [KIM API documentation (latest release)](https://kim-api.readthedocs.io/en/latest/)
- [KIM API overview page](https://openkim.org/kim-api/)
- [OpenKIM support forum](https://matsci.org/openkim/)
