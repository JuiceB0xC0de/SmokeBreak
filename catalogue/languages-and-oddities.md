# Languages and unusual utilities

Esoteric or unusual languages, databases with a twist, old-school environments, one-of-a-kind utilities that fit nowhere else.

236 entries. [Back to the shelf](README.md)

## quick

- **[abnfgen](../drafts/brew/abnfgen.md)**: Feed it a grammar written in ABNF and it prints random documents that match, a quick way to see a grammar run backwards and to fuzz parsers.  
  `abnf, fuzzing, grammar, parsers, testing`
- **[Amfora](../drafts/brew/amfora.md)**: A terminal browser for Gemini, a small text-first protocol that sits beside the Web, with tabs, bookmarks, feeds and certificate handling.  
  `browser, gemini, go, protocol, tui`
- **[bas55](../drafts/brew/bas55.md)**: A small interpreter for ECMA-55 Minimal BASIC, the 1978 standard, tested against the US National Bureau of Standards conformance programs.  
  `basic, ecma-55, interpreter, language, retro`
- **[Befunge-93](../drafts/brew/befunge93.md)**: A 1993 esoteric language where code is a grid, the instruction pointer moves in any of four directions, and programs can rewrite themselves.  
  `1993, 2d, esoteric, language, self-modifying`
- **[bioawk](../drafts/brew/bioawk.md)**: Brian Kernighan's awk taught to read FASTA, FASTQ, SAM, VCF, BED and GFF, so genome files can be queried by column name in one-liners.  
  `awk, bioinformatics, genomics, language, text-processing`
- **[bttf](../drafts/brew/bttf.md)**: A Rust datetime tool that formats, shifts and converts times, and can find timestamps in any text and rewrite them in place.  
  `datetime, rust, text-filter, unix-pipes`
- **[calc](../drafts/brew/calc.md)**: An arbitrary-precision calculator with its own C-like language, exact fractions, and a lineage tied to hunting huge prime numbers.  
  `ancient, arbitrary-precision, language, math, primes`
- **[cbmbasic](../drafts/brew/cbmbasic.md)**: Commodore 64 BASIC V2 reimplemented in native C, so you can type line numbers at a prompt or run BASIC files as Unix scripts.  
  `basic, commodore, language, retro, scripting`
- **[cdb](../drafts/brew/cdb.md)**: D. J. Bernstein's constant database: a read-only key/value file built once, rewritten whole, and looked up in one or two disk accesses.  
  `c, database, djb, file-format, key-value`
- **[cdecl](../drafts/brew/cdecl.md)**: Turns English like "pointer to const pointer to const char" into a C or C++ declaration, and explains declarations back in English.  
  `c, c++, declarations, old-school, parsing, preprocessor`
- **[Chawan](../drafts/brew/chawan.md)**: A terminal web browser with its own from-scratch engine that renders CSS, inline images and optional JavaScript, and also reads Gopher, Gemini and man pages.  
  `browser, gemini, gopher, nim, terminal, tui`
- **[clac](../drafts/brew/clac.md)**: A postfix stack calculator that redraws the whole stack on every keystroke, so you watch Forth-style arithmetic happen instead of just getting an answer.  
  `calculator, forth, postfix, rpn, stack`
- **[cling](../drafts/brew/cling.md)**: An interactive C++ interpreter from the ROOT project at CERN, built on Clang and LLVM, that lets you type C++ at a prompt and run it immediately.  
  `c++, clang, interpreter, jupyter, llvm, repl`
- **[cmigemo](../drafts/brew/cmigemo.md)**: Turns a romaji query like 'ai' into a regex matching 愛, 相, 藍 and 合, so ordinary search tools can find Japanese text typed in Latin letters.  
  `emacs, japanese, library, regex, search, vim`
- **[cppp](../drafts/brew/cppp.md)**: A partial C preprocessor that resolves only the #ifdef-style conditionals you name and leaves everything else untouched, for cleaning old code.  
  `c, cli, legacy-code, preprocessor`
- **[cxgo](../drafts/brew/cxgo.md)**: A C-to-Go source translator that parses C in pure Go and tries to emit readable, idiomatic Go rather than just code that compiles.  
  `c, compilers, go, transpiler`
- **[Cyphernetes](../drafts/brew/cyphernetes.md)**: A Cypher-style graph query language for Kubernetes: write MATCH and WHERE statements against cluster resources instead of chaining kubectl, xargs and bash.  
  `graph, kubernetes, language, query-language`
- **[d2](../drafts/brew/d2.md)**: D2 is a small declarative language that turns a few lines of text into a rendered diagram, with live reload and a hand-drawn sketch mode.  
  `diagrams, go, language, visual`
- **[dpic](../drafts/brew/dpic.md)**: dpic compiles pic, a small text language for describing diagrams, into SVG, PDF, PostScript, LaTeX or xfig drawings.  
  `ancient, diagrams, language, latex, svg`
- **[eg (Expert Guide)](../drafts/brew/eg.md)**: A terminal reader for Norton Guide, the compiled hypertext help format from 1990s DOS programming tools, so old help files can be read on Linux.  
  `ancient, dos, help-files, hypertext, tui`
- **[etsh](../drafts/brew/etsh.md)**: Ports of the 1975 Sixth Edition UNIX Thompson shell that run as ordinary interactive shells, so you can type at the ancestor of sh.  
  `ancient, shell, unix-history, v6`
- **[Fennel](../drafts/brew/fennel.md)**: A Lisp with macros that compiles to plain Lua, so it runs anywhere Lua does, with a REPL and a single-file compiler you can embed.  
  `compiler, language, lisp, lua, macros, repl`
- **[fpart](../drafts/brew/fpart.md)**: Crawls a file tree and sorts it into similar-sized bags, as lists of file names, so huge copies can be split and run in parallel.  
  `backup, bin-packing, c, cli, migration, rsync`
- **[glulxe](../drafts/brew/glulxe.md)**: The reference interpreter for Glulx, a 32-bit virtual machine for interactive fiction games, and a way to run text adventures built on a documented spec.  
  `glulx, interactive-fiction, old-school, text-adventure, virtual-machine, z-machine`
- **[GNU Units](../drafts/brew/gnu-units.md)**: A unit converter that treats units as algebra, tracking dimensions through whole expressions, with a big editable text file of odd units and constants behind it.  
  `calculator, cli, math, units`
- **[GitQL](../drafts/brew/gql.md)**: Write SQL-like queries against a git repository's commits, branches, tags and diffs, with no import step and no database file.  
  `git, query-language, rust, sql`
- **[GraphQLite](../drafts/brew/graphqlite.md)**: A SQLite extension that lets you write Cypher graph queries and run graph algorithms like PageRank inside an ordinary .db file, with no server.  
  `cypher, database, extension, graph, sqlite`
- **[Hy](../drafts/brew/hy.md)**: A Lisp that compiles to Python's own syntax tree, so you can write parentheses and still call any Python library.  
  `language, lisp, macros, python, repl`
