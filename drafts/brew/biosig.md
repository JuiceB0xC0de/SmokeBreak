---
name: biosig
title: BioSig
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, ecg, eeg, file-formats, library, science]
homepage: https://biosig.sourceforge.net/
scout_score: 5
status: draft
---

# BioSig

**TLDR;** An open source library and set of converters for EEG, ECG and other biosignal file formats, built so researchers can read and write each other's recordings.

BioSig is a research toolkit for biomedical signals: EEG, ECoG, ECG, EOG, EMG, respiration and similar recordings. The core is a C/C++ library that reads and writes many biosignal data formats. Around it sit bindings and tools for Octave, Matlab, Python, Java, R and Mathematica, plus a real-time brain-computer interface system called rtsBCI and a viewer and scoring tool.

The Homebrew formula installs the library and a handful of command-line programs with names like `biosig2gdf`, `save2gdf`, `save2scp`, `save2aecg` and `heka2itx`. The names suggest format converters, for example to GDF, SCP-ECG and aECG. The brief did not confirm what each one does, so check their `--help` output before relying on a guess.

The project's stated aim is "to foster research in biomedical signal processing by providing open source software tools for many different applications." Labs record in different vendors' formats, and data acquisition, artifact processing, quality control, feature extraction, classification and visualization all depend on being able to open the file first. A shared reader library removes that obstacle.

The door here is the signal-processing field itself. Once a recording opens, you can see how brain and heart signals are stored, annotated and passed between tools. That is a long way into a field, and the converters are only the first step.

## Install

```
brew install biosig
# The Python package needs libbiosig installed first: pip install biosig
# Viewer via the project's tap: brew install schloegl/biosig/sigviewer
```

## Try this

```
biosig2gdf --help
```
Prints usage for what the name suggests is a converter to the GDF biosignal format.

```
save2gdf --help
```
Prints usage for the GDF saving tool, so you can see which input formats and options it accepts.

```
brew install schloegl/biosig/sigviewer
```
Installs SigViewer, a viewer for biosignal recordings with GDF event file import and export.

## What's unique

One GPL library reads many biosignal file formats, with bindings across Octave, Matlab, Python, Java, R and Mathematica. It also sits beside a real-time brain-computer interface system and a viewer.

## Caveats

You need your own recordings to do anything interesting, and the brief did not show usage text for the executables. Some components, such as the Octave and Matlab packages, are older than the core library.

## Links

- [BioSig homepage](https://biosig.sourceforge.net/)
- [BioSig download page](https://biosig.sourceforge.net/download.html)
