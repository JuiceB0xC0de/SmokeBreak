# Take things apart

Reverse engineering, binary exploration, watching programs execute, poking at file formats, circuits, firmware, apps.

259 entries. [Back to the shelf](README.md)

## quick

- **[afsctool](../drafts/brew/afsctool.md)**: A macOS command-line tool that applies, removes, and reports Apple's transparent filesystem compression on files Finder won't compress for you.  
  `apfs, compression, filesystems, macos, zfs`
- **[ares](../drafts/brew/ares.md)**: Paste in encoded or encrypted text and it searches chains of decoders, with no key or hint, until plaintext falls out.  
  `ciphers, crypto, ctf, encodings, puzzles, rust`
- **[Austin](../drafts/brew/austin.md)**: Austin reads a running Python process's memory from outside and samples every thread's call stack, with no changes to the code being watched.  
  `cpython, flamegraph, profiler, python, tui`
- **[AVI MetaEdit](../drafts/brew/avimetaedit.md)**: A preservation tool from the US National Archives project that reads, edits, validates and exports metadata inside AVI video files.  
  `avi, file-formats, metadata, preservation`
- **[badkeys](../drafts/brew/badkeys.md)**: Checks public keys, certificates and live SSH or TLS hosts against known cryptographic weaknesses, from the Debian OpenSSL bug to ROCA to leaked vendor keys.  
  `crypto, keys, math, security, ssh, tls`
- **[biodiff](../drafts/brew/biodiff.md)**: A terminal hex diff viewer that lines up two binary files using DNA sequence alignment, so inserted or deleted bytes don't scramble the comparison.  
  `bioinformatics, diff, hex, reverse-engineering, rust, tui`
- **[Bloaty](../drafts/brew/bloaty.md)**: Bloaty breaks a compiled binary down by section, symbol, or source file, showing where every byte went and what grew between builds.  
  `binaries, dwarf, elf, reverse-engineering, size-profiling`
- **[bpftop](../drafts/brew/bpftop.md)**: A top-style live table of the eBPF programs running inside your Linux kernel, with per-program runtime, event rate and CPU estimates.  
  `ebpf, kernel, linux, monitoring, tui`
- **[bsdiff](../drafts/brew/bsdiff.md)**: A pair of tools that diff two binary files into a small patch and rebuild the new file from the old, using suffix sorting.  
  `binary-diff, compression, executables, patching, suffix-array`
- **[btdu](../drafts/brew/btdu.md)**: A btrfs disk usage profiler that samples random points on the disk and asks the filesystem who owns them, so answers appear instantly and sharpen over time.  
  `btrfs, disk-usage, filesystem, sampling, tui`
- **[Capstone](../drafts/brew/capstone.md)**: A disassembly engine that turns raw machine-code bytes into readable instructions for dozens of CPU architectures, with a small shell tool, cstool, for trying it.  
  `c, disassembly, library, reverse-engineering`
- **[cargo-show-asm](../drafts/brew/cargo-show-asm.md)**: A Cargo subcommand that prints the assembly, LLVM-IR, MIR or WASM rustc produces for a single Rust function, so you can see what the compiler did.  
  `assembly, cargo, compiler, llvm, rust`
- **[CCExtractor](../drafts/brew/ccextractor.md)**: Pulls closed captions and subtitles out of TV recordings and other media files, and writes them as SRT or WebVTT.  
  `c, captions, srt, subtitles, video`
- **[CFR](../drafts/brew/cfr-decompiler.md)**: CFR turns compiled Java .class files and jars back into readable Java source, by recognising the patterns compilers leave behind.  
  `decompiler, java, jvm, reverse-engineering`
- **[ClangQL](../drafts/brew/clangql.md)**: ClangQL lets you query C and C++ source files with SQL, treating functions and globals as tables you can filter, count and select from.  
  `ast, c, clang, cpp, sql, static-analysis`
- **[C++ Insights](../drafts/brew/cppinsights.md)**: Rewrites your C++ the way Clang sees it, with lambdas, implicit conversions and deduced types spelled out as ordinary C++ you can read.  
  `c++, clang, compilers, learning, source-to-source`
- **[cyme](../drafts/brew/cyme.md)**: A cross-platform lsusb replacement that prints your USB buses and devices as a tree, down through descriptors, interfaces and endpoints.  
  `cross-platform, lsusb, rust, tui, usb`
- **[dcraw](../drafts/brew/dcraw.md)**: A single-file C program that decodes raw sensor data from hundreds of camera models, built by reverse engineering formats the makers never documented.  
  `c, file-formats, image-processing, raw-photos, reverse-engineering`
- **[deark](../drafts/brew/deark.md)**: A command-line tool that decodes obscure legacy file formats, converting old images, icons, and archives into modern files or extracting what is inside.  
  `file-formats, legacy, retro, reverse-engineering`
- **[decompose](../drafts/brew/decompose.md)**: Reads the live network connections of running Docker containers and draws the architecture, so you can see how an undocumented stack fits together.  
  `docker, graphviz, network, reverse-engineering, visualization`
- **[deheader](../drafts/brew/deheader.md)**: Eric Raymond's tool finds unneeded #include lines in C and C++ by deleting each one and asking your real compiler whether the build still passes.  
  `build, c, c++, includes, static-analysis`
- **[desed](../drafts/brew/desed.md)**: A step debugger for sed scripts that lets you watch a stream editor run one command at a time.  
  `debugger, language, reverse-engineering, sed`
- **[difftastic](../drafts/brew/difftastic.md)**: A diff tool that parses code into syntax trees and shows what actually changed, so reformatting and wrapping stop looking like rewrites.  
  `cli, diff, parsing, syntax, tree-sitter`
- **[DotSlash](../drafts/brew/dotslash.md)**: A shebang-driven tool that turns a small text manifest into a runnable file, fetching and verifying the right platform binary on first use.  
  `cli, executables, reproducible-builds, rust, shebang`
- **[dvd-vr](../drafts/brew/dvd-vr.md)**: Reads the navigation file on a DVD-VR disc from a recorder or camcorder and lists every recording on it, built by reverse engineering.  
  `dvd, file-formats, reverse-engineering, video`
- **[elfx86exts](../drafts/brew/elfx86exts.md)**: Disassembles a compiled binary and reports which CPU instruction set extensions it uses, plus a guess at the minimum Intel generation needed to run it.  
  `cpu, disassembly, reverse-engineering, rust, x86`
- **[Enchive](../drafts/brew/enchive.md)**: A tiny dependency-free C tool that encrypts files to yourself, producing archives indistinguishable from random bytes, with keys you can derive from a passphrase.  
  `archival, c, crypto, curve25519, encryption`
- **[evtx](../drafts/brew/evtx.md)**: A Rust parser that turns Windows binary .evtx event logs into XML or JSON on any platform, plus a browser viewer that runs locally.  
  `file-formats, forensics, reverse-engineering, rust, windows`
- **[Exomizer](../drafts/brew/exomizer.md)**: A file compressor built so the compressed data can be unpacked quickly on 8-bit machines, a small door into retro constrained-machine engineering.  
  `8-bit, compression, demoscene, retro`
- **[f3](../drafts/brew/f3.md)**: Fills a flash drive with checkable pseudorandom data, then reads it back to expose cards that claim far more capacity than they hold.  
  `counterfeit, flash, hardware, needs-hardware, storage, testing`
- **[faketty](../drafts/brew/faketty.md)**: Runs any command inside a pseudoterminal while your redirects still work, so programs keep their colors and progress bars and you still get separate stdout and stderr logs.  
  `pty, rust, shell, tty, unix`
- **[fatsort](../drafts/brew/fatsort.md)**: A small C tool that reorders the directory entries on FAT and exFAT volumes, so dumb players and car stereos play files in the order you want.  
  `c, exfat, fat, filesystems, mp3`
