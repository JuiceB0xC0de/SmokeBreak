---
name: katago
title: KataGo
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, ai, game, go, neural-network, self-play]
homepage: https://katagotraining.org/
scout_score: 6
status: draft
---

# KataGo

**TLDR;** A Go engine that taught itself to play at top levels from self-play alone, and tells you estimated score and territory, not just win rate.

KataGo is an open-source Go engine written in C++. It is an AlphaZero-like self-play system: a neural network plays against itself, learns from the games, and repeats. Per the README, it "is capable of reaching top levels rapidly and entirely from scratch with no outside data, improving only via self-play." It searches with Monte-Carlo Graph Search, which extends MCTS from trees to graphs.

The engine has no graphical interface. It speaks the Go Text Protocol (GTP), so a GUI such as KaTrain, Sabaki, or Lizzie launches it and sends moves. It needs a separate neural network weights file (.bin.gz) and a config file. It also has a JSON analysis engine for batch evaluation of whole games.

What sets it apart for players is the output. It estimates final score and territory ownership rather than only win rate. That makes handicap games and weaker-player games easier to review, because win rate alone says little when one side is far ahead. There is also a human-style mode, using a separate model, that imitates a chosen kyu level.

The homepage, katagotraining.org, hosts a public distributed training run. Volunteers donate GPU time to generate self-play games, so the same engine you install is the one producing the next network. The brew formula installs only the engine, not the training run. The methods are described in arXiv 1902.10565.

## Install

```
brew install katago
# Neural network weights are a separate download from https://katagotraining.org/ (the README recommends the strongest recent b18 net, b18c384nbt).
# You will want a GUI such as KaTrain, Sabaki, or Lizzie for normal play.
# Uses a GPU backend (OpenCL, CUDA, TensorRT, ROCm, ONNX, Metal on macOS) or the Eigen CPU backend.
```

## Try this

```
katago version
```
Prints the installed KataGo version, a quick check that the binary runs.

```
katago genconfig -model <NEURALNET>.bin.gz -output gtp_custom.cfg
```
Asks a series of questions and writes a custom GTP config file.

```
katago benchmark -model <NEURALNET>.bin.gz -config gtp_custom.cfg
```
Checks that the network and config work, suggests a thread count, and on OpenCL tunes for your GPU.

## What's unique

It reaches strong play with no outside game data, and it reports score and territory instead of only win rate. The same engine also powers a public volunteer training run.

## Caveats

It is a command-line engine that needs a separate network file and a GUI for normal play, first-run GPU tuning can take minutes, and some GPUs and drivers are known to fail.

## Links

- [KataGo distributed training homepage](https://katagotraining.org/)
- [KataGo GitHub repository (README)](https://github.com/lightvector/KataGo)
- [Accelerating Self-Play Learning in Go (arXiv paper)](https://arxiv.org/abs/1902.10565)