- **[idsgrep](../drafts/brew/idsgrep.md)**: Grep for Han characters by shape: ask for every character with 月 on the right and get 明, 朝 and 期 back.  
  `cjk, kanji, language, search, unicode`
- **[Jim Tcl](../drafts/brew/jimtcl.md)**: A from-scratch Tcl interpreter in about 14k lines of C, small enough to embed inside another program as its scripting language.  
  `c, embeddable, interpreter, language, tcl`
- **[le](../drafts/brew/le.md)**: A small console text editor with rectangular block selection, a hex mode, and binary-clean editing, modelled loosely on Norton Editor for DOS.  
  `editor, hex, old-school, tui`
- **[LOLCODE](../drafts/brew/lolcode.md)**: An esoteric programming language written in lolspeak, with lci, a real interpreter that includes a bytecode VM, a JIT, and even a small language model library.  
  `esoteric, interpreter, jit, language`
- **[m4](../drafts/brew/m4.md)**: The classic Unix macro processor: it copies text through and expands macros as it goes, and it quietly sits under GNU Autoconf.  
  `ancient, gnu, language, macros, unix`
- **[malbolge](../drafts/brew/malbolge.md)**: An interpreter for Malbolge, an esoteric language built to be nearly impossible to program, shipped with a working cat and a 99 Bottles program.  
  `ancient, esoteric, language`
- **[mdsh](../drafts/brew/mdsh.md)**: mdsh reruns shell commands embedded in a Markdown file and rewrites the results in place, so README examples never drift from reality.  
  `ci, documentation, markdown, rust, shell`
- **[Metashell](../drafts/brew/metashell.md)**: An interactive shell for C++ template metaprogramming: type compile-time code at a prompt and see what Clang makes of it, no source file needed.  
  `clang, cpp, metaprogramming, repl, templates`
- **[min](../drafts/brew/min-lang.md)**: A small concatenative language with a REPL, where programs are words and quoted blocks acting on a stack, shipped as one binary.  
  `concatenative, language, nim, repl, stack`
- **[moreutils](../drafts/brew/moreutils.md)**: Fifteen small Unix tools that fill gaps in the shell, like sponge, ts and vidir, which you will want in your pipelines once you know they exist.  
  `cli, pipelines, shell, unix`
- **[neatvi](../drafts/brew/neatvi.md)**: A small vi/ex clone written in C, built to edit text that mixes right-to-left scripts like Farsi or Arabic with left-to-right text.  
  `bidi, c, editor, tui, utf-8, vi`
- **[nesC](../drafts/brew/nesc.md)**: nesC is a C dialect that builds TinyOS's event-driven, component-wiring model into the language, for sensor nodes with a few hundred bytes of RAM.  
  `c, deprecated, embedded, language, tinyos`
- **[newLISP](../drafts/brew/newlisp.md)**: A small Lisp-like scripting language with its own quirks, installed as a single binary with a readline prompt and a doc generator.  
  `ancient, language, lisp, scripting`
- **[nkf](../drafts/brew/nkf.md)**: A small Unix filter that converts Japanese text between encodings like Shift_JIS, EUC-JP, ISO-2022-JP and UTF-8, and guesses the input encoding so you never have to declare it.  
  `encoding, history, japanese, unix-filter`
- **[picoc](../drafts/brew/picoc.md)**: A very small C interpreter that runs C source directly, with no separate compile step, so C works a bit like a scripting language.  
  `c, interpreter, language`
- **[Planck](../drafts/brew/planck.md)**: A ClojureScript REPL that starts instantly with no JVM, so Clojure-flavoured scripting works from the shell like a quick scripting language.  
  `clojurescript, deprecated, javascriptcore, repl, scripting`
- **[prqlc](../drafts/brew/prqlc.md)**: A compiler for PRQL, a pipelined query language where each line transforms the previous one, and the output is plain SQL for your database.  
  `compiler, data, language, rust, sql`
- **[QuickJS](../drafts/brew/quickjs.md)**: A complete JavaScript engine in a few C files, small enough to embed anywhere, that can also compile scripts into standalone executables.  
  `c, compiler, embeddable, interpreter, javascript`
- **[ratfor](../drafts/brew/ratfor.md)**: A preprocessor that turns Rational Fortran, Fortran with structured control flow, into plain FORTRAN 77, a working piece of the Software Tools era.  
  `ancient, fortran, language, preprocessor`
- **[Redka](../drafts/brew/redka.md)**: Redis reimplemented on top of SQLite or PostgreSQL, speaking the Redis wire protocol so existing clients work while your data sits in ordinary SQL tables.  
  `database, go, postgresql, redis, sqlite`
- **[regldg](../drafts/brew/regldg.md)**: Runs regular expressions backwards: give it a pattern and it prints every string that matches, turning a regex into a word list.  
  `grammar, language, regex, wordlist`
- **[rgxg](../drafts/brew/rgxg.md)**: Writes the regular expression for you: give it a numeric range or a CIDR block and it prints a pattern matching exactly that set.  
  `c-library, cidr, generator, regex`
- **[scriptisto](../drafts/brew/scriptisto.md)**: A shebang interpreter that lets you run single-file scripts in compiled languages like C, Rust, Go or COBOL, building and caching the binary on first run.  
  `cli, compiled-languages, scripting, shebang`
- **[snow](../drafts/brew/snow.md)**: Hides a message in the invisible spaces and tabs at the ends of lines of ordinary text, with optional encryption on top.  
  `encryption, steganography, text, whitespace`
- **[srgn](../drafts/brew/srgn.md)**: A grep-like tool that understands source code grammar, so you can search and rewrite only the docstrings, comments, or struct definitions you mean.  
  `cli, grep, refactoring, rust, tree-sitter`
- **[twtxt](../drafts/brew/twtxt.md)**: A microblogging format where your account is one plain text file at a URL, and the client merges the files you follow into a timeline.  
  `decentralised, microblogging, network, plain-text, protocol`
- **[Umka](../drafts/brew/umka-lang.md)**: A small statically typed scripting language with Go-like syntax, built to be embedded in C programs and run on a bytecode VM.  
  `c, embeddable, language, scripting, static-typing`
- **[vip](../drafts/brew/vip.md)**: A 1997 Bourne shell script that drops into the middle of a pipe so you can edit the stream by hand before it moves on.  
  `ancient, pipes, shell, unix`
- **[Woxi](../drafts/brew/woxi.md)**: A from-scratch Rust interpreter for a subset of the Wolfram Language, so you can run symbolic one-liners and scripts without a Wolfram kernel or license.  
  `interpreter, jupyter, language, repl, rust, wolfram`

## afternoon

- **[ABCL (Armed Bear Common Lisp)](../drafts/brew/abcl.md)**: A full ANSI Common Lisp that compiles to Java bytecode, giving you a Lisp REPL with direct access to the Java ecosystem.  
  `common-lisp, jvm, language, lisp, repl`