- **[foremost](../drafts/brew/foremost.md)**: Foremost carves files out of raw disk images by recognising their headers and footers, even when the filesystem that once listed them is gone.  
  `data-carving, disk-images, file-formats, forensics, reverse-engineering`
- **[gfxutil](../drafts/brew/gfxutil.md)**: A small macOS tool that converts Apple firmware Device Properties between text and binary form, a peek at how firmware describes hardware to the OS.  
  `device-properties, firmware, macos, reverse-engineering`
- **[go-size-analyzer](../drafts/brew/go-size-analyzer.md)**: gsa takes a compiled Go binary and shows which packages and sections take up its space, as a table, treemap, or terminal UI.  
  `binary-analysis, go, reverse-engineering, treemap, tui`
- **[gzrt](../drafts/brew/gzrt.md)**: gzrecover skips past the damaged bytes in a corrupted .gz file and saves whatever it can still read, where gunzip gives up at the first error.  
  `compression, file-formats, forensics, gzip, recovery`
- **[hexapoda](../drafts/brew/hexapoda.md)**: A terminal hex editor that colours each byte by value and edits the way Helix and Kakoune do: select first, then act.  
  `binary, hex-editor, modal-editing, tui`
- **[imessage-exporter](../drafts/brew/imessage-exporter.md)**: A read-only Rust tool that opens the local iMessage SQLite database, or an iPhone backup, and exports your conversations to plain text or HTML.  
  `backup, ios, macos, reverse-engineering, rust, sqlite`
- **[innoextract](../drafts/brew/innoextract.md)**: Unpacks Windows Inno Setup installers on any OS without running them or needing Wine, so you can see what a setup.exe actually contains.  
  `file-formats, gog, installers, reverse-engineering`
- **[ipapatch](../drafts/brew/ipapatch.md)**: A single Go binary that injects a dylib load command into the Mach-O binaries inside an iOS IPA, and into its plugins, with no external tools.  
  `go, ios, ipa, mach-o, reverse-engineering`
- **[jadx](../drafts/brew/jadx.md)**: jadx turns Android APKs and Dex files back into readable Java source, with a command-line tool and a GUI for browsing the result.  
  `android, decompiler, gui, java, reverse-engineering`
- **[jbig2dec](../drafts/brew/jbig2dec.md)**: A decoder for JBIG2, the monochrome image compression format hiding inside many scanned PDFs, with a command-line tool for unpacking streams.  
  `decoder, image-formats, jbig2, library, pdf`
- **[jbig2enc](../drafts/brew/jbig2enc.md)**: An open encoder for JBIG2, the format that quietly shrinks scanned PDFs by reusing one picture of each letter wherever it appears.  
  `compression, image-formats, jbig2, pdf, scanning`
- **[jbigkit](../drafts/brew/jbigkit.md)**: Converters and a C library for JBIG1, the fax-era lossless bilevel image standard that encodes pictures as a coarse layer followed by refinements.  
  `c-library, compression, fax, image-formats, jbig, netpbm`
- **[kuto](../drafts/brew/kuto.md)**: Kuto splits a finished JavaScript bundle into a main file plus cached chunks, so returning visitors only download the code that changed.  
  `bundler, code-splitting, esm, javascript, node`
- **[landrun](../drafts/brew/landrun.md)**: Put landrun in front of any Linux command and the kernel itself restricts which files and network ports it can touch, with no root or containers.  
  `kernel, landlock, linux, sandbox, security`
- **[LCDF Typetools](../drafts/brew/lcdf-typetools.md)**: Eleven small command-line tools that open up OpenType, TrueType and Type 1 fonts to read their features and convert them into TeX and PostScript files.  
  `file-formats, fonts, opentype, tex, truetype, type1`
- **[ldid-procursus](../drafts/brew/ldid-procursus.md)**: A command-line tool that signs Mach-O binaries with a real key or a fake signature, a direct way to see how iOS and macOS code signing works.  
  `code-signing, ios, mach-o, macos, reverse-engineering`
- **[libeatmydata](../drafts/brew/libeatmydata.md)**: A tiny LD_PRELOAD library that makes any program's fsync calls do nothing, so it runs faster and stops being crash-safe.  
  `fsync, ld_preload, linux, syscalls, testing`
- **[libfaketime](../drafts/brew/libfaketime.md)**: Makes one program believe it is a different date, without touching the real system clock. Useful for expired certificates, year-2038 tests, and reproducible builds.  
  `ld-preload, library, simulation, testing, time`
- **[lzfse](../drafts/brew/lzfse.md)**: Apple's open-sourced LZFSE compressor in plain C, pairing Lempel-Ziv matching with Finite State Entropy coding for zlib-like ratios at higher speed.  
  `apple, c, codec, compression, library`
- **[lzsa](../drafts/brew/lzsa.md)**: A byte-aligned compression format and packer built so 8-bit CPUs like the Z80 and 6502 can unpack data fast, with tiny decompressors.  
  `6502, 8-bit, compression, formats, retro, z80`
- **[Magika](../drafts/brew/magika.md)**: A small neural network that looks at a file's bytes and tells you what it really is, from Python source to Word documents, in milliseconds.  
  `cli, file-types, machine-learning, security`
- **[mat2](../drafts/brew/mat2.md)**: Strips hidden metadata from images, PDFs, Office files, audio, video and archives, and admits it cannot promise the result is fully clean.  
  `file-formats, metadata, privacy, python`
- **[Mergiraf](../drafts/brew/mergiraf.md)**: A Git merge driver that parses code into syntax trees, so it can resolve conflicts that line-by-line merging gives up on.  
  `developer-tools, git, merge, parsing, rust, syntax-trees`
- **[mftrace](../drafts/brew/mftrace.md)**: Turns TeX's METAFONT bitmap fonts like Computer Modern into scalable outline fonts by rendering them large and tracing the pixels back into curves.  
  `fonts, metafont, reverse-engineering, tex, vectorizing`
- **[midicsv](../drafts/brew/midicsv.md)**: Two small programs that turn a MIDI file into one-event-per-line CSV and back, so grep, Perl, or a spreadsheet can edit music.  
  `audio, csv, file-formats, midi, perl, pipelines`
- **[mobiledevice](../drafts/brew/mobiledevice.md)**: A small macOS command-line tool that talks to iPhones and iPads over USB through Apple's private MobileDevice framework: list devices, install apps, tunnel ports.  
  `apple, ios, macos, needs-hardware, reverse-engineering, usb`
- **[msitools](../drafts/brew/msitools.md)**: Open, dump, diff and extract Windows .MSI installers from a Mac or Linux terminal, or build new ones from XML without Windows.  
  `file-formats, installers, reverse-engineering, windows`
- **[objconv](../drafts/brew/objconv.md)**: A small converter that turns x86 object files and libraries between ELF, PE/COFF, OMF and Mach-O, and also disassembles them.  
  `disassembler, elf, mach-o, object-files, reverse-engineering, x86`
- **[paperkey](../drafts/brew/paperkey.md)**: Strips an OpenPGP secret key down to its few hundred secret bytes so you can print it on paper and rebuild the full key later.  
  `backup, file-format, gpg, openpgp`
- **[patchelf](../drafts/brew/patchelf.md)**: Edits a compiled Linux binary's loader path, library search paths and dependency list in place, without recompiling, and shows how dynamic linking works.  
  `elf, linking, linux, reverse-engineering`
- **[patchutils](../drafts/brew/patchutils.md)**: Two dozen small commands that treat patch files as data you can list, filter, split, merge and repair instead of just applying.  
  `ancient, cli, diff, patch`
- **[payload-dumper-go](../drafts/brew/payload-dumper-go.md)**: Unpacks Android OTA update packages into individual partition images like boot, system and vendor, so you can look inside a phone's firmware.  
  `android, firmware, go, reverse-engineering`
- **[pgpdump](../drafts/brew/pgpdump.md)**: Prints the packet structure inside a PGP file, so you can see how OpenPGP messages, signatures and keys are actually laid out.  
  `file-formats, openpgp, pgp, protocol, reverse-engineering`
