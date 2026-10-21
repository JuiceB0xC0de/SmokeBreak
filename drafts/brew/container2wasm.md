---
name: container2wasm
title: container2wasm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, browser, containers, docker, emulation, experimental, wasm]
homepage: https://ktock.github.io/container2wasm-demo/
scout_score: 6
status: draft
---

# container2wasm

**TLDR;** Converts a Linux container image into a single WebAssembly module that boots a real kernel on an emulated CPU, running under wasmtime or in a browser tab.

`c2w` takes a container image such as `ubuntu:22.04` and writes one `.wasm` file, `out.wasm` by default. That file contains the container, a Linux kernel, and an emulated CPU. Bochs emulates x86_64 and TinyEMU emulates RISC-V, both compiled to WASM. For the browser path, QEMU Wasm is used instead. Linux boots inside the emulator and starts the container with runc. A WASI runtime such as wasmtime can then run it like any other module.

The README's motivation is that more languages can target WASM, but existing programs are hard to run there. They usually need re-implementation and re-compilation. This tool skips that step: instead of porting the program, it emulates a machine that already runs it. The README calls it "a PoC converter" that enables "running unmodified containers on WASM."

The idea underneath is that a WASM sandbox is just another place to put a computer. Once a CPU emulator compiles to WASM, anything that runs on that CPU comes along. Host directories reach the guest through WASI filesystem calls and virtio-9p. Networking goes through a user-space stack, `c2w-net`, which uses `sock_*` calls under WASI and the Fetch API or WebSocket in a browser.

The live demo page shows the result: Debian, Python and Vim running in a browser tab, on both x86_64 and RISC-V.

## Install

```
brew install container2wasm
# Docker 18.09+ with BuildKit (DOCKER_BUILDKIT=1) is required for conversion; Buildx v0.8+ is recommended.
# You also need a WASI runtime such as wasmtime to run the output, or a browser for the --to-js path.
```

## Try this

```
c2w ubuntu:22.04 out.wasm
```
Converts the Ubuntu image into a WASI module named out.wasm.

```
wasmtime out.wasm uname -a
```
Runs the converted image under wasmtime and prints the guest kernel info.

```
c2w --to-js alpine:3.20 /tmp/out-js/htdocs/
```
Builds a WASM plus JS bundle, using emscripten and QEMU Wasm, that can be served to a browser.

## What's unique

It runs whole unmodified Linux containers, kernel included, inside a WASM sandbox by emulating a CPU. Per the README, similar tools either run containers on WASM runtimes without running the containers themselves, or emulate Linux in WASM without WASI support.

## Caveats

The README calls it experimental and a PoC. Containers for architectures other than x86_64 and riscv64 run slowly under extra emulation. Networking was tested only on Chrome, and support varies across WASI runtimes. The generated images also bundle GPL and LGPL software.

## Links

- [Live browser demo (Debian, Python, Vim on x86_64 and RISC-V)](https://ktock.github.io/container2wasm-demo/)
- [Source repository and README](https://github.com/ktock/container2wasm)
- [Release binaries](https://github.com/ktock/container2wasm/releases)
