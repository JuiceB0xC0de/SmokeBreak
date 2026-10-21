---
name: payload-dumper-go
title: payload-dumper-go
source: brew
category: take-things-apart
commitment: quick
tags: [android, firmware, go, quick, reverse-engineering]
homepage: https://github.com/ssut/payload-dumper-go
scout_score: 7
status: draft
---

# payload-dumper-go

**TLDR;** Unpacks Android OTA update packages into individual partition images like boot, system and vendor, so you can look inside a phone's firmware.

payload-dumper-go reads an Android OTA update, either a raw payload.bin or the OTA zip itself, and writes each partition out as an image file. You can list what is inside with -l, pull out only the partitions you want with -p, or dump everything. The zip is read in place, without first copying payload.bin out.

The interesting part is what an OTA actually is. Android's update_engine ships updates as a sequence of operations over partitions, described by a protobuf schema called update_metadata.proto. Full OTAs carry whole partitions. Incremental OTAs carry deltas, and applying one means starting from the previous version's images. This tool does that: extract the base full OTA to a directory, then pass it with -old along with the incremental OTA to rebuild the new images.

For delta updates, the payload leaves out the dm-verity hash tree and FEC parity data. The tool regenerates them itself, so no avbtool or fec tooling is needed, and it checks operation data, source images and final images with sha256. Its README says it "Fails loudly with a non-zero exit code." Decompression runs in parallel, with the worker count set by -c.

It is written in Go, shells out to the system xz library via CGO (the author found the pure Go xz about 6 times slower), and the payload package can also be used as a library. Once you have the images, you have raw material for the rest of the firmware-poking toolbox.

## Install

```
brew install payload-dumper-go
# needs the xz library on the system; on Linux or Windows, download a binary from the GitHub releases page and put it on PATH
```

## Try this

```
payload-dumper-go /path/to/payload.bin
```
Dumps every partition from the payload (or from an OTA zip) into the output directory as image files.

```
payload-dumper-go -o base_images base_full_ota.zip
```
Extracts a full OTA to a directory, which can serve as the base for an incremental update.

```
payload-dumper-go -old base_images -o new_images incremental_ota.zip
```
Applies an incremental OTA on top of the base images and writes the rebuilt partitions to new_images.

## What's unique

It rebuilds images from incremental OTAs and regenerates the dm-verity hash tree and FEC parity itself, with output claimed to be bit-exact, rather than leaning on external Android tooling.

## Caveats

PUFFDIFF, ZUCCHINI and LZ4DIFF delta operations are unsupported, so some partitions can fail on certain incremental OTAs, and images made with -no-fec are for inspection only, never for flashing; maintenance status was not confirmed.

## Links

- [GitHub repository (homepage)](https://github.com/ssut/payload-dumper-go)
- [Releases (binaries)](https://github.com/ssut/payload-dumper-go/releases)
- [Android update_metadata.proto (format source)](https://android.googlesource.com/platform/system/update_engine/+/master/update_metadata.proto)