- **[pngcheck](../drafts/brew/pngcheck.md)**: Walks a PNG file chunk by chunk, printing offsets, lengths and decoded fields, and flags anything invalid, misplaced or obsolete.  
  `file-formats, image, png, reverse-engineering`
- **[precomp](../drafts/brew/precomp.md)**: Precomp opens up zip, PDF, PNG and similar files, undoes the compression inside them, and stores the raw data so it can be compressed again, smaller.  
  `compression, deflate, file-formats, lossless`
- **[psftools](../drafts/brew/psftools.md)**: A NetPBM-style toolkit that converts bitmap fonts from old machines like the BBC Micro, Amstrad CP/M and DOS into PSF and back out again.  
  `bitmap, file-formats, fonts, retro, reverse-engineering`
- **[Radamsa](../drafts/brew/radamsa.md)**: A fuzzer that works like cat: pipe in sample data, get back subtly broken variants, and watch what falls over when you feed them to a program.  
  `fuzzing, security, testing, unix-filter`
- **[rbspy](../drafts/brew/rbspy.md)**: A sampling profiler that attaches to a running Ruby process by PID and shows which functions eat the time, with no restart or code changes.  
  `flamegraph, profiler, ruby, rust`
- **[rdb](../drafts/brew/rdb.md)**: A Go tool that opens Redis RDB snapshot files and turns them into JSON, memory reports, biggest-key lists, or a flame graph of key prefixes.  
  `binary-format, flame-graph, go, redis, reverse-engineering`
- **[recoverpy](../drafts/brew/recoverpy.md)**: A terminal tool that scans a raw disk for a string you remember, then lets you walk the surrounding blocks to recover deleted text by hand.  
  `disk, forensics, linux, python, tui`
- **[rura](../drafts/brew/rura.md)**: A terminal scratchpad where you type a shell pipeline and watch its output update live, stage by stage, instead of editing and rerunning.  
  `debugging, pipelines, shell, tui`
- **[sequin](../drafts/brew/sequin.md)**: Pipe any program's coloured output into sequin and it names every ANSI escape sequence and says what it does, a quick look at how terminals are told what to draw.  
  `ansi, debugging, go, terminal, tui`
- **[sha1dc](../drafts/brew/sha1dc.md)**: A sha1sum lookalike that also notices when a file was crafted to collide, like the SHAttered PDFs, by spotting the fingerprints of the attack.  
  `cryptography, hashing, math, reverse-engineering`
- **[shmcat](../drafts/brew/shmcat.md)**: A small C tool that dumps System V and POSIX shared memory segments to your terminal, like cat for memory shared between processes.  
  `c, debugging, ipc, shared-memory, unix`
- **[sng](../drafts/brew/sng.md)**: Turns a PNG into editable text and compiles it back, so you can read and change every chunk of the file in a text editor.  
  `file-formats, png, reverse-engineering, text`
- **[sqlite3_analyzer](../drafts/brew/sqlite-analyzer.md)**: A small tool that reads an SQLite file and reports where every page went, table by table and index by index, as a report that is also valid SQL.  
  `database, deprecated, file-formats, sqlite`
- **[SQLsmith](../drafts/brew/sqlsmith.md)**: A random SQL generator that reads a database's schema, fires nonsense-but-valid queries at it, and reports which ones crash the server.  
  `databases, fuzzing, postgresql, sql, sqlite, testing`
- **[SRecord](../drafts/brew/srecord.md)**: A set of command-line tools for converting, filtering, comparing and generating EPROM and firmware load files across Intel hex, Motorola S-Record and many other formats.  
  `cli, eprom, file-formats, firmware, retro`
- **[ssdeep](../drafts/brew/ssdeep.md)**: A hashing tool that scores how similar two files are instead of just whether they match, widely used in malware triage and forensics.  
  `forensics, hashing, malware, similarity`
- **[t1utils](../drafts/brew/t1utils.md)**: Six small tools that take a PostScript Type 1 font apart into editable text and put it back together, plus Mac font extraction.  
  `file-formats, fonts, postscript, reverse-engineering`
- **[t2sz](../drafts/brew/t2sz.md)**: Compresses a tar archive into a seekable zstd file, one frame per member, so a reader can pull out one file without unpacking the rest.  
  `compression, file-formats, seekable, tar, zstd`
- **[torf-cli](../drafts/brew/torf-cli.md)**: A command-line tool that builds, inspects, edits and verifies .torrent files, so you can see exactly what is inside the metadata of a swarm file.  
  `bittorrent, cli, file-formats, protocol, python, torrent`
- **[unshield](../drafts/brew/unshield.md)**: Unshield lists and extracts files from InstallShield cabinets, opening up a 1990s Windows installer format that was never officially documented.  
  `ancient, c, file-formats, installers, reverse-engineering`
- **[vgmstream](../drafts/brew/vgmstream.md)**: Decodes hundreds of proprietary video game audio formats, so streamed music and sound pulled from old game files plays or converts to .wav.  
  `audio, cli, decoder, game-audio, reverse-engineering`
- **[video-compare](../drafts/brew/video-compare.md)**: Plays two videos in sync under a draggable slider so you can see exactly what a codec, resize, or filter did to every frame.  
  `codecs, ffmpeg, gui, sdl2, video`
- **[Vineflower](../drafts/brew/vineflower.md)**: A Java decompiler that turns compiled JVM bytecode back into readable source, from a jar, a folder, or a single class file.  
  `bytecode, decompiler, java, jvm, reverse-engineering`
- **[vmtouch](../drafts/brew/vmtouch.md)**: vmtouch shows which pages of a file are sitting in the operating system's page cache, and lets you load, evict or lock them yourself.  
  `cli, filesystem, memory, page-cache, unix`
- **[vtable-dumper](../drafts/brew/vtable-dumper.md)**: Prints the C++ virtual tables inside a compiled shared library, showing the slot layout the compiler actually produced.  
  `abi, c++, elf, library, reverse-engineering`
- **[vttest](../drafts/brew/vttest.md)**: A decades-old interactive test suite that puts your terminal emulator through DEC VT100-and-later escape sequences, showing how 'compatible' it really is.  
  `ancient, escape-sequences, terminal, tui, vt100`
- **[weave](../drafts/brew/weave.md)**: A Git merge driver that parses files with tree-sitter and merges functions and classes instead of lines, so edits to different functions stop conflicting.  
  `ai-agents, git, merge, tree-sitter, version-control`
- **[weggli](../drafts/brew/weggli.md)**: A grep for C and C++ that matches code by structure, not text, so you can search for patterns like a memcpy into a stack buffer.  
  `c, code-search, cpp, rust, security, tree-sitter`
- **[wiggle](../drafts/brew/wiggle.md)**: Wiggle applies patches that GNU patch rejects, matching word by word instead of line by line so drifted context still lands.  
  `c, diff, merge, patch`
- **[wimlib](../drafts/brew/wimlib.md)**: Read, build, and modify Windows Imaging (WIM) archives from any OS, with content deduplicated by hash and compressed with Microsoft's own formats.  
  `archives, compression, deduplication, file-formats, wim, windows`
- **[witr](../drafts/brew/witr.md)**: witr answers "why is this running?" for a process, port, container or file by tracing it back through the chain of parents that started it.  
  `cli, debugging, linux, macos, processes, tui`
- **[xdelta3](../drafts/brew/xdelta.md)**: A binary diff tool that writes the smallest recipe for turning one file into another, using the VCDIFF standard (RFC 3284).  
  `binary, compression, diff, patching, vcdiff`
- **[xdotool](../drafts/brew/xdotool.md)**: Type, click, and rearrange windows on an X11 desktop from the shell, by sending synthetic input through the X server.  
  `automation, cli, input, windows, x11`
- **[xorriso](../drafts/brew/xorriso.md)**: A text-command tool for reading, building and editing ISO 9660 disc images, including bootable ones, session by session.  
  `boot, disc-images, file-formats, gnu, iso9660`
