---
name: opentimestamps-client
title: opentimestamps-client
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [bitcoin, cryptography, network, protocol, quick, timestamping]
homepage: https://opentimestamps.org
scout_score: 6
status: draft
---

# opentimestamps-client

**TLDR;** Prove a file existed at a given time by anchoring its hash in Bitcoin, with no account, no fees, and no trusted notary.

`ots` hashes a file and sends only the digest to remote calendar servers. The calendars batch many digests from many people into a single Bitcoin transaction. What comes back is a small `.ots` proof file. Later, anyone can replay the proof against the Bitcoin blockchain and confirm the data existed no later than that block.

The idea underneath is a timestamp notary with no one to trust. The README says a calendar learns nothing about your file, because it only ever receives an opaque digest, and a per-file nonce protects the contents. The proof is a chain of operations (append, prepend, sha256) that leads from your file's hash to a block header. `ots info` prints that chain so you can read it.

Stamping needs no Bitcoin node and no fees, since the default calendars are free and run on donations. A fresh proof reads as pending for a few hours until the calendar completes it. `ots upgrade` then embeds the path to the block in the proof, so it no longer depends on the calendar. Verifying independently takes a local Bitcoin Core node, and a pruned one is fine.

The package also includes `ots-git-gpg-wrapper`, which timestamps PGP-signed Git commits. The README calls the project 'production software that has been in use for many years.'

## Install

```
brew install opentimestamps-client
# Or: pip3 install opentimestamps-client
# Needs Python 3. Stamping needs no account or Bitcoin node. Independent verification needs a local Bitcoin Core node, or a calendar can complete proofs for you.
```

## Try this

```
ots verify examples/hello-world.txt.ots
```
Verifies a bundled example proof from the repository; the README says it succeeds against Bitcoin block 358391, dated 2015-05-28.

```
ots info examples/two-calendars.txt.ots
```
Prints the file's sha256 and the proof's commitment operations and attestations, so you can see how a hash is chained to a block.

```
ots stamp README.md
```
Submits the file's digest to remote calendars and writes README.md.ots. Verifying it right away reports it as pending until Bitcoin confirms, which takes a few hours.

## What's unique

Stamping needs no node, account, or fees, and the proof file carries its own path to the block. The README's Privacy section is unusually candid about metadata leaks, such as timestamps made close together.

## Caveats

Proofs can sit pending for hours, independent verification needs a Bitcoin Core node, and the README lists known issues including no unit tests and a calendar protocol that may change incompatibly.

## Links

- [Project homepage](https://opentimestamps.org)
- [Client repository (README source)](https://github.com/opentimestamps/opentimestamps-client)
- [OpenTimestamps server repo, with otsd-backup.py for mirroring calendars](https://github.com/opentimestamps/opentimestamps-server)