- **[ad](../drafts/brew/ad.md)**: A Rust text editor that pairs vi and kakoune style modal editing with Plan 9 Acme's idea that text on screen can be executed.  
  `acme, editor, modal-editing, plan9, rust, tui`
- **[Agda](../drafts/brew/agda.md)**: A programming language where types can depend on values, so a program's type can carry a machine-checked proof about what it does.  
  `emacs, functional, language, proofs, type-theory`
- **[Algol 68 Genie](../drafts/brew/algol68g.md)**: A from-scratch interpreter for Algol 68, the 1968 language with a two-level grammar, runtime checks, a debugger and arbitrary-precision arithmetic.  
  `algol, ancient, interpreter, language`
- **[Anyquery](../drafts/brew/anyquery.md)**: A SQLite-based query engine that turns GitHub, Notion, Spotify, Gmail, CSV files and 40+ other sources into tables you can SELECT from and JOIN.  
  `cli, mcp, plugins, sql, sqlite`
- **[Arturo](../drafts/brew/arturo.md)**: A small scripting language with no reserved words, where code is just a list of words and symbols read by context, descended from Rebol, Forth and Lisp.  
  `language, nim, rebol-like, scripting`
- **[Asymptote](../drafts/brew/asymptote.md)**: A programming language for technical drawings, where figures are code in a mathematical coordinate system and labels are typeset by real LaTeX.  
  `diagrams, language, latex, math, vector-graphics`
- **[ATS/Postiats](../drafts/brew/ats2-postiats.md)**: A statically typed language where dependent types, linear types and proofs live in the same source file as the program, compiling to native code.  
  `dependent-types, language, linear-types, proofs, types`
- **[BaseX](../drafts/brew/basex.md)**: A lightweight XML database and XQuery processor that lets you query XML, JSON and CSV with a functional query language most developers never meet.  
  `database, java, query-language, xml, xquery`
- **[Beancount](../drafts/brew/beancount.md)**: A double-entry bookkeeping language: you write your finances as plain text, and it parses and checks them like a compiler would.  
  `accounting, language, plain-text, python`
- **[Bend](../drafts/brew/bend.md)**: A parallel functional language whose type checker doubles as a proof checker, pitched as a way to stop AI coding agents from breaking your declared rules.  
  `dependent-types, functional, gpu, language, parallel, proofs`
- **[bic](../drafts/brew/bic.md)**: A C interpreter with a REPL prompt that lets you #include real system headers and call actual libc functions, no main() required.  
  `api, c, interpreter, libc, repl`
- **[bsc](../drafts/brew/bsc.md)**: A compiler that turns Bluespec, a high-level hardware description language with a Haskell-style syntax, into plain Verilog, so you can design circuits as rules instead of wiring.  
  `compiler, hardware, haskell, language, verilog`
- **[btfs](../drafts/brew/btfs.md)**: Mounts a .torrent file or magnet link as a read-only directory, so ls, cat and video players can read files that download from the swarm as they are opened.  
  `bittorrent, filesystem, fuse, network, protocol`
- **[C-Kermit](../drafts/brew/c-kermit.md)**: A single portable binary that handles serial lines, modems, Telnet and SSH, transfers files with a protocol from 1981, and automates it all with its own scripting language.  
  `ancient, file-transfer, modem, protocol, scripting, serial`
- **[CafeOBJ](../drafts/brew/cafeobj.md)**: An algebraic specification language from Japan where you describe software as equations, run them by rewriting, and prove properties by executing proof scores.  
  `formal-methods, language, math, rewriting, theorem-proving`
- **[Cayley](../drafts/brew/cayley.md)**: A graph database for Linked Data, modeled on the one behind Google's Knowledge Graph, queryable in Gremlin-style, GraphQL-style or Freebase MQL languages.  
  `go, graph-database, linked-data, query-languages`
- **[cc65](../drafts/brew/cc65.md)**: A full C compiler and assembler toolchain for the 6502 chip, letting you write C that runs on the C64, NES, Apple II and other 8-bit machines.  
  `6502, 8-bit, assembler, c, compiler, cross-compiler, retro`
- **[ChaiScript](../drafts/brew/chaiscript.md)**: A header-only scripting language you embed inside a C++ program, so scripts can call your C++ functions and hand typed values back.  
  `c++, embedded, language, library, scripting`
- **[Chapel](../drafts/brew/chapel.md)**: A compiled parallel programming language where threads, multiple machines and GPUs are all written with the same few language constructs, and it runs on a laptop.  
  `compiler, gpu, hpc, language, parallel`
- **[Chez Scheme](../drafts/brew/chezscheme.md)**: A Scheme implementation that compiles everything, even what you type at the prompt, straight to optimized native machine code.  
  `compiler, language, lisp, repl, scheme`
- **[Chibi-Scheme](../drafts/brew/chibi-scheme.md)**: A very small Scheme interpreter built to be embedded in C programs, with R7RS, a full numeric tower, and Unicode, and a REPL to try it.  
  `c, embedding, language, r7rs, scheme`
- **[ClassAds](../drafts/brew/classads.md)**: An expression language from HTCondor where two records match only if each one's requirements evaluate true against the other, a two-sided matchmaking data model.  
  `htcondor, language, library, matchmaking`
- **[Coconut](../drafts/brew/coconut.md)**: A functional language that compiles to plain Python, adding pipelines, pattern matching and short lambdas while staying a superset of Python.  
  `compiler, functional, language, python`
- **[Cryptol](../drafts/brew/cryptol.md)**: A language for writing cryptographic algorithms as executable specs, which you can test with random inputs or prove correct for all inputs with an SMT solver.  
  `cryptography, formal-methods, language, smt`
- **[CTL](../drafts/brew/ctl.md)**: A deliberately tiny language for color transforms: write pixel math as a program, run it on an image, and share it as plain text.  
  `color, dsl, image, language, vfx`
- **[CWB (IMS Open Corpus Workbench)](../drafts/brew/cwb3.md)**: Index and query text corpora of up to two billion words with linguistic annotations, using CQP, a dedicated corpus query language and engine.  
  `corpus, linguistics, query-language, text-analysis`
- **[cweb](../drafts/brew/cweb.md)**: Knuth and Levy's literate programming system: write one file of prose and C, then get both a compilable program and a typeset, cross-indexed document.  
  `ancient, c, knuth, literate-programming, tex`
- **[Dafny](../drafts/brew/dafny.md)**: A programming language where you write specifications beside your code and a built-in verifier proves the code meets them, then compiles to C#, Go, Python, Java, or JavaScript.  
  `formal-methods, language, math, verification`
- **[dbacl](../drafts/brew/dbacl.md)**: A set of small Unix tools that learn from example text and then say which category a new document most resembles, using Bayesian statistics.  
  `bayesian, old-school, spam, text-classification, unix`
- **[Decker](../drafts/brew/decker.md)**: A HyperCard-style sketchpad for making interactive cards with pictures, sound and scripts, saved as one HTML file, plus a terminal interpreter called Lilt.  
  `creative-tools, gui, html, hypercard, language, lil`