- **[YARA-X](../drafts/brew/yara-x.md)**: VirusTotal's Rust rewrite of YARA: write rules from text or byte patterns plus a condition, then see which files match.  
  `malware, pattern-matching, reverse-engineering, rust`
- **[zzuf](../drafts/brew/zzuf.md)**: A fuzzer that sits under any program and flips random bits in the data it reads, so you can watch software break on malformed input.  
  `fuzzing, reverse-engineering, security, testing`

## afternoon

- **[ACPICA](../drafts/brew/acpica.md)**: Intel's reference ACPI toolkit: dump your machine's firmware tables, disassemble the AML bytecode inside, and run it in a simulator.  
  `acpi, bytecode, disassembler, firmware, reverse-engineering`
- **[AFFLIB](../drafts/brew/afflib.md)**: A C library and toolkit for the Advanced Forensic Format, an open disk-image container that carries its own metadata, signatures and encryption.  
  `disk-images, file-formats, forensics, library`
- **[AFL++](../drafts/brew/afl++.md)**: A coverage-guided fuzzer that mutates seed inputs, watches which code paths they reach, and keeps the ones that find new ones, until something crashes.  
  `fuzzing, instrumentation, reverse-engineering, security`
- **[Alive2](../drafts/brew/alive2.md)**: Alive2 uses an SMT solver to check whether an LLVM optimization preserves a program's meaning, and hands back a concrete counterexample when it does not.  
  `compilers, formal-verification, llvm, optimization, smt, z3`
- **[ancient](../drafts/brew/ancient.md)**: A command-line decompressor for dead Amiga and Atari compression formats like ByteKiller, PowerPacker and Pack-Ice, rewritten cleanly and tested on about 10,000 real files.  
  `amiga, atari, compression, file-formats, retro, reverse-engineering`
- **[APKiD](../drafts/brew/apkid.md)**: PEiD for Android: point it at an APK and it reports which compilers, packers and obfuscators were used to build and wrap the app.  
  `android, python, reverse-engineering, yara`
- **[apktool](../drafts/brew/apktool.md)**: Takes a compiled Android app apart into readable resources and smali code, then rebuilds your edited folder back into a working APK.  
  `android, apk, java, reverse-engineering, smali`
- **[asar](../drafts/brew/asar.md)**: An assembler for the Super Nintendo's 65c816, SPC700 and Super FX chips, used to patch existing ROMs or build new ones from assembly source.  
  `assembly, retro, reverse-engineering, rom-hacking, snes`
- **[atari800](../drafts/brew/atari800.md)**: A free emulator of the Atari 400/800, XL/XE computers and the 5200 console that runs disk, cartridge, tape and program images.  
  `atari, emulator, retro, sdl, vintage-hardware`
- **[Augeas](../drafts/brew/augeas.md)**: Augeas parses config files into a tree and writes them back, so scripts edit structured data instead of patching text with sed.  
  `config, dsl, library, linux, parsing`
- **[AVFS](../drafts/brew/avfs.md)**: A virtual file system that lets ordinary programs open archives and remote locations as if they were directories, with no recompiling and no kernel changes.  
  `ancient, archives, filesystem, fuse`
- **[babl](../drafts/brew/babl.md)**: A C library that converts pixels between any two formats by assembling a chain of conversions at runtime, and the engine under GIMP's color handling.  
  `c, color, gimp, library, pixels`
- **[bao](../drafts/brew/bao.md)**: Encodes a file with its BLAKE3 hash tree so a reader can verify every byte as it streams in, or check just one slice.  
  `blake3, cryptography, hashing, protocol, rust, streaming`
- **[Bento4](../drafts/brew/bento4.md)**: A C++ MP4 toolkit whose mp4dump prints the full box tree of any MP4 file, so you can see how video containers are built.  
  `containers, dash, hls, mp4, reverse-engineering, video`
- **[binwalk](../drafts/brew/binwalk.md)**: Scans a binary blob such as a firmware image and lists the files, filesystems and compressed data hidden inside it.  
  `binary-analysis, entropy, firmware, reverse-engineering`
- **[BlastEm](../drafts/brew/blastem.md)**: A Sega Genesis emulator built to be both fast and accurate, tuned to run demanding demos and accuracy tests on modest old hardware.  
  `emulator, genesis, gui, retro, sega`
- **[blink](../drafts/brew/blink.md)**: A 221kb x86-64 Linux emulator for any POSIX host, with blinkenlights, a terminal debugger that animates memory as you step through assembly.  
  `cosmopolitan, debugger, emulator, reverse-engineering, tui, x86-64`
- **[Bochs](../drafts/brew/bochs.md)**: Bochs is a software emulator of an entire x86 PC, CPU, devices and BIOS included, built for accuracy over speed.  
  `bios, bootloader, emulation, reverse-engineering, x86`
- **[bubblewrap](../drafts/brew/bubblewrap.md)**: A small Linux tool that builds a container-like sandbox from kernel namespaces without root, so you can see how Flatpak-style isolation is assembled.  
  `containers, linux, namespaces, sandboxing`
- **[bulk_extractor](../drafts/brew/bulk_extractor.md)**: A forensics scanner that reads raw bytes, decodes anything that looks encoded or compressed, and pulls out emails, card numbers and images without parsing a file system.  
  `c++, carving, disk-images, forensics`
- **[cargo-mutants](../drafts/brew/cargo-mutants.md)**: Breaks your Rust code on purpose, one small change at a time, and reports which breakages your tests never noticed.  
  `cargo, mutation-testing, rust, testing`
- **[CBMC](../drafts/brew/cbmc.md)**: A bounded model checker for C and C++ that turns your program into a logic equation and searches for inputs that break your assertions.  
  `c, formal-methods, math, model-checking, verification`
- **[Chisel](../drafts/brew/chisel-ubuntu.md)**: Chisel carves Ubuntu's Debian packages into small slices, so you can build a root filesystem with only the files you need.  
  `containers, debian, go, packaging, ubuntu`
- **[Coccinelle](../drafts/brew/coccinelle.md)**: Coccinelle rewrites C code by matching its structure instead of its text, using semantic patches the Linux kernel community relies on for large API changes.  
  `c, linux-kernel, ocaml, refactoring, source-transformation`
- **[container2wasm](../drafts/brew/container2wasm.md)**: Converts a Linux container image into a single WebAssembly module that boots a real kernel on an emulated CPU, running under wasmtime or in a browser tab.  
  `browser, containers, docker, emulation, experimental, wasm`
- **[cpmtools](../drafts/brew/cpmtools.md)**: Command-line tools that list, copy, create and check files inside CP/M disk images, so 8-bit era floppies can be handled from a modern shell.  
  `cp/m, disk-images, file-systems, retro, z80`
- **[crcany](../drafts/brew/crcany.md)**: Computes and generates C code for any CRC from its parameters, showing the same checksum done bit by bit, byte by byte and word by word.  
  `algorithms, c, checksums, crc, math`
- **[C-Reduce](../drafts/brew/creduce.md)**: Give it a huge C or C++ file and a test script, and it shrinks the file to a tiny program that still does the same thing.  
  `c, c++, compilers, debugging, llvm, test-case-reduction`
- **[crosstool-NG](../drafts/brew/crosstool-ng.md)**: A menuconfig-driven generator that builds a complete cross-compiler toolchain (compiler, linker, C library) for a machine other than the one you're on.  
  `compiler, cross-compilation, embedded, toolchain, tui`
- **[Csmith](../drafts/brew/csmith.md)**: Csmith writes random C programs that avoid undefined behavior, so you can compile them with different compilers and treat any disagreement as a bug.  
  `c, compilers, fuzzing, generative, testing`
- **[cvs-fast-export](../drafts/brew/cvs-fast-export.md)**: Reads decades-old CVS or RCS history and rewrites it as a Git fast-import stream, rebuilding the changesets CVS never recorded.  
  `ancient, cvs, git, history, migration, version-control`
