---
name: midicsv
title: midicsv
source: brew
category: take-things-apart
commitment: quick
tags: [audio, csv, file-formats, midi, perl, pipelines, quick]
homepage: https://www.fourmilab.ch/webtools/midicsv/
scout_score: 7
status: draft
---

# midicsv

**TLDR;** Two small programs that turn a MIDI file into one-event-per-line CSV and back, so grep, Perl, or a spreadsheet can edit music.

midicsv reads a standard MIDI file and writes a text file with one event per line. Each line starts with track number and absolute time, then an event type, for example `Track, Time, Note_on_c, Channel, Note, Velocity`. The file opens with a Header record and ends with End_of_file. Its companion csvmidi reads that same format and writes a MIDI file. Both use standard input and output, so they slot into a pipeline.

John Walker of Fourmilab wrote them because MIDI files are compact binary and hard to read or write without a special-purpose library, while Perl and Python are good at the kind of transformations musicians want. Once the file is text, transposing a song is a filter that shifts note numbers. Thickening a bass line is a script that duplicates each note an octave lower.

The idea underneath is that a binary format becomes approachable the moment you have a lossless text view of it. You can read what a MIDI file actually contains: tempo changes, program changes, note on and off events, all with readable names. You can also skip the source file entirely and have a script print CSV that csvmidi turns into music. The README's examples include a very simple drummer and a randomly generated guitar line.

## Install

```
brew install midicsv
# The Perl examples need Perl. The README suggests TiMidity++ as a software synthesiser for listening to the results.
```

## Try this

```
midicsv song.mid | perl transpose.pl | csvmidi >tsong.mid
```
Converts a MIDI file to CSV, shifts the notes down an octave with a Perl filter (leaving percussion alone), and writes tsong.mid. transpose.pl is the README's example script, which you need to write or copy.

```
perl drummer.pl | csvmidi >drumtrack.mid
```
A Perl script prints CSV for a repeating drum pattern with no source file, and csvmidi turns it into drumtrack.mid. drummer.pl comes from the README.

```
midicsv --help
```
Prints usage for the converter.

## What's unique

The CSV format is designed on purpose for text tools, spreadsheets, and databases, and the author states that no information is lost on a round trip. Editing or generating music through a pipe is a different approach from a sequencer or a MIDI library.

## Caveats

The software is finished rather than active (README dated 2004, revised 2008), assumes well-formed input, and does no musical sanity checking, so nonsense CSV becomes a MIDI file that instruments may not play sensibly.

## Links

- [midicsv homepage (Fourmilab)](https://www.fourmilab.ch/webtools/midicsv/)
