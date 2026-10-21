---
name: pacparser
title: pacparser
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, javascript, library, network, pac, proxy]
homepage: https://github.com/manugarg/pacparser
scout_score: 5
status: draft
---

# pacparser

**TLDR;** A small library that runs proxy auto-config (PAC) JavaScript files outside a browser, so you can ask which proxy a given URL would get.

A PAC file is a JavaScript file that a browser or operating system runs to decide which proxy to use for each request. The script defines one function, and that function can branch on the URL, the host, the client's IP address, or the time of day. It returns a string like `DIRECT` or `PROXY proxy1.manugarg.com:3128; PROXY proxy2.manugarg.com:3128; DIRECT`. Most people use these every day at work or on a school network without ever seeing one run.

Pacparser embeds the QuickJS engine to execute those files from C or Python. You initialise it, load a PAC file, and call `find_proxy` with a URL and host to get the proxy string back. You can also override the client IP the script sees with `setmyip`, which lets you test how the same file behaves from different network positions. The README says the standard's helper functions come from Mozilla's PAC implementation, apart from a couple of DNS functions pacparser defines itself.

The stated idea is to "make it easy to add PAC-file parsing capability to any program". The deeper door is the mechanism itself: proxy policy delivered as a program, not a config file, fetched and run by every client. Once you can evaluate one offline, you can read a real company's `wpad.dat` and see what it decides.

Homebrew also installs a `pactester` executable. The README does not document it, so start with its `--help`.

## Install

```
brew install pacparser
# Python module instead: python -m pip install pacparser
```

## Try this

```
pactester --help
```
Shows the options of the command-line tester that Homebrew installs, which the README does not document.

```
python -m pip install pacparser
```
Installs the Python module from PyPI, with prebuilt wheels for 64-bit Linux, Windows and macOS.

```
pacparser.find_proxy('http://www.google.com', 'www.google.com')
```
In Python, after init and parse_pac, returns the proxy string for that URL. The README example returns 'DIRECT' by default.

## What's unique

It is a small embeddable evaluator for a mechanism most people never see running. Any C or Python program can make the same proxy decision a browser would, using real PAC JavaScript.

## Caveats

The API is not thread-safe, since all state is process-global, and the brief could not confirm recent project activity.

## Links

- [Project homepage and online PAC file tester](http://pacparser.manugarg.com)
- [GitHub repository](https://github.com/manugarg/pacparser)
- [Wikipedia: Proxy auto-config](http://en.wikipedia.org/wiki/Proxy_auto-config)
- [Releases](https://github.com/manugarg/pacparser/releases)