- **[dash-mpd-cli](../drafts/brew/dash-mpd-cli.md)**: Feed it a DASH manifest URL and it fetches the segments and muxes them into one local video file, exposing how adaptive streaming is assembled.  
  `dash, media, protocol, rust, streaming, video`
- **[DCMTK](../drafts/brew/dcmtk.md)**: About 80 command-line tools for reading, converting and sending DICOM, the file and network format behind medical imaging, from one long-running open toolkit.  
  `cli, dicom, file-formats, medical-imaging, protocol`
- **[der-ascii](../drafts/brew/der-ascii.md)**: Turns binary DER and BER into editable text and back again, so you can hand-craft ASN.1 structures, including deliberately broken ones, without counting bytes.  
  `asn1, ber, der, go, protocol, reverse-engineering, x509`
- **[diffoci](../drafts/brew/diffoci.md)**: A diff tool for Docker and OCI container images that compares them layer by layer, built to check whether a rebuilt image matches the official one.  
  `containers, diff, docker, oci, reproducible-builds`
- **[dislocker](../drafts/brew/dislocker.md)**: A FUSE driver that unlocks Windows BitLocker volumes on Linux, exposing the decrypted disk as a virtual NTFS file you can mount.  
  `bitlocker, encryption, filesystems, fuse, reverse-engineering`
- **[DOSBox-X](../drafts/brew/dosbox-x.md)**: A DOS emulator that aims past games: it emulates whole pre-2001 PCs, including PC-98 and Windows 9x guests, for preservation and testing.  
  `dos, emulator, gui, preservation, retro`
- **[dovi_convert](../drafts/brew/dovi_convert.md)**: Converts Dolby Vision Profile 7 MKV rips to Profile 8.1 without re-encoding, after scanning each file to decide whether that is safe.  
  `dolby-vision, hdr, mkv, remux, video`
- **[dovi_tool](../drafts/brew/dovi_tool.md)**: A command-line tool that reads, plots, edits and generates the hidden Dolby Vision metadata inside HEVC video streams.  
  `hdr, hevc, metadata, reverse-engineering, rust, video`
- **[DV Analyzer](../drafts/brew/dvanalyzer.md)**: Reads a DV video file frame by frame and reports the tape-transfer errors most capture tools never mention, from concealed video blocks to timecode jumps.  
  `dv, file-formats, needs-sample-files, preservation, video`
- **[dwarf](../drafts/brew/dwarf.md)**: A gdb-flavoured hex editor that understands ELF, PE and Mach-O headers as editable variables, so you can patch binaries at the structure level.  
  `binary, elf, hex-editor, mach-o, pe, reverse-engineering`
- **[DwarFS](../drafts/brew/dwarfs.md)**: A read-only compressed filesystem that packs a directory into one image, clusters similar files together, and mounts it instantly as a normal folder.  
  `archive, compression, deduplication, filesystem, fuse`
- **[dwarfutils](../drafts/brew/dwarfutils.md)**: dwarfdump prints the DWARF debug information inside compiled object files, showing how a compiler describes your program's types, functions and line numbers.  
  `compilers, debug-info, dwarf, elf, reverse-engineering`
- **[e2fsprogs](../drafts/brew/e2fsprogs.md)**: The reference toolkit for ext2, ext3 and ext4 filesystems, including debugfs and dumpe2fs for looking at on-disk structures directly.  
  `ancient, debugfs, ext4, file-formats, filesystems`
- **[ESBMC](../drafts/brew/esbmc.md)**: A model checker that turns C, C++ or Python code into SMT formulas and either proves assertions hold within a bound or hands back a concrete failing trace.  
  `bug-finding, c, formal-verification, model-checking, python, smt`
- **[FCEUX](../drafts/brew/fceux.md)**: An NES/Famicom emulator whose debugger tools let you watch 8-bit programs run, one instruction at a time.  
  `debugger, emulator, gui, nes, retro, reverse-engineering`
- **[Fernflower](../drafts/brew/fernflower.md)**: JetBrains' Java decompiler: feed it .class files or jars and it writes back readable Java source, with a renamer for obfuscated code.  
  `bytecode, decompiler, java, jetbrains, reverse-engineering`
- **[flashrom](../drafts/brew/flashrom.md)**: A command-line tool that identifies, reads, writes, verifies and erases the flash chips holding BIOS and firmware, on hundreds of boards and programmers.  
  `bios, firmware, needs-hardware, reverse-engineering, spi`
- **[FLIF](../drafts/brew/flif.md)**: A dead but fascinating lossless image format whose files can be cut off at any byte and still decode into a usable, lower-quality picture.  
  `compression, deprecated, file-format, image-format, lossless`
- **[fwup](../drafts/brew/fwup.md)**: fwup packs partitions, filesystems and update logic into one signed ZIP, then writes it to an SD card or image file. It shows how embedded devices update themselves.  
  `embedded, firmware, images, needs-hardware, updates`
- **[GammaRay](../drafts/brew/gammaray.md)**: A runtime inspector for Qt applications that lets you browse live objects, edit properties, and watch signals and state machines while the program runs.  
  `debugging, gui, introspection, qt, reverse-engineering`
- **[GEGL](../drafts/brew/gegl.md)**: The node-graph image engine under GIMP, with a command-line tool for chaining pixel operations into pipelines in floating point.  
  `gimp, image-processing, library, node-graph`
- **[gerbv](../drafts/brew/gerbv.md)**: A desktop viewer that draws the Gerber files PCB factories use, letting you see how a circuit board is described layer by layer.  
  `electronics, file-formats, gerber, gui, pcb, visual`
- **[Ghidra](../drafts/brew/ghidra.md)**: A reverse engineering framework from the NSA that disassembles and decompiles compiled programs across many processor architectures, with a GUI and scripting in Java or Python.  
  `decompiler, disassembler, gui, java, python, reverse-engineering`
- **[Ghostscript](../drafts/brew/ghostscript.md)**: A PostScript and PDF interpreter that renders, converts and compresses documents from one command, and runs PostScript as the programming language it is.  
  `converter, language, pdf, postscript, rendering`
- **[GmSSL](../drafts/brew/gmssl.md)**: A C crypto library and gmssl command-line tool implementing China's national cryptography standards (SM2, SM3, SM4, SM9, ZUC), a different crypto lineage from the usual AES and RSA.  
  `c, crypto, sm2, sm3, sm4, standards, tls`
- **[GoReSym](../drafts/brew/goresym.md)**: Reads a compiled Go binary, even a stripped one, and prints its function names, source paths, and types as JSON by pulling them out of Go's own runtime metadata.  
  `binary, go, reverse-engineering, symbols`
- **[gotestwaf](../drafts/brew/gotestwaf.md)**: Fires OWASP-style attack requests at a web application firewall or API gateway, then reports which ones were blocked and which slipped through.  
  `api, http, owasp, security, waf`
- **[gpsim](../drafts/brew/gpsim.md)**: A simulator for Microchip PIC microcontrollers that runs real firmware on a virtual chip with simulated pins, LEDs, switches and an LCD, debuggable like gdb.  
  `debugger, hardware, microcontroller, pic, simulation`
- **[Hatari](../drafts/brew/hatari.md)**: An Atari ST, STE, TT and Falcon emulator that copies the hardware closely enough to run old games and demo-scene tricks.  
  `atari, demoscene, emulator, hardware-emulation, retro`
- **[Hercules](../drafts/brew/hercules.md)**: A software emulator of IBM System/370, ESA/390 and z/Architecture mainframes, so you can boot period operating systems like MVS or VM on an ordinary computer.  
  `emulator, ibm, mainframe, operating-systems, retro`
- **[hfsutils](../drafts/brew/hfsutils.md)**: Command-line tools that read and write classic Macintosh HFS disks and image files from a modern shell, in the spirit of mtools for DOS floppies.  
  `ancient, filesystems, hfs, macintosh, retro, reverse-engineering`
