---
name: wcstools
title: WCSTools
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, ancient, astronomy, c, fits, science]
homepage: http://tdc-www.harvard.edu/wcstools/
scout_score: 5
status: draft
---

# WCSTools

**TLDR;** Fifty-odd small command-line programs that turn pixel positions in astronomical images into sky coordinates, and back, by reading the WCS stored in FITS headers.

WCSTools is a set of C programs and a library for working with the world coordinate system stored in the header of an astronomical image. It reads FITS and IRAF .imh files. Given an image, `xy2sky` and `sky2xy` convert between pixel positions and positions on the sky. `gethead` and `sethead` read and edit header keywords, and other tools handle pixel work such as rotating, smoothing, resizing and stacking.

The larger programs deal with catalogs. `imcat`, `scat` and `imstar` read reference star catalogs, and `imwcs` matches stars it finds in an image against catalog stars and fits a new WCS into the header. The catalog files must be obtained separately, and their location is set through environment variables.

The idea underneath is that an image of the sky is only useful once you can say where on the sky each pixel points. The homepage puts it this way: "Astronomers often need to relate positions on an image of the sky to positions on the real sky to identify catalogued objects in images". A few header keywords describe that projection, and the library does the math.

The project grew out of the move to standardize WCS keywords in FITS, discussed at the 1994 ADASS conference. In the author's words, the subroutines came first, then the utilities, then the catalog and fitting programs. It is the work of one author, Jessica Mink, and has been described in ADASS papers from 1996 to 2018. The documentation and interface style are correspondingly old.

## Install

```
brew install wcstools
# Catalog-based tools (imcat, scat, imstar, imwcs) also need reference catalogs such as USNO, GSC, 2MASS or Tycho-2, with their location set through environment variables. You need your own FITS images to try the rest.
```

## Try this

```
imhead --help
```
Prints usage for the tool that lists an image's header, a first look at the keywords that hold the WCS.

```
xy2sky --help
```
Shows how to convert a pixel position in an image to sky coordinates.

```
imwcs --help
```
Shows the options for matching stars in an image to a catalog and fitting a WCS into the header.

## What's unique

The projection and fitting code is the same library used by SAOimage, SAOtng, ds9 and skycat, so header conversions match what those viewers do. It is a long-lived toolkit from a single author, split into many small Unix-style programs.

## Caveats

Maintained at a low level, with the latest release, 3.9.7, from April 2022; catalog tools need catalog files you must obtain yourself, and online catalog services may have changed since then.

## Links

- [WCSTools homepage](http://tdc-www.harvard.edu/wcstools/)
- [WCSTools README (installation and program list)](http://tdc-www.harvard.edu/software/wcstools/wcstools.readme.html)
- [WCSTools publications (ADASS papers)](http://tdc-www.harvard.edu/software/wcstools/publications/)