- **[dMagnetic](../drafts/brew/dmagnetic.md)**: A terminal interpreter that runs 1980s Magnetic Scrolls text adventures like The Pawn and Jinxter from their original game files, with pictures drawn as text or sixels.  
  `c, interactive-fiction, interpreter, retro, text-adventure`
- **[Dolt](../drafts/brew/dolt.md)**: A MySQL-compatible SQL database you can branch, merge, diff, push and pull like a Git repository, with history down to individual cells.  
  `database, git, mysql, sql, versioning`
- **[Doltgres](../drafts/brew/doltgres.md)**: A Postgres-compatible database where tables are versioned like a Git repository, so you can commit, branch and merge your data using SQL.  
  `database, postgres, sql, version-control`
- **[DoltLite](../drafts/brew/doltlite.md)**: A SQLite fork that swaps the B-tree for a prolly tree, so a single-file SQL database gets Git-style branches, commits, diffs and merges.  
  `database, embedded, prolly-tree, sql, sqlite, version-control`
- **[DOSBox Staging](../drafts/brew/dosbox-staging.md)**: A modern DOSBox fork that runs old DOS games and programs in a window, with CRT shader emulation and period sound hardware built in.  
  `audio, dos, emulator, games, retro`
- **[DPS8M](../drafts/brew/dps8m.md)**: A simulator of the 36-bit Honeywell/GE mainframes built to run Multics, so you can run software for hardware almost nobody has touched.  
  `36-bit, ancient, mainframe, multics, simulation`
- **[ECL](../drafts/brew/ecl.md)**: A maintained Common Lisp implementation built to be embedded in other programs, with a REPL and a small config helper.  
  `common-lisp, compiler, embeddable, language, lisp`
- **[edbrowse](../drafts/brew/edbrowse.md)**: A web browser, editor and mail client driven by ed-style line commands, built by a blind programmer and scriptable enough to run web tasks from cron.  
  `accessibility, browser, ed, network, scripting, tui`
- **[EiffelStudio](../drafts/brew/eiffelstudio.md)**: A full IDE for Eiffel, the object-oriented language where preconditions, postconditions and invariants are part of the code itself.  
  `design-by-contract, eiffel, gui, ide, language, object-oriented`
- **[Elm](../drafts/brew/elm.md)**: A small functional language that compiles to JavaScript, built around one architecture and a promise of no runtime errors in practice.  
  `functional, javascript, language, web`
- **[Erg](../drafts/brew/erg.md)**: A statically typed language that runs on Python, with refinement types that catch out-of-range indexes and unit mismatches at compile time.  
  `compiler, language, python, type-system`
- **[Erlang/OTP 27](../drafts/brew/erlang@27.md)**: A functional language and runtime built around tiny isolated processes that talk by message, made for systems that must keep running.  
  `actors, concurrency, functional, language, runtime`
- **[execline](../drafts/brew/execline.md)**: A scripting language with no interpreter loop: each command execs the next program in the chain, giving a different way to think about shells.  
  `exec, language, shell, skarnet, unix`
- **[Fantom](../drafts/brew/fantom.md)**: Fantom is a Java-flavoured object-oriented language that runs on the JVM and in browsers, with closures, immutability and actor concurrency built in.  
  `actors, jvm, language, object-oriented`
- **[Flix](../drafts/brew/flix.md)**: A statically typed JVM language where side effects are tracked in the type system and Datalog constraints are ordinary values you can pass around.  
  `datalog, effects, functional, jvm, language`
- **[foma](../drafts/brew/foma.md)**: A finite-state compiler for building transducers, the machines computational linguists use to turn words into their parts and back again.  
  `automata, language, library, linguistics`
- **[Frege](../drafts/brew/frege.md)**: A lazy, purely functional language in the spirit of Haskell that compiles to Java and runs on the JVM, with access to any Java library.  
  `functional, haskell, jvm, language`
- **[Futhark](../drafts/brew/futhark.md)**: A small functional array language from the University of Copenhagen that compiles to GPU code, so you write ML-style array functions instead of CUDA or OpenCL.  
  `compiler, functional, gpu, language, parallel`
- **[GCL (GNU Common Lisp)](../drafts/brew/gcl.md)**: GCL is the GNU project's Common Lisp, which turns Lisp into native code by handing it to your C compiler.  
  `common-lisp, compiler, gnu, lisp, repl`
- **[Gerbil Scheme](../drafts/brew/gerbil-scheme.md)**: A Scheme dialect on the Gambit runtime that compiles to native code, with a full macro tower and a module system aimed at systems programming.  
  `compiler, gambit, language, lisp, macros, scheme`
- **[Gforth](../drafts/brew/gforth.md)**: The GNU implementation of Forth, a stack-based language with almost no syntax, where you type words at a prompt and build the language up yourself.  
  `forth, gnu, language, repl, stack-based`
- **[git-bug](../drafts/brew/git-bug.md)**: A bug tracker that lives inside your git repository as git objects, syncs through normal remotes, and works fully offline.  
  `bug-tracker, git, go, offline-first, tui`
- **[Gluon](../drafts/brew/gluon.md)**: A small, statically typed, type-inferred functional language written in Rust, designed to be embedded in other programs the way Lua is.  
  `embeddable, functional, language, rust, type-inference`
- **[GNU APL](../drafts/brew/gnu-apl.md)**: A free interpreter for APL, the glyph-heavy array language from the 1960s, where one line of symbols can replace a page of loops.  
  `ancient, apl, array, gnu, language`
- **[GNU Prolog](../drafts/brew/gnu-prolog.md)**: A Prolog compiler with a finite-domain constraint solver that turns logic programs into stand-alone native executables, the way gcc turns C into binaries.  
  `compiler, constraints, logic-programming, prolog`
- **[GNU Smalltalk](../drafts/brew/gnu-smalltalk.md)**: A command-line Smalltalk-80 you can script with, where everything is an object and the whole system lives in a rebuildable image file.  
  `language, object-oriented, old-school, repl, scripting, smalltalk`
- **[GnuCOBOL](../drafts/brew/gnucobol.md)**: A free COBOL compiler that turns the language behind banks and mainframes into native executables on an ordinary laptop.  
  `ancient, cobol, compiler, language`
- **[Game of Trees (got)](../drafts/brew/got.md)**: A version control system from OpenBSD developers that trades Git's flexibility for simplicity while keeping Git repositories as its storage format.  
  `git, openbsd, tui, version-control`
- **[grap](../drafts/brew/grap.md)**: A Bell Labs-era language for describing graphs as text and typesetting them inside troff or TeX documents, still being updated in 2025.  
  `bell-labs, graphs, language, pic, troff, typesetting`
- **[Guile](../drafts/brew/guile.md)**: GNU's Scheme implementation, built to be embedded in other programs as an extension language and able to host other languages on its compiler.  
  `compilers, embeddable, gnu, language, lisp, scheme`
