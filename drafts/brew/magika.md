---
name: magika
title: Magika
source: brew
category: take-things-apart
commitment: quick
tags: [cli, file-types, machine-learning, quick, security]
homepage: https://securityresearch.google/magika/
scout_score: 5
status: draft
---

# Magika

**TLDR;** A small neural network that looks at a file's bytes and tells you what it really is, from Python source to Word documents, in milliseconds.

Magika is a command-line tool, with Python, Rust and JavaScript bindings, that identifies what kind of content a file holds. Give it paths, a directory with -r, or data on standard input, and it prints a label and description for each file, such as 'Python source' or 'Microsoft Word 2007+ document'. Output can be plain text, JSON, JSONL, a MIME type, or a custom format. The README says it covers 200+ content types, both binary and textual.

The classic approach is magic bytes and extensions: check the first few bytes, or trust the filename. That works for formats with a clear signature and fails on plain text, where a shell script, an INI file and a config snippet all look alike. Magika instead uses a model of a few MB, trained on about 100M samples, that predicts a type from a limited slice of each file's bytes. Because it reads only that slice, inference time stays near-constant whatever the file size.

The part worth poking at is how it handles doubt. Each content type has a pre-tuned confidence threshold. If the model is not sure enough, the result falls back to a generic label like 'Generic text document' or 'Unknown binary data' rather than a guess. Three prediction modes (high-confidence, medium-confidence, best-guess) tune how tolerant it is. The JSON output shows a score, and shows both the raw model output and the final output when the threshold overrules it.

The homepage says Google uses it at scale to route Gmail, Drive and Safe Browsing files to the right security and content-policy scanners. The README also states that it is not an official Google project and is not supported by Google.

## Install

```
brew install magika
# alternatives: pipx install magika, or cargo install --locked magika-cli. No account, API key or special hardware needed; it runs on a single CPU.
```

## Try this

```
magika --help
```
Lists the options, including -r, --json, --jsonl and --format with placeholders like %p and %l.

```
magika ./tests_data/basic/python/code.py --json
```
Identifies one Python file (from the repo's test data) and prints label, MIME type, group and score as JSON.

```
cat tests_data/basic/ini/doc.ini | magika -
```
Reads the file from standard input and prints '-: INI configuration file (text)'.

## What's unique

It replaces magic-byte matching with a neural classifier that has per-type confidence thresholds, so it can answer 'Unknown binary data' instead of bluffing. The same model also runs in the browser through a web demo.

## Caveats

The README says it is not an official Google project and is not supported by Google; the JavaScript package is experimental, the Go binding is work in progress, and outside pull requests are accepted only for limited cases.

## Links

- [Magika homepage](https://securityresearch.google/magika/)
- [GitHub repository](https://github.com/google/magika)
- [Research paper (ICSE 2025)](https://securityresearch.google/magika/additional-resources/research-papers-and-citation/)
- [Web demo (runs locally in browser)](https://securityresearch.google/magika/demo/magika-demo/)
