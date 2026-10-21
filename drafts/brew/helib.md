---
name: helib
title: HElib
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, cryptography, homomorphic-encryption, library, math]
homepage: https://github.com/homenc/HElib
scout_score: 6
status: draft
---

# HElib

**TLDR;** A C++ library for homomorphic encryption: add and multiply numbers while they stay encrypted, so the machine doing the math never sees the data.

HElib implements two homomorphic encryption schemes: BGV (with bootstrapping) and CKKS, which works on approximate numbers. You encrypt data into ciphertext objects, then add, multiply and shift them directly. The results are still encrypted, and only the key holder can read them. The README describes the library as an "assembly language for HE", with low-level routines such as set, add, multiply and shift.

The library is for people who want to program against the schemes themselves, not use a finished product. It manages noise automatically. In schemes like these every operation adds a little noise to the ciphertext, and too much makes the result unreadable. It also supports multi-threading and Ptxt (plaintext) objects that mirror the interface of Ctxt (ciphertext) objects, so the same code shape works on both. The README names ciphertext packing (Smart-Vercauteren) and Gentry-Halevi-Smart optimizations as the techniques underneath.

The README says that since mid-2018 the project has been heavily refactored for reliability, performance and, above all, usability for researchers and developers working on HE. The stated goal is to make homomorphic evaluation practical. A design report (eprint 2020/1481) explains the internals.

The idea that opens up is computing on data you cannot see. Once you have added two numbers inside ciphertexts, questions about outsourced computation, private queries and the cost of doing math under encryption follow naturally.

## Install

```
brew install helib
# Library, not a command-line tool: brew installs no executables. It depends on gmp and ntl.
# The README also describes source builds (needs g++ >= 11.3 or Apple clang >= 14, cmake >= 3.22, GNU make >= 4.3).
```

## Try this

```
cmake -DPACKAGE_BUILD=ON -DCMAKE_INSTALL_PREFIX=/home/alice/helib_install ..
```
Configures the recommended source build, which bundles HElib with NTL and GMP in one relocatable folder. Run it from a build directory inside the repo.

```
make -j16
```
Compiles HElib into the relocatable helib_pack folder. The 16 is an example thread count.

```
./BGV_packed_arithmetic -h
```
Prints the help for one of the BGV example programs, which demonstrate arithmetic on ciphertexts and plaintexts.

## What's unique

It is one of the reference implementations of BGV and CKKS, and it exposes the schemes directly as ciphertext and plaintext objects with low-level operations.

## Caveats

It is a C++ library with no command-line tool, it needs a recent toolchain, and the examples are BGV-focused. The README links a separate CKKS-security.md on the security status of the CKKS implementation.

## Links

- [HElib GitHub repository](https://github.com/homenc/HElib)
- [INSTALL.md (build and dependency instructions)](https://github.com/homenc/HElib/blob/master/INSTALL.md)
- [Examples and tutorials README](https://github.com/homenc/HElib/blob/master/examples/README.md)
- [Design and implementation of HElib (eprint 2020/1481)](https://eprint.iacr.org/2020/1481)