- **[guile-fibers](../drafts/brew/guile-fibers.md)**: A Guile Scheme library for lightweight fibers that talk over synchronous channels, built on the ideas of Concurrent ML.  
  `concurrency, guile, library, lisp, scheme`
- **[Halide](../drafts/brew/halide.md)**: A language embedded in C++ and Python that splits what an image computation does from how it runs, so you can retune performance without touching the math.  
  `compiler, gpu, image-processing, language`
- **[Harbour](../drafts/brew/harbour.md)**: A free, Clipper-compatible xBase compiler that turns .prg source into native apps, keeping the dBASE-era language alive on modern systems.  
  `clipper, compiler, dbase, language, xbase`
- **[HashLink](../drafts/brew/hashlink.md)**: A virtual machine for Haxe that runs typed bytecode through a JIT, or turns the same program into C for a native build.  
  `bytecode, haxe, jit, language, vm`
- **[Icon](../drafts/brew/icon.md)**: A 1979 successor to SNOBOL4 where expressions can yield multiple results and the runtime backtracks until something succeeds.  
  `ancient, backtracking, language, snobol`
- **[Idris 2](../drafts/brew/idris2.md)**: A purely functional language where types are ordinary values, so the compiler can check things like list lengths before your program ever runs.  
  `functional, language, math, types`
- **[immudb](../drafts/brew/immudb.md)**: A database that only appends, and hands back cryptographic proofs that its history has not been altered, which clients check without trusting the server.  
  `cryptography, database, go, merkle-tree, sql, tamper-evident`
- **[Inform 6](../drafts/brew/inform6.md)**: A 1993 compiler for writing text adventures in a C-like language, producing Z-machine story files and still serving as the engine under Inform 7.  
  `compiler, interactive-fiction, retro, text-adventure, z-machine`
- **[Inko](../drafts/brew/inko.md)**: A statically typed language that compiles to native code, with Erlang-style lightweight processes and Rust-style ownership but no garbage collector.  
  `actors, concurrency, language, llvm, ownership`
- **[INSTEAD](../drafts/brew/instead.md)**: A small Lua-driven interpreter for text adventures from the Russian interactive fiction scene. Hand it a zipped game and it plays.  
  `game-engine, interactive-fiction, lua, sdl, text-adventure`
- **[Interface99](../drafts/brew/interface99.md)**: A C99 header library that gives plain C Rust-style traits and Go-style interfaces, with vtables generated by preprocessor macros.  
  `c, c99, interfaces, library, macros, metaprogramming`
- **[Io](../drafts/brew/io.md)**: A small prototype-based language where everything is a message send and objects are made by cloning, in the Smalltalk and Self family.  
  `language, prototype-based, repl, smalltalk, webassembly`
- **[Janet](../drafts/brew/janet.md)**: A small Lisp-style scripting language with a bytecode VM, built-in PEG parsing, green threads and networking, all under 1MB and embeddable via two C files.  
  `bytecode-vm, embeddable, language, lisp, peg`
- **[JerryScript](../drafts/brew/jerryscript.md)**: A JavaScript engine written in C99 that is meant to run in under 64 KB of RAM on microcontrollers, with a `jerry` command for trying it on a desktop.  
  `c, embedded, iot, javascript, language, microcontrollers`
- **[Joker](../drafts/brew/joker.md)**: A small Clojure dialect written in Go that starts fast, so you can script with it, and that doubles as a Clojure linter and formatter.  
  `clojure, formatter, go, linter, lisp, scripting`
- **[Jolie](../drafts/brew/jolie.md)**: A programming language where the basic unit is a service, not an object or function, so one program can run locally, remotely, or over several protocols at once.  
  `jvm, language, microservices, protocols`
- **[Joyce](../drafts/brew/joyce.md)**: An emulator of the Amstrad PCW, a 1980s all-in-one word processor that ran CP/M, kept alive with a deep archive of documentation.  
  `amstrad, cp/m, emulator, retro, z80`
- **[Judy](../drafts/brew/judy.md)**: A C library for a sparse dynamic array that starts as a null pointer, grows only as you fill it, and claims to replace hash tables and trees.  
  `c, data-structures, library`
- **[JUMAN](../drafts/brew/juman.md)**: A Japanese morphological analyser from Kyoto University that splits text into words and tags each with reading, base form and part of speech, even for slangy spellings.  
  `japanese, linguistics, nlp, tokenizer`
- **[Kawa](../drafts/brew/kawa.md)**: Kawa is a Scheme implementation for the Java platform: a Lisp REPL on the JVM that also compiles to bytecode and works with Java classes.  
  `java, jvm, language, lisp, repl, scheme`
- **[Kiesel](../drafts/brew/kiesel.md)**: A JavaScript engine written from scratch in Zig, installable as a single kiesel executable, for seeing how an ECMAScript engine works without V8 underneath.  
  `engine, javascript, language, zig`
- **[Kimwitu++](../drafts/brew/kimwitu++.md)**: A tree-processing generator from the compiler-toolkit era: describe a syntax tree and rewrite rules in a small language, get C++ classes back.  
  `ancient, c++, code-generation, compilers, term-rewriting`
- **[Koka](../drafts/brew/koka.md)**: A research functional language that tracks side effects in its types and compiles to C without a garbage collector, using effect handlers for exceptions and async.  
  `compiler, effect-types, functional, language, research`
- **[Kona](../drafts/brew/kona.md)**: An open-source reimplementation of k3, a terse ASCII array language descended from APL and LISP, run as an interactive interpreter called k.  
  `apl, array-programming, interpreter, k, language`
- **[ksh93](../drafts/brew/ksh93.md)**: A maintained fork of KornShell 93, the AT&T shell that shaped bash and POSIX sh, patched to be the least buggy ksh93 yet.  
  `ancient, language, shell, unix`
- **[LaTeXML](../drafts/brew/latexml.md)**: Converts LaTeX documents into XML, HTML and MathML by emulating TeX in Perl, built so a math library could keep the meaning of its formulas.  
  `documents, latex, mathml, perl, xml`
- **[lci](../drafts/brew/lci.md)**: A command-line interpreter for the untyped lambda calculus, where integers, lists and operators are all built from nothing but functions.  
  `functional, lambda-calculus, language, math`
- **[ledger](../drafts/brew/ledger.md)**: A command-line double-entry accounting tool that reads a plain-text journal you write by hand and turns it into balances, registers and reports.  
  `accounting, cli, double-entry, plain-text`
- **[LFE (Lisp Flavoured Erlang)](../drafts/brew/lfe.md)**: A Lisp with Erlang's data types that compiles to BEAM bytecode, so you can write macros and call OTP's concurrency machinery in s-expressions.  
  `beam, erlang, language, lisp, macros, repl`
- **[libansilove](../drafts/brew/libansilove.md)**: A small C library that turns BBS-era ANSI art and related text-mode formats into PNG images, the engine behind the Ansilove converter.  
  `ansi-art, bbs, c, library, png`
