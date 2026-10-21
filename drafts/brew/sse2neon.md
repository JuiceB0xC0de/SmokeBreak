---
name: sse2neon
title: sse2neon
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, arm, c, header-only, intrinsics, neon, simd, sse]
homepage: https://github.com/DLTcollab/sse2neon
scout_score: 5
status: draft
---

# sse2neon

**TLDR;** A single C header that lets x86 SSE intrinsic code compile on Arm by re-implementing each SSE call with NEON, showing how SIMD maps across architectures.

sse2neon is one header, `sse2neon.h`. You swap the x86 includes (`xmmintrin.h`, `emmintrin.h` and friends) for it, and code written against SSE intrinsics compiles for little-endian Arm and AArch64. It covers MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2 and AES. The README frames the goal as rapid porting of x86 SIMD code to Arm while preserving the original semantics.

The interesting part is reading how the mapping works. Some intrinsics become a single NEON instruction. Others need many: `_mm_maddubs_epi16` takes 22 instructions. The two instruction sets were not designed to match, so every function in the header is a small answer to the question of how to get the same result on different hardware.

The edges are where it gets honest. NEON trades IEEE-754 compliance for speed on denormals and NaNs, so some results differ from SSE. The README's example is `_mm_rsqrt_ps`, which returns NaN for 0.0 on NEON where SSE returns INF. Macros such as `SSE2NEON_PRECISE_MINMAX` and `SSE2NEON_PRECISE_SQRT`, defined as 1 before the include, switch to slower and more precise versions. The README also includes a table of which flags suit graphics, DSP, crypto, scientific, game physics and ML work.

## Install

```
There is no package-manager install in the README, and the brew formula installs no executables. Copy `sse2neon.h` into your source tree and include it in place of the SSE headers. Add the flag for your target, such as `-march=armv8-a+fp+simd+crypto+crc` for AArch64. Needs GCC 10+, Clang 11+, MSVC 2019+ or Apple Clang 12+, on little-endian Arm. Running the tests needs `make`, plus QEMU on non-Arm hosts.
```

## Try this

```
make check
```
Runs the built-in test suite in the tests directory with a basic configuration.

```
make FEATURE=crypto+crc check
```
Runs the test suite with the crypto and CRC features enabled.

```
make CROSS_COMPILE=aarch64-linux-gnu- check
```
Cross-compiles the tests for ARMv8-A AArch64 and runs them; on a non-Arm host this needs QEMU.

## What's unique

It is a drop-in single header that documents openly where NEON and SSE diverge, and lets you choose speed or precision per workload with compile-time flags.

## Caveats

Little-endian Arm only, older GCC and Clang have vector codegen bugs, default settings trade IEEE-754 accuracy for speed, and the brief could not confirm recent project activity.

## Links

- [sse2neon homepage (GitHub repository and README)](https://github.com/DLTcollab/sse2neon)
- [Arm Neon Intrinsics Reference](https://developer.arm.com/architectures/instruction-sets/simd-isas/neon/intrinsics)
- [Intel Intrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html)