- **[hivex](../drafts/brew/hivex.md)**: Reads Windows Registry hive files on any machine, with a shell, an XML exporter and a C library, built to survive malformed input.  
  `file-formats, forensics, library, reverse-engineering, windows-registry`
- **[ht (HT Editor)](../drafts/brew/ht.md)**: A terminal hex editor and disassembler that parses executable formats like ELF, PE and Mach-O, so you can browse a binary's structure and patch it in place.  
  `disassembler, hex-editor, reverse-engineering, tui`
- **[httm](../drafts/brew/httm.md)**: A fast command-line Time Machine that lists every unique past version of a file across ZFS, btrfs and other snapshots, and can restore any of them.  
  `backup, btrfs, rust, snapshots, tui, zfs`
- **[iccDEV](../drafts/brew/iccdev.md)**: The International Color Consortium's own toolkit for opening, validating, editing and applying ICC colour profiles, including the newer iccMAX model, from the command line.  
  `cli, colour, file-formats, icc, images`
- **[IceStorm](../drafts/brew/icestorm.md)**: Open-source tools and documentation for the Lattice iCE40 FPGA bitstream format, letting you pack, unpack and inspect the file that configures the chip.  
  `bitstream, fpga, needs-hardware, reverse-engineering`
- **[ipsw](../drafts/brew/ipsw.md)**: A single command-line tool for downloading, unpacking and picking apart Apple firmware: dyld caches, kernelcaches, Mach-O binaries and more.  
  `apple, firmware, ios, macos, needs-hardware, reverse-engineering`
- **[Jasmin](../drafts/brew/jasmin.md)**: Jasmin is an assembler for the JVM: you write bytecode mnemonics by hand and it emits a real .class file Java can run.  
  `assembler, bytecode, java, jvm, old`
- **[Joern](../drafts/brew/joern.md)**: Joern turns source code, bytecode and binaries into a queryable code property graph, so you can hunt bugs by asking questions of a program.  
  `graph, jvm, reverse-engineering, scala, security, static-analysis`
- **[Kaitai Struct](../drafts/brew/kaitai-struct-compiler.md)**: Describe a binary file format once in a YAML file, and the compiler generates a parser for it in a dozen languages.  
  `binary-formats, file-formats, java, parser-generator, reverse-engineering`
- **[keyd](../drafts/brew/keyd.md)**: A Linux daemon that remaps keys below the display server, bringing QMK-style layers and tap/hold keys to any keyboard with a short config file.  
  `daemon, evdev, keyboard, linux, remapping, uinput`
- **[KLEE](../drafts/brew/klee.md)**: KLEE runs programs with unknown inputs instead of fixed ones, then works out concrete inputs that reach each path through the code.  
  `llvm, research, symbolic-execution, testing`
- **[ldid](../drafts/brew/ldid.md)**: A small tool that signs Mach-O binaries and dumps their entitlements, showing how Apple's code signing works at the level of raw signature blocks.  
  `code-signing, entitlements, ios, mach-o, macos, reverse-engineering`
- **[libaacs](../drafts/brew/libaacs.md)**: An open-source library implementing the AACS copy protection scheme used on Blu-ray discs, published as a research project for understanding how DRM and its crypto fit together.  
  `blu-ray, crypto, drm, library, reverse-engineering`
- **[libcaption](../drafts/brew/libcaption.md)**: A small C library that writes and reads CEA-608 and CEA-708 closed captions, the hidden caption data riding inside broadcast video.  
  `c, closed-captions, h264, library, protocol, video`
- **[libdsk](../drafts/brew/libdsk.md)**: A C library and set of utilities that read, convert and write floppy disc images across dozens of obscure formats, from CP/M and Amstrad to Commodore 64.  
  `cp/m, disk-images, file-formats, floppy, library, retrocomputing`
- **[libesedb](../drafts/brew/libesedb.md)**: A C library and two tools for opening ESE database files, the proprietary Microsoft format behind Active Directory, Exchange and Windows Search.  
  `file-formats, forensics, library, reverse-engineering, windows`
- **[libewf](../drafts/brew/libewf.md)**: An open library and set of tools for reading, writing and verifying Expert Witness forensic disk images, the container format behind EnCase evidence files.  
  `c, disk-images, file-formats, forensics, library`
- **[libforensic1394](../drafts/brew/libforensic1394.md)**: A C library with Python bindings that reads a running machine's physical memory over FireWire, using DMA, with nothing installed on the target.  
  `dma, firewire, memory-forensics, needs-hardware, protocol, reverse-engineering`
- **[libgig](../drafts/brew/libgig.md)**: A C++ library and a drawer of command-line tools for opening, dumping, converting and extracting samples from Gigasampler, DLS, SoundFont, KORG and AKAI sampler files.  
  `audio, file-formats, library, samplers, soundfont`
- **[liblcf](../drafts/brew/liblcf.md)**: A library and two small tools that turn RPG Maker 2000/2003 binary game data into XML and back, and pull out every string.  
  `easyrpg, file-formats, library, reverse-engineering, rpg-maker, xml`
- **[liblqr](../drafts/brew/liblqr.md)**: A C/C++ library for seam carving, the content-aware resizing trick that shrinks a picture by quietly removing paths of boring pixels.  
  `c, images, library, seam-carving`
- **[LibreDWG](../drafts/brew/libredwg.md)**: A free C library and set of command-line tools that read and write AutoCAD's proprietary DWG format, converting it to DXF, JSON and SVG.  
  `cad, dwg, file-formats, gnu, library, reverse-engineering`
- **[LIEF](../drafts/brew/lief.md)**: A library that parses, edits and rewrites ELF, PE and Mach-O executables through one API in C++, Python or Rust.  
  `elf, library, mach-o, pe, python, reverse-engineering`
- **[GNU lightning](../drafts/brew/lightning.md)**: A GNU library that emits native machine code at run-time from one RISC-style instruction set, so a JIT does not need a code generator per CPU.  
  `assembly, compilers, gnu, jit, library`
- **[Limine](../drafts/brew/limine.md)**: A bootloader for x86, ARM and RISC-V machines, and a readable way into what happens between power-on and the first line of a kernel.  
  `bios, bootloader, osdev, secure-boot, uefi`
- **[lziprecover](../drafts/brew/lziprecover.md)**: Repairs damaged lzip archives by using the format's built-in redundancy, and can rebuild one good file from several broken copies.  
  `compression, data-recovery, error-correction, file-formats, lzip`
- **[mcap](../drafts/brew/mcap.md)**: A command-line tool for MCAP, the self-describing container format that robots use to record timestamped sensor and message streams into one file.  
  `binary, file-format, logging, robotics, ros`
- **[mdbtools](../drafts/brew/mdbtools.md)**: A set of command-line tools that read Microsoft Access database files on Unix, turning a proprietary binary format into tables, CSV and JSON.  
  `access, databases, file-formats, reverse-engineering`
- **[mdk](../drafts/brew/mdk.md)**: An emulator, assembler and debugger for MIX, the imaginary computer from Knuth's The Art of Computer Programming, so you can step through its assembly.  
  `ancient, assembly, education, emulator, knuth, scheme`
- **[MediaConch](../drafts/brew/mediaconch.md)**: A conformance checker for archival video and audio files that tells you whether a Matroska, FFV1 or LPCM file really follows its spec.  
  `audio, ffv1, file-formats, matroska, preservation, video`
- **[minidjvu](../drafts/brew/minidjvu.md)**: A small encoder and decoder for the black-and-white layer of DjVu, which squeezes scanned pages by reusing shared letter shapes across a whole document.  
  `ancient, compression, djvu, file-format, scanned-documents`
- **[MLT](../drafts/brew/mlt.md)**: The multitrack video engine behind Shotcut, Kdenlive and Flowblade, with a melt command that plays and renders compositions described in XML.  
  `audio, cli, ffmpeg, video, xml`
