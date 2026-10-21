---
name: gammaray
title: GammaRay
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, debugging, gui, introspection, qt, reverse-engineering]
homepage: https://www.kdab.com/software-technologies/developer-tools/gammaray/
scout_score: 5
status: draft
---

# GammaRay

**TLDR;** A runtime inspector for Qt applications that lets you browse live objects, edit properties, and watch signals and state machines while the program runs.

GammaRay attaches to a running Qt application, or launches one, and shows its internals as Qt sees them. You can walk the QObject tree, read and change properties, invoke slots, and watch signal/slot connections. It also has specialised views for Qt Quick scene graphs, model/view proxy chains, state machines, and QGraphicsView scenes. It works on a local workstation or remotely against an embedded target.

It exists because an instruction-level debugger does not understand framework concepts. The README says GammaRay lets you work at "a much higher level, with the same concepts as the frameworks you use". A debugger shows stack frames and memory. GammaRay shows a QStateMachine's live state, or a chain of proxy models stage by stage.

The idea underneath is that a framework with built-in introspection can be examined from outside without being rewritten. Qt's QObject introspection mechanism describes the objects, their properties, and their connections at runtime, and GammaRay builds a tool on top of that. It runs alongside your debugger rather than replacing it. If you have ever wondered what a GUI program is doing behind its windows, this gives you a way to look.

## Install

```
brew install gammaray

The formula pulls in Qt modules and graphviz as dependencies, so expect a large download. You need a Qt application to inspect.
```

## Try this

```
gammaray --help
```
Lists the launcher's options, including how to start a program under inspection or attach to a running one.

## What's unique

Most debuggers show raw memory and stack frames. GammaRay understands Qt's own framework objects and can change properties in running code, including on remote embedded targets.

## Caveats

It relies heavily on Qt private headers, which can change between Qt releases, and the README does not say whether views for older Qt technology such as QtQuick1 and QScriptEngine still work with Qt 6.

## Links

- [KDAB homepage for GammaRay](https://www.kdab.com/software-technologies/developer-tools/gammaray/)
- [GitHub repository and README](https://github.com/KDAB/GammaRay)
- [INSTALL.md (build instructions)](https://github.com/KDAB/GammaRay/blob/master/INSTALL.md)