- **[Cello](../drafts/brew/libcello.md)**: A C library that bolts generics, type classes, exceptions, reflection and optional garbage collection onto plain C, as an experiment in how far the language can be pushed.  
  `c, experiment, generics, library, macros`
- **[libmps (Memory Pool System)](../drafts/brew/libmps.md)**: A C memory management library, in development since 1994, that lets you mix manual allocation and incremental generational garbage collection through swappable pool classes.  
  `ancient, c, garbage-collection, library, memory-management`
- **[LifeLines](../drafts/brew/lifelines.md)**: A 1990s terminal genealogy program with its own database and a scripting language that turns family trees into LaTeX books and PostScript charts.  
  `ancient, curses, gedcom, genealogy, scripting, tui`
- **[LilyPond](../drafts/brew/lilypond.md)**: A music engraving program where you type sheet music as plain text and a compiler typesets it into a score.  
  `gnu, language, music, notation, typesetting`
- **[Lisette](../drafts/brew/lisette.md)**: A small Rust-flavoured language that compiles to readable Go, adding pattern matching, Option and Result, and a linter aimed at Go's footguns.  
  `go, language, rust, transpiler`
- **[Logtalk](../drafts/brew/logtalk.md)**: Logtalk adds objects, protocols, and hot-patchable components to Prolog by compiling down to the Prolog system you already have.  
  `language, logic-programming, object-oriented, prolog`
- **[Lout](../drafts/brew/lout.md)**: A document formatter in the LaTeX family, built on a purely functional language, that turns plain-text descriptions into PostScript.  
  `ancient, functional, language, postscript, typesetting`
- **[LuaJIT](../drafts/brew/luajit.md)**: A Lua interpreter with a trace-compiling JIT and a built-in C FFI, a small VM with an unusually deep design.  
  `compiler, jit, language, lua`
- **[LunarML](../drafts/brew/lunarml.md)**: A Standard ML compiler that emits Lua or JavaScript, so a statically typed functional language can run inside Lua, LuaJIT, Node.js or a browser.  
  `compiler, continuations, functional, javascript, lua, standard-ml`
- **[MAME](../drafts/brew/mame.md)**: An emulator whose source code doubles as documentation for thousands of arcade boards, computers, consoles and calculators, built to preserve old hardware.  
  `arcade, emulation, preservation, vintage-hardware`
- **[marisa](../drafts/brew/marisa.md)**: A static trie that squeezes millions of strings into a fraction of the usual space, with command-line tools for building and querying dictionaries.  
  `c++, compression, data-structures, library, trie`
- **[Mercury](../drafts/brew/mercury.md)**: A compiled logic/functional language built for large programs, with static analysis that catches errors before anything runs.  
  `compiler, functional, language, logic-programming`
- **[Metalang99](../drafts/brew/metalang99.md)**: A functional programming language that runs inside the C preprocessor, with lists, pattern matching and recursion, shipped as plain header files.  
  `c, functional, header-only, library, metaprogramming, preprocessor`
- **[MicroPython](../drafts/brew/micropython.md)**: A real Python 3 interpreter small enough for microcontrollers, with a REPL that runs on about 16k of RAM and talks to pins, buses and timers.  
  `embedded, language, microcontroller, needs-hardware, python`
- **[Racket (minimal)](../drafts/brew/minimal-racket.md)**: A Lisp-family language built for making new languages: define your own syntax with macros and have it compile down to ordinary Racket.  
  `language-design, lisp, macros, racket, scheme`
- **[MLKit](../drafts/brew/mlkit.md)**: A Standard ML compiler that decides memory allocation and freeing at compile time using region inference, so programs can skip or limit garbage collection.  
  `compiler, language, memory-management, regions, standard-ml`
- **[MLton](../drafts/brew/mlton.md)**: A whole-program optimizing compiler for Standard ML that turns an entire program into one small native executable, with its own lexer, parser and profiler tools.  
  `compiler, functional, language, standard-ml`
- **[Nickel](../drafts/brew/nickel.md)**: A small lazy configuration language that is essentially JSON with functions, merging, and contracts, and exports to JSON, YAML, or TOML.  
  `configuration, functional, language, nix`
- **[Nickle](../drafts/brew/nickle.md)**: A C-like desk calculator language with exact rationals and arbitrary precision numbers, built as a fuller replacement for bc, dc and expr.  
  `arbitrary-precision, calculator, language`
- **[nip4](../drafts/brew/nip4.md)**: A spreadsheet where cells hold images and formulas instead of numbers, built on libvips, so editing one input recalculates everything downstream.  
  `functional, gui, images, libvips, spreadsheet`
- **[noweb](../drafts/brew/noweb.md)**: A small literate-programming tool: write prose and named code chunks in one file, then weave it into a document or tangle it into compilable source.  
  `ancient, documentation, literate-programming, tex`
- **[NQP (Not Quite Perl)](../drafts/brew/nqp.md)**: A deliberately tiny Raku-flavoured language, with Raku's object model and regex engine, built for writing compilers that run on virtual machines.  
  `compilers, language, moarvm, raku, virtual-machine`
- **[Numbat](../drafts/brew/numbat.md)**: A scientific calculator and statically typed language where physical units are part of the type system, so 15 km/h * 30 min comes out as 7.5 km.  
  `calculator, language, math, repl, science, units`
- **[nvc](../drafts/brew/nvc.md)**: A free VHDL compiler and simulator that compiles hardware descriptions to native code via LLVM, so you can run digital circuits from the terminal.  
  `fpga, hardware-description, llvm, simulation, vhdl`
- **[oakc](../drafts/brew/oakc.md)**: Oak is a small Rust-flavoured language that compiles down to a 17-instruction intermediate representation, so porting it to a new target means implementing a handful of operations.  
  `compiler, intermediate-representation, language, rust`
- **[Odin](../drafts/brew/odin.md)**: A compiled systems language that calls itself 'the C alternative for the Joy of Programming', with data-oriented features and graphics bindings built in.  
  `compiler, data-oriented, graphics, language, systems`
- **[1ML](../drafts/brew/one-ml.md)**: An experimental ML dialect where modules are ordinary values and the core and module languages collapse into one, from Andreas Rossberg's research.  
  `functional, language, ml, research, type-systems`
- **[OpenSP](../drafts/brew/open-sp.md)**: OpenSP is James Clark's SGML parser suite, the old pre-XML markup toolkit, installed as onsgmls, osx and a few other small tools.  
  `ancient, dsssl, markup, parser, sgml`
- **[Ott](../drafts/brew/ott.md)**: Write a programming language's syntax and semantics once in ASCII math notation, then generate LaTeX, Coq, Isabelle, HOL and Lem definitions from it.  
  `coq, formal-methods, language, latex, math, semantics`
- **[PC6001VX](../drafts/brew/pc6001vx.md)**: An emulator for NEC's obscure early-1980s PC-6001 home computer line, with a built-in ROM so it boots without any dumps.  
  `8-bit, emulator, gui, japanese, retro`