- **[MMIX](../drafts/brew/mmix.md)**: Donald Knuth's 64-bit RISC teaching computer, with an assembler and simulator, so you can write and run assembly for a machine that never existed.  
  `architecture, assembly, knuth, risc, simulator, teaching`
- **[mp4ff](../drafts/brew/mp4ff.md)**: A Go library and nine command-line tools that print the box tree inside MP4 files and rewrite, crop, encrypt or decrypt them.  
  `file-formats, go, library, mp4, streaming, video`
- **[nDPI](../drafts/brew/ndpi.md)**: An open source C library that works out which application protocol a network flow belongs to by looking at the traffic itself, not the port number.  
  `c, dpi, library, network, protocol`
- **[ntfs2btrfs](../drafts/brew/ntfs2btrfs.md)**: Converts an NTFS volume into Btrfs on the same disk, with no copy-off and restore, and keeps the original as a reflink image you can roll back to.  
  `btrfs, filesystems, ntfs, risky, storage`
- **[Oclgrind](../drafts/brew/oclgrind.md)**: A virtual OpenCL device that runs GPU kernels in a bounds-checking interpreter, catching memory errors, data races and barrier bugs a real device would ignore.  
  `debugger, gpu, llvm, opencl, simulator`
- **[oggz](../drafts/brew/oggz.md)**: A command-line toolkit for looking inside Ogg files: dump packets, validate streams, cut by time, and merge or sort logical bitstreams.  
  `audio, cli, containers, file-formats, ogg`
- **[Open SIMH](../drafts/brew/open-simh.md)**: A family of simulators that boot historic computers like the PDP-8, PDP-11 and VAX in software, so their original operating systems run unchanged.  
  `emulation, history, pdp-11, simulation, unix, vax, vintage`
- **[openMSX](../drafts/brew/openmsx.md)**: An emulator for the MSX, a 1980s home computer standard, built to be accurate down to chip timing, with a debugger and Tcl scripting.  
  `debugger, emulator, gui, msx, retro, tcl`
- **[PacketQ](../drafts/brew/packetq.md)**: Run SQL queries straight against PCAP files, so a packet capture becomes a table you can group, sort and count without a database.  
  `dns, network, pcap, protocol, sql`
- **[Packetry](../drafts/brew/packetry.md)**: A Rust and GTK 4 USB 2.0 protocol analyser that shows traffic captured by Cynthion hardware, or read from a saved .pcap file.  
  `gui, needs-hardware, pcap, protocol, rust, usb`
- **[pdfalyzer](../drafts/brew/pdfalyzer.md)**: Draws a PDF's hidden object tree in colour and scans its embedded streams with YARA, without ever executing the file's content.  
  `forensics, pdf, python, reverse-engineering, visual, yara`
- **[Peekaboo](../drafts/brew/peekaboo.md)**: A macOS command-line tool that reads any app's accessibility tree as a list of clickable element IDs, then clicks and types against them.  
  `accessibility, automation, gui, macos, mcp`
- **[pkcs11-tools](../drafts/brew/pkcs11-tools.md)**: Unix-style ls, cat, mv, rm and od for the keys inside hardware security modules and software tokens, so you can see what a PKCS#11 token holds.  
  `cryptography, hsm, keys, needs-hardware-optional, pkcs11`
- **[GNU poke](../drafts/brew/poke.md)**: An interactive editor where you describe a binary format in a small language, then map it onto a file and edit its fields as typed values.  
  `binary-formats, editor, language, reverse-engineering`
- **[pwntools](../drafts/brew/pwntools.md)**: A Python library and 19 command-line tools for writing exploits and poking at binaries, built for capture-the-flag competitions.  
  `ctf, exploitation, library, python, reverse-engineering`
- **[radare2](../drafts/brew/radare2.md)**: A command-line reverse engineering framework that disassembles, patches, debugs and scripts binaries, firmware and live processes from a terse shell.  
  `binary-analysis, debugger, disassembler, reverse-engineering, tui`
- **[ratarmount](../drafts/brew/ratarmount.md)**: Mounts tar, zip, rar, 7z and other archives as read-only filesystems, using a SQLite index to jump straight to any file without extracting.  
  `archives, filesystem, fuse, python, sqlite`
- **[redress](../drafts/brew/redress.md)**: Redress rebuilds package names, types, and approximate source layout from stripped Go binaries, so you can read compiled Go programs and malware samples.  
  `binary-analysis, go, radare2, reverse-engineering`
- **[regipy](../drafts/brew/regipy.md)**: Parses offline Windows registry hive files from the command line, dumping them to JSON, diffing them, and running forensic plugins without needing Windows.  
  `file-formats, forensics, python, registry, windows`
- **[remake](../drafts/brew/remake.md)**: A patched GNU Make with tracing, target listing, profiling and an actual debugger, so you can watch a build run and see why.  
  `build-systems, debugger, make, profiling, tracing`
- **[reposurgeon](../drafts/brew/reposurgeon.md)**: A debugger-style tool that reads a repository's history, lets you rewrite it, and writes it back out, including into a different version-control system.  
  `cli, conversion, git, history, version-control`
- **[RetDec](../drafts/brew/retdec.md)**: A decompiler from Avast that turns compiled executables for many architectures and file formats back into readable C, a hands-on way into reverse engineering.  
  `binaries, decompiler, llvm, reverse-engineering`
- **[Rizin](../drafts/brew/rizin.md)**: A Unix-style reverse engineering toolkit: open a binary, firmware image or running program and read its disassembly from an interactive shell.  
  `binary-analysis, disassembler, reverse-engineering, tui`
- **[RVVM](../drafts/brew/rvvm.md)**: A RISC-V emulator with a tracing JIT that boots real operating systems like Linux, Haiku and the BSDs in a window, from one small binary.  
  `emulator, jit, operating-systems, risc-v, virtual-machine`
- **[save3ds_fuse](../drafts/brew/save3ds_fuse.md)**: Mounts Nintendo 3DS save data, extdata and title databases as an ordinary folder you can browse and edit, then writes changes back on unmount.  
  `3ds, filesystem, fuse, needs-hardware, reverse-engineering, rust`
- **[scummvm-tools](../drafts/brew/scummvm-tools.md)**: About 44 utilities that unpack, convert and decompile the data files of classic adventure games, a hands-on way into how old games stored their assets.  
  `adventure-games, decompiler, game-formats, reverse-engineering, scummvm`
- **[SDCC](../drafts/brew/sdcc.md)**: A C compiler for tiny chips like the 8051, Z80, STM8 and 6502, bundled with assemblers, a debugger and simulators so you can run the result without hardware.  
  `8051, c, compiler, microcontrollers, retro, simulator, z80`
- **[sq (Sequoia-PGP)](../drafts/brew/sequoia-sq.md)**: A Rust OpenPGP command-line tool that encrypts, signs and verifies, and can inspect keys and messages as of any past date.  
  `cli, crypto, openpgp, pgp, protocol, rust`
- **[The Sleuth Kit](../drafts/brew/sleuthkit.md)**: A set of small command-line tools that take a raw disk image apart layer by layer, showing partitions, file names, inodes, and deleted files.  
  `cli, disk-images, file-systems, forensics, reverse-engineering`
- **[Sparse](../drafts/brew/sparse.md)**: Linus Torvalds's semantic C checker, which uses annotations in ordinary C to catch mixups like kernel pointers passed where user-space pointers belong.  
  `c, linux-kernel, parsers, static-analysis`
- **[SPIM](../drafts/brew/spim.md)**: A MIPS32 simulator that runs assembly source in your terminal, so you can step through how a simple processor executes code.  
  `assembly, cpu, mips, old, simulator, teaching`
- **[Splint](../drafts/brew/splint.md)**: A C static checker from the 2000s that works as a better lint, and checks harder if you annotate your source with extra specifications.  
  `c, history, lint, security, static-analysis`
