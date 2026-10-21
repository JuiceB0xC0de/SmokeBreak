---
name: puzzles
title: Simon Tatham's Portable Puzzle Collection
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, gui, logic, puzzle]
homepage: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/
scout_score: 7
status: draft
---

# Simon Tatham's Portable Puzzle Collection

**TLDR;** About forty small one-player logic puzzles, each its own command, from Simon Tatham's collection. Type a name and a puzzle window opens.

The Homebrew formula `puzzles` describes itself as a "Collection of one-player puzzle games". It installs around forty separate executables, one per game: `net`, `loopy`, `tents`, `galaxies`, `pearl`, `untangle`, `signpost`, `dominosa`, `blackbox` and many more. The scout notes call it Simon Tatham's collection, with an unusual range of grids and rules.

The names hint at the range. Some are classic sliding or flipping toys (`fifteen`, `sixteen`, `flip`, `twiddle`). Others are logic grids in the Sudoku or Nikoli tradition (`solo`, `keen`, `towers`, `unequal`, `tents`, `pattern`). A few are closer to graph or geometry problems (`untangle`, `net`, `bridges`, `loopy`).

The idea underneath is that a small rule set on a grid can hold a whole puzzle genre. Each command is a way into one of them, and playing a few shows how different constraint types feel to solve.

This entry is written from the formula's description and executable list only. The homepage could not be loaded when the brief was prepared, so details of how the games look and play are not confirmed here.

## Install

```
brew install puzzles
```

## Try this

```
net --help
```
Shows the command-line options for the net puzzle, one of the installed games.

```
untangle --help
```
Shows the options for the untangle puzzle.

```
loopy --help
```
Shows the options for the loopy puzzle.

## What's unique

One install gives you about forty distinct logic puzzles, each a separate command, with many unusual grids and rules rather than yet another Sudoku.

## Caveats

The homepage was unreachable when this was researched, so maintenance status and gameplay details are unverified; the scout also tags it as a GUI program, not a terminal one.

## Links

- [Homepage](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/)
