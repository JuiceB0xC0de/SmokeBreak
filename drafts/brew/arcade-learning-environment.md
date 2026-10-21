---
name: arcade-learning-environment
title: Arcade Learning Environment
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, atari, emulator, gymnasium, python, reinforcement-learning, research]
homepage: https://github.com/Farama-Foundation/Arcade-Learning-Environment
scout_score: 6
status: draft
---

# Arcade Learning Environment

**TLDR;** A framework that turns Atari 2600 games into environments for AI agents: send a joystick action, get back the screen, the score, and a game-over flag.

The Arcade Learning Environment (ALE) wraps the Stella Atari 2600 emulator so a program can play games instead of a person. An agent sends an action, such as a joystick input. The environment returns the screen image, the current score, and a signal for whether the game has ended. The README says score and end-of-game extraction work automatically for more than 100 games.

The README says it exists to give researchers and hobbyists a platform for developing general AI agents, and points to the JAIR paper 'The Arcade Learning Environment: An Evaluation Platform for General Agents' for the goals. The idea is that one agent, with no game-specific knowledge, should be tested across many different games, and Atari titles are a cheap, varied, well-understood set to do that on.

In practice you use it from Python. The loop calls ale.act(action) to step the game and getScreenRGB() to read the screen. Through Gymnasium, gym.make('ALE/Breakout-v5') gives the standard reset/step interface that most reinforcement learning code expects. The emulation core is kept separate from rendering and sound so it stays fast with few dependencies. There are also C++ and WebAssembly interfaces, and a C++ vectorizer that runs several ROMs at once.

The README also points to the Machado et al. 2018 evaluation protocol, which covers sticky actions and the game mode and difficulty flavours. That makes this a door into how reinforcement learning results are measured, not only a way to run old games.

## Install

```
brew install arcade-learning-environment
# The brew formula installs no executables. It provides the library, with numpy, python@3.15 and sdl2-compat as dependencies.
# From PyPI: pip install ale-py (update pip first or the install may fail). Python 3.11 to 3.15 is supported.
# For Gymnasium: pip install "gymnasium[atari]"
# ROMs ship inside the pip package, so there is no separate download. No account or hardware needed.
```

## Try this

```
pip install ale-py
```
Installs the ALE Python package from PyPI, with the Atari ROMs bundled inside.

```
pip install "gymnasium[atari]"
```
Installs Gymnasium with the Atari extras, so gym.make('ALE/Breakout-v5') gives you a standard reset/step environment.

```
npm install @farama/ale-wasm
```
Installs the WebAssembly build so the emulator environment can run in a browser.

## What's unique

It makes an Atari game a standard Gymnasium environment in a few lines, and the same emulator core is reachable from Python, C++, and the browser. It also documents an evaluation protocol, not just a way to run games.

## Caveats

Free-threaded CPython builds are not supported, and nothing here plays the game for you: watching an agent needs render_mode='human' in Gymnasium, and the README does not discuss the licensing of the bundled ROMs.

## Links

- [Project homepage (GitHub)](https://github.com/Farama-Foundation/Arcade-Learning-Environment)
- [ALE documentation site](https://ale.farama.org/)
- [Gymnasium Atari environments page](https://gymnasium.farama.org/environments/atari/)
- [JAIR paper (2013)](https://jair.org/index.php/jair/article/view/10819)