- **[SQLancer](../drafts/brew/sqlancer.md)**: Fuzzes database engines like SQLite, DuckDB and PostgreSQL with generated queries, and uses clever oracles to catch cases where the database silently returns the wrong rows.  
  `databases, fuzzing, java, science, testing`
- **[sse2neon](../drafts/brew/sse2neon.md)**: A single C header that lets x86 SSE intrinsic code compile on Arm by re-implementing each SSE call with NEON, showing how SIMD maps across architectures.  
  `arm, c, header-only, intrinsics, neon, simd, sse`
- **[swftools](../drafts/brew/swftools.md)**: A set of command-line tools that take apart, rebuild and generate Adobe Flash SWF files, a good way to look inside a dead binary format.  
  `binary, file-formats, flash, reverse-engineering`
- **[swift-section](../drafts/brew/swift-section.md)**: Reads a compiled Mach-O binary and prints the Swift types, protocols, and field layouts inside it, without running the binary.  
  `mach-o, macos, reverse-engineering, swift`
- **[sysdig](../drafts/brew/sysdig.md)**: Sysdig records Linux system calls and shows what every process and container is doing, like strace, tcpdump, htop and lsof in one tool.  
  `containers, linux, syscalls, tracing, troubleshooting`
- **[TestDisk](../drafts/brew/testdisk.md)**: A terminal tool that reads a disk's raw partition tables and backup boot sectors to rebuild lost partitions, with PhotoRec to carve files from wrecks.  
  `data-recovery, filesystems, forensics, partitions, tui`
- **[Topiary](../drafts/brew/topiary.md)**: A code formatter engine from Tweag, built on Tree-sitter, where a language's style is written in a small DSL instead of a hand-built formatter.  
  `formatter, language-tools, parsing, rust, tree-sitter`
- **[Tracy](../drafts/brew/tracy.md)**: A nanosecond-resolution profiler that streams timing data from a running program into a live viewer, covering CPU, GPU, memory, locks and context switches.  
  `gamedev, gpu, gui, performance, profiler, telemetry`
- **[TSDuck](../drafts/brew/tsduck.md)**: A toolbox of small command-line tools for taking apart MPEG transport streams, the container that carries digital TV, from live broadcasts or recorded files.  
  `broadcast, cli, dvb, mpeg-ts, protocol, streaming`
- **[u-boot-tools](../drafts/brew/u-boot-tools.md)**: Host-side utilities from the U-Boot boot loader project, for working with the image and environment files that small devices boot from.  
  `bootloader, embedded, firmware, needs-hardware, reverse-engineering`
- **[uCON64](../drafts/brew/ucon64.md)**: A command-line Swiss Army knife for video game ROM dumps: it identifies, patches, converts and checks cartridge files from dozens of old consoles.  
  `cli, emulation, file-formats, retro, reverse-engineering, rom`
- **[uftrace](../drafts/brew/uftrace.md)**: uftrace records every function call a C, C++ or Rust program makes and prints it as an indented call tree with a duration on each line.  
  `c, cpp, linux, profiling, rust, tracing, tui`
- **[Unicorn](../drafts/brew/unicorn.md)**: A CPU emulator library: hand it machine code for ARM, MIPS, x86 and more, and run it in isolation while hooks watch every step.  
  `cpu, emulation, library, qemu, reverse-engineering`
- **[vc4asm](../drafts/brew/vc4asm.md)**: An assembler and disassembler for the Raspberry Pi's VideoCore IV GPU, a barely documented processor you can write machine code for yourself.  
  `assembler, disassembler, gpu, hardware, raspberry-pi, reverse-engineering`
- **[veraPDF](../drafts/brew/verapdf.md)**: A validator that checks PDF files against the PDF/A archival and PDF/UA accessibility standards, and reports exactly which structural rules a file breaks.  
  `archival, file-formats, java, pdf, validation`
- **[Verovio](../drafts/brew/verovio.md)**: Turns machine-readable music scores (MEI, MusicXML, ABC, Humdrum and more) into SVG sheet music from one command.  
  `abc, library, mei, music, musicxml, notation, svg`
- **[VICE](../drafts/brew/vice.md)**: A family of emulators for Commodore's 8-bit computers, from the C64 to the PET, with tools for disk images, cartridges and SID music.  
  `commodore, emulator, gui, retro, sid`
- **[vvdec](../drafts/brew/vvdec.md)**: Fraunhofer's open-source H.266/VVC video decoder: feed it a raw next-generation bitstream and get plain YUV frames back, with a library underneath.  
  `codec, h266, library, video, vvc, wasm`
- **[wabt](../drafts/brew/wabt.md)**: A suite of command-line tools that turns WebAssembly binaries into readable text and back, with byte-exact round-trips, so you can see what a .wasm file contains.  
  `binary-format, compiler-toolchain, disassembler, reverse-engineering, webassembly`
- **[wasm-tools](../drafts/brew/wasm-tools.md)**: A single Rust binary that validates, prints, parses, mutates and generates WebAssembly, so you can read a .wasm file as text and rebuild it.  
  `binary-formats, reverse-engineering, rust, wasm, webassembly`
- **[wasm3](../drafts/brew/wasm3.md)**: A WebAssembly interpreter in C, small enough for microcontrollers, that runs portable bytecode directly instead of compiling it to native code.  
  `c, embedded, interpreter, virtual-machine, webassembly`
- **[wllvm](../drafts/brew/wllvm.md)**: Compiler wrappers that build an ordinary C or C++ project as usual, then hand you the whole program as one LLVM bitcode file for analysis.  
  `bitcode, compilers, llvm, python, static-analysis`
- **[WuppieFuzz](../drafts/brew/wuppiefuzz.md)**: A coverage-guided fuzzer that reads an OpenAPI spec and mutates HTTP requests against a running service, using feedback to find where the API breaks.  
  `fuzzing, libafl, openapi, rest, rust, security`
- **[Xbyak](../drafts/brew/xbyak.md)**: A header-only C++ library that turns method calls like mov(eax, x) into x86 machine code in memory, then lets you call it as a function.  
  `assembler, c++, jit, library, x86`
- **[xmount](../drafts/brew/xmount.md)**: Presents a forensic or virtual disk image as a different image format through a FUSE mount, so you can boot or inspect it without converting a copy.  
  `disk-images, forensics, fuse, virtualization`
- **[XRoar](../drafts/brew/xroar.md)**: An emulator for the Dragon 32/64 and Tandy Colour Computers, with a GDB stub for stepping through 6809 machine code.  
  `6809, 8-bit, debugging, emulator, retro`
- **[YARA](../drafts/brew/yara.md)**: A small rule language for describing files by their strings and a boolean condition, then scanning anything to see which rules match.  
  `malware, pattern-matching, reverse-engineering, security`
- **[yaze-ag](../drafts/brew/yaze-ag.md)**: A Z80 CPU emulator that boots real CP/M 2.2 and 3.1 in your terminal, with undocumented opcodes and adjustable clock speed.  
  `8-bit, cp/m, emulator, retro, z80`
- **[z80dasm](../drafts/brew/z80dasm.md)**: A disassembler for the Zilog Z80 that turns ROM dumps from 1980s micros into assembly source you can reassemble byte for byte.  
  `assembly, disassembler, retro, reverse-engineering, rom, z80`
- **[Zeek](../drafts/brew/zeek.md)**: Zeek watches network traffic and turns it into structured logs of what every protocol conversation did, steered by its own scripting language.  
  `network, protocol, scripting, security`
- **[zpaq](../drafts/brew/zpaq.md)**: A journaling command-line archiver that keeps every version of your files and compresses with a context-mixing model you can reconfigure.  
  `archiver, cli, compression, journaling`

## days-off

- **[Project Trellis](../drafts/brew/prjtrellis.md)**: Open documentation and tools for the bitstream format of Lattice ECP5 FPGAs, reverse-engineered by correlating thousands of vendor-generated designs.  
  `bitstream, fpga, needs-hardware, reverse-engineering, yosys`
