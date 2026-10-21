---
name: swift-section
title: swift-section
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, mach-o, macos, reverse-engineering, swift]
homepage: https://github.com/MxIris-Reverse-Engineering/MachOSwiftSection
scout_score: 6
status: draft
---

# swift-section

**TLDR;** Reads a compiled Mach-O binary and prints the Swift types, protocols, and field layouts inside it, without running the binary.

swift-section is a command-line tool that opens a Mach-O binary or a dyld shared cache and prints the Swift metadata it finds: types, protocols, conformances, and field layouts. You give it a file path (plus `--architecture` for fat binaries) and it writes text to stdout or a file. Subcommands include `dump`, `interface` (which generates a .swiftinterface-style file), `diff`, `snapshot`, `evolution`, and `objc` for Objective-C declarations.

The project's own description is that it recovers metadata "without loading them into a process." It parses the `__swift5_*` sections and the descriptors inside them, resolves relative pointers, and uses its own demangler to turn symbolic references into names. Field offsets and type and enum layouts are computed statically, the way the Swift runtime would compute them at load time. For some types behind metadata accessor thunks, it decodes the thunk's ARM64 code with Capstone instead of executing it.

The idea underneath is that a compiled Swift binary carries a surprising amount of its own structure, and the runtime's reading logic can be reimplemented offline. That makes the `diff` command interesting: it compares ABI at the binary level, so it can see field retypes, tag renumbering, and witness-table slot changes that a .swiftinterface diff cannot. It can also recover things not in the Swift metadata itself, such as `@objc` and override markers, from the ObjC method table.

It is the CLI wrapper around the MachOSwiftSection Swift library, which is built as an extension of MachOKit.

## Install

```
brew install swift-section
# Needs a Mach-O binary to inspect, so macOS is the natural home. Building from source needs Xcode 26.0 and a Swift 6.2+ toolchain. Binaries are also on GitHub Releases.
```

## Try this

```
swift-section dump /path/to/binary
```
Dumps all Swift information found in the Mach-O file.

```
swift-section dump --emit-field-offsets /path/to/binary
```
Adds statically computed field-offset comments to struct and class stored properties.

```
swift-section interface --output-path interface.swiftinterface /path/to/binary
```
Generates a complete Swift interface file from the binary and saves it.

## What's unique

It reads Swift metadata statically with its own demangler and layout engine, and its diff compares binary-level ABI rather than source-level interfaces.

## Caveats

Building from source needs Swift 6.2+ and Xcode 26.0+, some features such as `--resolve-c-module-names` are macOS-only and need Xcode, and the README gives no release dates, so maintenance status is unclear.

## Links

- [Homepage / GitHub repository](https://github.com/MxIris-Reverse-Engineering/MachOSwiftSection)
- [GitHub Releases (binaries)](https://github.com/MxIris-Reverse-Engineering/MachOSwiftSection/releases)
- [Documentation index (in repo)](https://github.com/MxIris-Reverse-Engineering/MachOSwiftSection/blob/main/Documentations/README.md)
