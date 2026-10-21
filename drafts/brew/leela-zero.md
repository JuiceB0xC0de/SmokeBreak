---
name: leela-zero
title: Leela Zero
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, ai-history, alphago, go, gtp, mcts, neural-network, opencl]
homepage: https://zero.sjeng.org/
scout_score: 6
status: draft
---

# Leela Zero

**TLDR;** An open reimplementation of AlphaGo Zero: a Go engine whose neural network learned the game purely from self-play, trained in public by volunteers.

Leela Zero is a Go-playing engine built on the design from the paper 'Mastering the Game of Go without Human Knowledge'. It runs a Monte Carlo tree search, but without random playouts. A deep residual convolutional network supplies move priors and position evaluations instead. The engine reads that network from a plain-text weights file and works out the number of residual blocks and filters on its own at startup.

The interesting part is that the weights are the product, not the code. The README says recomputing them would take about 1700 years on commodity hardware, so the project ran a public distributed effort. Volunteers donated GPU time to generate self-play games, which became training data (search probabilities plus game outcome) for the next network. The homepage keeps a dated history of network releases and head-to-head match results.

That effort is over. The homepage says the distributed training has finished and the server is closed, with a shutdown dated 2021-02-15. What remains is a readable, runnable record of how a from-scratch Go engine was built in the open, and a way to see the AlphaGo Zero idea working on your own machine.

The engine is not meant to be used directly. It speaks the GTP protocol, so you pair it with a Go GUI such as Lizzie or Sabaki.

## Install

```
brew install leela-zero
# You also need a weights file, which is not included. The README links the best known network at https://zero.sjeng.org/best-network
# A GPU with OpenCL is strongly recommended. A GUI such as Lizzie or Sabaki is needed to play comfortably.
```

## Try this

```
leelaz --help
```
Lists the engine's options, including how to set weights and threads.

```
src/leelaz -w weights.txt
```
Starts the engine with the weights file you downloaded. This is the form shown in the README's supervised-learning section, run from a source checkout. Add --gtp to put it in GTP mode for a GUI.

```
dump_training white train.txt
```
Typed over GTP after a game ends, it saves gzip-compressed training data with the winner to a file.

## What's unique

It was an early open reproduction of AlphaGo Zero, trained in public with donated GPU time. The weights and the match history are the artifact as much as the code.

## Caveats

The engine does nothing without a separately downloaded weights file, the training server is closed, and the homepage points to SAI and KataGo as active alternatives.

## Links

- [Project homepage (status page and network history)](https://zero.sjeng.org/)
- [GitHub repository](https://github.com/leela-zero/leela-zero)
- [AlphaGo Zero paper, Nature 2017](https://www.nature.com/articles/nature24270)