- **[peg and leg](../drafts/brew/peg.md)**: Two small tools that turn a parsing expression grammar into a C recursive-descent parser, with backtracking and ordered choice instead of lex and yacc.  
  `c, code-generator, grammar, parsing, peg`
- **[Picat](../drafts/brew/picat.md)**: A logic programming language that mixes Prolog-style search and unification with loops, assignments, tabling, and constraint solvers, so planning problems become short rule sets.  
  `constraints, language, logic-programming, prolog, tabling`
- **[PicoRuby](../drafts/brew/picoruby.md)**: A small Ruby implementation built for microcontrollers like the Raspberry Pi Pico, which also runs on your desktop as an interpreter, bytecode compiler and shell.  
  `embedded, language, microcontroller, mruby, needs-hardware, ruby`
- **[Poly/ML](../drafts/brew/polyml.md)**: A Standard ML implementation with a REPL, a native-code compiler and multicore threads, used to run large theorem provers like Isabelle and HOL.  
  `compiler, functional, language, repl, standard-ml`
- **[Pony](../drafts/brew/ponyc.md)**: A compiled actor-model language whose type system checks at compile time that concurrent programs cannot have data races, with no locks.  
  `actors, compiler, concurrency, language, type-system`
- **[Prog8](../drafts/brew/prog8.md)**: A structured, compiled language that turns readable source into native machine code for the 6502 chip inside the Commodore 64, Commander X16 and other 8-bit machines.  
  `6502, commander-x16, commodore-64, compiler, emulator, language, retro`
- **[Proof General](../drafts/brew/proof-general.md)**: An Emacs front end for interactive theorem provers like Coq: you write a proof in one buffer and the prover checks it step by step.  
  `coq, emacs, formal-methods, math, theorem-proving`
- **[PureScript](../drafts/brew/purescript.md)**: A small, strongly typed, Haskell-inspired language that compiles to readable JavaScript, giving you a serious type system in the browser and Node.  
  `functional, haskell-like, javascript, language, types`
- **[QBE](../drafts/brew/qbe.md)**: A hobby-scale compiler backend that turns a small SSA intermediate language into assembly, showing in a few thousand lines of C how real compilers lower code.  
  `backend, compiler, intermediate-language, ssa`
- **[QTads](../drafts/brew/qtads.md)**: A graphical interpreter that plays TADS interactive fiction games, including the Multimedia TADS ones with pictures and sound that text-only players skip.  
  `game, gui, interactive-fiction, language, tads`
- **[QUASI88](../drafts/brew/quasi88.md)**: An SDL2 emulator for NEC's PC-8801, a Japanese 8-bit home computer, so you can run its software in a window with sound.  
  `8-bit, emulator, japanese, pc-8801, retro, sdl2`
- **[Quex](../drafts/brew/quex.md)**: Quex generates lexical analyzers from pattern definitions, producing directly coded code instead of lookup tables, with Unicode queries and state graph drawing built in.  
  `code-generation, compilers, lexer, unicode`
- **[Ragel](../drafts/brew/ragel.md)**: Ragel compiles regex-like machine descriptions with embedded code actions into dependency-free C, C++ or assembly state machines, a hands-on way to see how parsers work.  
  `code-generation, compilers, parsing, regex, state-machines`
- **[Rakudo](../drafts/brew/rakudo.md)**: Rakudo is the main compiler for Raku, the language formerly known as Perl 6, with a name that means 'Way of the Camel'.  
  `compiler, language, perl, raku`
- **[recutils](../drafts/brew/recutils.md)**: GNU recutils turns plain text files into typed, queryable databases you can still edit by hand in any editor.  
  `csv, database, gnu, plain-text, query-language`
- **[redo](../drafts/brew/redo.md)**: A build system where each target is a small shell script and dependencies are declared by running ordinary commands, from djb's design as a replacement for make.  
  `build-system, djb, make, python, shell`
- **[Remind](../drafts/brew/remind.md)**: A decades-old command-line calendar and alarm program driven by its own small scripting language for recurring events, holidays and exceptions.  
  `calendar, old-school, plain-text, scripting-language, unix`
- **[RGBDS](../drafts/brew/rgbds.md)**: An assembler and linker toolchain for the Game Boy and Game Boy Color: write assembly and PNG art, get a ROM that runs on the console.  
  `assembler, assembly, game-boy, homebrew, linker, retro`
- **[rqlite](../drafts/brew/rqlite.md)**: A SQLite database you reach with curl and replicate across machines, so a few nodes keep serving SQL if one dies.  
  `database, distributed, http, network, raft, sqlite`
- **[RumbleDB](../drafts/brew/rumbledb.md)**: A query engine that runs JSONiq and XQuery over messy nested data, on a laptop or scaled out across a Spark cluster.  
  `java, json, jsoniq, query-language, spark, xml, xquery`
- **[Rune](../drafts/brew/rune.md)**: Rune is a small dynamic scripting language written for embedding inside Rust programs, with async built in from the start.  
  `async, embeddable, language, rust, scripting`
- **[RustPython](../drafts/brew/rustpython.md)**: A Python 3 interpreter written from scratch in Rust, embeddable in Rust programs and compilable to WebAssembly to run Python in a browser.  
  `interpreter, python, rust, wasi, webassembly`
- **[Rye](../drafts/brew/ryelang.md)**: Rye is a small homoiconic scripting language where if, loop and fn are ordinary functions, and failures are values instead of null.  
  `go, homoiconic, language, rebol, repl`
- **[SBCL](../drafts/brew/sbcl.md)**: A fast, free Common Lisp compiler with a live interactive environment, debugger and profiler built in: a door into one of the oldest programming traditions.  
  `common-lisp, compiler, language, lisp, repl`
- **[Scheme 48](../drafts/brew/scheme48.md)**: A Scheme interpreter built on a byte-code VM, made by Kelsey and Rees as a testbed and teaching tool, and the birthplace of Pre-Scheme.  
  `byte-code, interpreter, language, pre-scheme, research, scheme`
- **[Scryer Prolog](../drafts/brew/scryer-prolog.md)**: A modern ISO Prolog written in Rust, with constraint solving, tabling and an HTTP server, for trying logic programming where you state facts and ask questions.  
  `constraints, language, logic-programming, prolog, rust`
- **[SFST](../drafts/brew/sfst.md)**: A finite-state transducer toolbox for building morphological analysers, the machinery that lets software split words into stems and endings.  
  `c++, finite-state, language, morphology, nlp, transducers`
- **[SILE](../drafts/brew/sile.md)**: A typesetting system in the spirit of TeX, scriptable in Lua, that turns plain-text source or XML into a printed-quality PDF.  
  `fonts, lua, pdf, tex, typesetting`
- **[SML/NJ](../drafts/brew/smlnj.md)**: A maintained compiler and interactive REPL for Standard ML, a statically typed functional language with a long academic history, plus its own parser and lexer generators.  
  `compiler, functional, language, ml`
