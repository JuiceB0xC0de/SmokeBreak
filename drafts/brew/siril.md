---
name: siril
title: Siril
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, fits, gui, image-processing, science]
homepage: https://www.siril.org
scout_score: 6
status: draft
---

# Siril

**TLDR;** Siril stacks hundreds of noisy telescope frames into one clean image, with calibration, colour correction and deconvolution, using real astronomy methods on your own data.

Siril is a desktop program for astronomical image processing. It reads raw camera frames, FITS files and SER video sequences. It calibrates them with bias, dark and flat master frames, aligns (registers) many frames, and stacks them into a single image. After that come enhancement tools such as colour calibration, deconvolution and histogram stretching. It also has science tools for star brightness variation and astrometry.

The idea underneath is signal-to-noise. A single exposure of a faint nebula is mostly noise. The project's own words: "Improve signal to noise ratio by combining many registered individual images." Align enough frames, reject the outliers, average the rest, and the faint signal survives while random noise cancels. Calibration frames remove the fixed patterns the camera itself adds, so what is left is the sky.

Preprocessing writes a new file for each step, and the SER and FITS-cube formats keep that cheap. Stacking runs in parallel across all cores. Registration can align on all stars, one star, or the nebulosity, which the site says helps with faint stars. SER support is native, so lucky-imaging workflows with tens of thousands of frames are practical.

It ships as a GUI app with a companion command-line binary, siril-cli, and the homepage says it can be driven manually or through scripts. It is GPLv3 and has a Journal of Open Source Software paper, which the homepage asks users to cite when they publish.

## Install

```
brew install siril
# GUI app plus siril-cli. Pulls in GTK3, OpenCV, ffmpeg and many more libraries, so expect a large download. You need your own telescope or camera data to get much out of it.
```

## Try this

```
siril
```
Opens the graphical application, where you can load FITS, raw or SER data and start a calibration and stacking workflow.

```
siril-cli --help
```
Lists the options of the command-line binary, the entry point for scripted processing.

```
siril --help
```
Prints the GUI binary's command-line options.

## What's unique

It covers the whole path from raw frames to a finished image in one free program, with native SER video handling for very large frame counts.

## Caveats

The brief could not verify the command-line interface or first-run steps, and the speed claims are the project's own; you need real astronomical frames to see it work.

## Links

- [Siril homepage](https://www.siril.org)
- [Source code (GitLab)](https://gitlab.com/free-astro/siril)
- [JOSS paper (Richard et al., 2024)](https://doi.org/10.21105/joss.07242)
