---
name: xorriso
title: xorriso
source: brew
category: take-things-apart
commitment: quick
tags: [boot, disc-images, file-formats, gnu, iso9660, quick]
homepage: https://www.gnu.org/software/xorriso/
scout_score: 6
status: draft
---

# xorriso

**TLDR;** A text-command tool for reading, building and editing ISO 9660 disc images, including bootable ones, session by session.

xorriso loads the directory tree of an existing ISO image, or starts an empty one. It applies a list of text commands to that in-memory model: add files, rename, delete, change permissions. Then it writes the result as a new image or as an extra session. It can also copy files back out of an image. The target can be a CD, DVD or BD, or just an ordinary file.

The idea underneath is that an optical disc is a sequence of sessions, each carrying its own management information. xorriso keeps the old information and appends changes as a new session, so an image can be updated incrementally instead of rebuilt. On overwritable media it emulates multi-session behaviour. Older sessions can still be listed and mounted.

It is a GNU project and part of the libburnia family (libburn, libisofs, libisoburn). The same engine appears in several forms: a command language driven by arguments, batch files or a dialog on standard input; `xorrisofs` and `xorrecord`, which emulate mkisofs and cdrecord; and a Tcl/Tk frontend, `xorriso-tcltk`. Bootable structures (El Torito, MBR, EFI System Partition) are added with `-boot_image`, which is a way into how a bootable ISO is laid out.

As the project puts it: "xorriso itself is entirely controlled by text commands."

## Install

```
brew install xorriso
No optical drive is needed to work with image files. Writing to real discs needs a CD/DVD/BD recorder and read-write access to the /dev/srN node, or superuser.
```

## Try this

```
man xorriso
```
Opens the detailed manual, which documents the whole command language.

```
xorriso -devices
```
Lists optical drives and their addresses (the homepage runs this as superuser).

```
xorrisofs --help
```
Shows the mkisofs-style options for building an image.

## What's unique

It edits an existing image in place, bootable structure included, and appends changes as new sessions rather than rebuilding. One engine is exposed as a command language, mkisofs and cdrecord emulators, and a GUI.

## Caveats

It does not write audio CDs or the UDF filesystems used for official video DVD/BD, and a wrong device target under /dev can overwrite a hard disk, which is why the stdio: prefix is required.

## Links

- [GNU xorriso homepage](https://www.gnu.org/software/xorriso/)
- [libisoburn git (libburnia), where xorriso's source lives](https://dev.lovelyhq.com/libburnia/libisoburn.git)
- [Source tarball on GNU FTP](https://ftp.gnu.org/gnu/xorriso/xorriso-1.5.8.pl02.tar.gz)
