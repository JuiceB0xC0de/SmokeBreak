---
name: wuppiefuzz
title: WuppieFuzz
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, fuzzing, libafl, openapi, rest, rust, security]
homepage: https://github.com/TNO-S3/WuppieFuzz
scout_score: 5
status: draft
---

# WuppieFuzz

**TLDR;** A coverage-guided fuzzer that reads an OpenAPI spec and mutates HTTP requests against a running service, using feedback to find where the API breaks.

WuppieFuzz takes an OpenAPI specification in YAML and a target service that is already running. It builds HTTP requests from the spec, mutates them, and fires them at the API. It is built on LibAFL, the Rust fuzzing library, and developed by TNO.

The idea underneath is feedback-driven fuzzing, which is usually applied to binaries, moved up to the HTTP layer. If the target is instrumented, coverage data (a JaCoCo agent for Java, LCOV for Python) flows back into the loop and steers which requests get mutated next. Without instrumentation you still get endpoint coverage, which is computed from the spec alone, so you can see which parts of the API your campaign has touched.

It supports black box, grey box and white box testing. TNO says it targets "a wide audience of end-users, with a strong focus on ease-of-use, explainability of the discovered flaws and modularity". With `--report`, results land in a timestamped folder under reports/. A database of request data is also written, which you can explore in a Grafana dashboard.

## Install

```
brew install wuppiefuzz
# Needs a running target service and its OpenAPI spec. Code coverage needs an instrumented target (JaCoCo only for now). Binaries are also on the GitHub releases page, and a Docker image can be built from the repo.
```

## Try this

```
wuppiefuzz --help
```
Prints the usage line and the required parameters and flags.

```
wuppiefuzz fuzz --timeout 60 --report openapi.yaml
```
Fuzzes the running service described by the spec for 60 seconds and writes an endpoint coverage report under reports/.

```
wuppiefuzz fuzz --config=config.yaml --report --coverage-host=localhost:6300 --timeout=10 ./openapi.yaml
```
Combines a YAML config file with command-line flags; the command-line timeout overrides the config value.

## What's unique

It covers black box, grey box and white box REST fuzzing in one tool. You get an endpoint coverage figure from the spec alone, with no instrumentation of the target.

## Caveats

Code coverage works only with JaCoCo for now, the target must be started and instrumented beforehand, and the brief does not show a last release or commit date.

## Links

- [Homepage (GitHub repository)](https://github.com/TNO-S3/WuppieFuzz)
- [Tutorial](https://github.com/TNO-S3/WuppieFuzz/tree/main/tutorial)
- [Short how-to video](https://www.youtube.com/watch?v=-oR4d9aXrqo)
- [Rooijakkers et al., 2026, ICISSP](https://doi.org/10.5220/0000217100004061)