- **[SNOBOL4](../drafts/brew/snobol4.md)**: A string-processing language from Bell Labs where patterns are first-class values and matching backtracks. Odd, old, and a good way to see another model of text handling.  
  `ancient, language, pattern-matching, strings`
- **[Solod](../drafts/brew/solod.md)**: Solod is a strict subset of Go that transpiles to readable C11 with no runtime, no garbage collector and explicit heap allocation.  
  `c, compilers, go, language, transpiler`
- **[Soufflé](../drafts/brew/souffle.md)**: Soufflé is a Datalog-style logic language that compiles analysis rules into parallel C++, built for questions like points-to and taint analysis over large programs.  
  `compiler, datalog, declarative, logic-programming, static-analysis`
- **[spatialite-tools](../drafts/brew/spatialite-tools.md)**: A bundle of about twenty command-line tools that turn SQLite into a GIS workbench: shapefiles, OpenStreetMap, GPS photos and routing networks, all in one database file.  
  `gis, maps, openstreetmap, shapefile, sql, sqlite`
- **[starlark-rust](../drafts/brew/starlark-rust.md)**: A Rust implementation of Starlark, the deterministic Python-like language behind Bazel and Buck2 builds, with a REPL, linter and language server.  
  `bazel, buck2, embeddable, language, rust, starlark`
- **[SWI-Prolog](../drafts/brew/swi-prolog.md)**: A mature Prolog system where you state facts and rules, then ask questions at a `?-` prompt and let the engine search for answers.  
  `language, logic-programming, prolog, repl`
- **[SystemC](../drafts/brew/systemc.md)**: A C++ class library that lets you model and simulate hardware in ordinary C++, standardised as IEEE 1666, so software can run before the chip exists.  
  `c++, hardware-modelling, language, library, simulation`
- **[Tarantool](../drafts/brew/tarantool.md)**: An in-memory database that runs your Lua code in the same process as the data, so logic and storage share one address space.  
  `application-server, database, in-memory, lua`
- **[64tass](../drafts/brew/tass64.md)**: A command-line macro assembler for the 6502 family that turns assembly source into binaries for C64-era machines, with an unusually rich expression language.  
  `6502, assembler, c64, macro-assembler, retro`
- **[tenyr](../drafts/brew/tenyr.md)**: A deliberately small 32-bit computer you can assemble, link and run in a simulator, with Verilog that also runs on real FPGA boards.  
  `assembly, cpu, fpga, simulation, verilog`
- **[tgif](../drafts/brew/tgif.md)**: An old X11 vector drawing editor that doubles as a browser for hyper-structured graphics, a web idea from 1994 that never caught on.  
  `ancient, gui, hypertext, vector-graphics, x11`
- **[Thrax](../drafts/brew/thrax.md)**: Write grammars as short readable scripts and compile them into finite-state transducers that tokenise text, spell out numbers, or model word morphology.  
  `compiler, fst, grammar, linguistics, nlp, openfst`
- **[TinTin++](../drafts/brew/tintin.md)**: A terminal client for MUDs, the text-based multiplayer games, with a built-in scripting language for triggers, aliases, timers and an automapper.  
  `accessibility, automapper, mud, old-school, scripting, tui`
- **[TrailDB](../drafts/brew/traildb.md)**: A C library and tool that packs per-user event histories into single immutable compressed files you can query without unpacking them.  
  `c-library, compression, database, events, time-series`
- **[Trealla Prolog](../drafts/brew/trealla-prolog.md)**: A compact ISO Prolog interpreter in plain C that gives you logic programming, tabling and constraint solving from one small tpl binary.  
  `c, constraints, embeddable, interpreter, logic-programming, prolog`
- **[treecc](../drafts/brew/treecc.md)**: A compiler-compiler from DotGNU that generates C tree-building and tree-walking code from a declarative spec, and errors if any node type lacks a case for an operation.  
  `ancient, c, code-generation, compilers, dotgnu, yacc`
- **[tup](../drafts/brew/tup.md)**: A file-based build system whose dependency arrows point up instead of down, so rebuilds after a small edit stay fast even on large projects.  
  `build-system, dependency-graph, fuse, make-alternative`
- **[Umple](../drafts/brew/umple.md)**: Umple is a modeling language that adds associations and state machines to Java, Python, C++ and PHP, then generates the boilerplate code and UML-style diagrams for you.  
  `code-generation, java, language, modeling, uml`
- **[Unison](../drafts/brew/unisonlang.md)**: A statically-typed functional language that stores code as hashed syntax trees in a database instead of text files, so renames are instant and never break anything.  
  `content-addressed, functional, language, repl`
- **[Ur/Web](../drafts/brew/urweb.md)**: A statically typed functional language for web apps where the type system rules out injection, invalid HTML, dead links and bad SQL.  
  `functional, language, sql, types, web`
- **[Virtuoso](../drafts/brew/virtuoso.md)**: A single database server that speaks SQL, SPARQL and WebDAV, and also serves web pages, built by OpenLink Software and still carrying 1999-era features.  
  `database, linked-data, rdf, sparql, sql`
- **[WAMR (WebAssembly Micro Runtime)](../drafts/brew/wasm-micro-runtime.md)**: A small WebAssembly runtime that runs .wasm files outside the browser, with an interpreter, ahead-of-time compiler and JIT tiers to compare.  
  `embedded, jit, runtime, wasi, webassembly`
- **[Wren](../drafts/brew/wren.md)**: A tiny class-based scripting language with built-in fibers, made to embed in other programs, and described as Smalltalk in a Lua-sized package.  
  `embeddable, fibers, language, scripting`
- **[x3270](../drafts/brew/x3270.md)**: A terminal emulator for IBM 3270 mainframe screens, with GUI, curses and headless variants, so a modern desktop can talk to a mainframe over TELNET.  
  `ancient, mainframe, network, protocol, terminal, tn3270`
- **[xidel](../drafts/brew/xidel.md)**: A single-binary command-line tool that fetches HTML, XML or JSON and queries it with XPath, XQuery, CSS selectors or JSONiq, including a full query language you can script in.  
  `cli, html, json, scraping, xpath, xquery`
- **[XLISP-STAT](../drafts/brew/xlispstat.md)**: A 1990s statistics environment built on Lisp, where dynamic graphics and a prototype object system are the core idea, and regression models are objects.  
  `ancient, graphics, lisp, statistics, x11`
- **[xwpe](../drafts/brew/xwpe.md)**: A Borland-style terminal IDE from 1993, revived in 2026, with function-key menus, mouse support, and a modern LSP and DAP client bolted on.  
  `borland, editor, ide, lsp, retro, tui`
- **[Yacas](../drafts/brew/yacas.md)**: Yacas is a small computer algebra system with its own scripting language, where you write the rules that transform mathematical expressions.  
  `cas, language, math, symbolic`
- **[zxcc](../drafts/brew/zxcc.md)**: A CP/M 2/3 emulator for UNIX that lets eight-bit-era compilers and build tools run as ordinary command-line cross-compilers on a modern machine.  
  `8-bit, cp/m, cross-compiler, emulator, retro`
