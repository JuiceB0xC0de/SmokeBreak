---
name: edbrowse
title: edbrowse
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [accessibility, afternoon, browser, ed, network, scripting, tui]
homepage: https://edbrowse.org
scout_score: 7
status: draft
---

# edbrowse

**TLDR;** A web browser, editor and mail client driven by ed-style line commands, built by a blind programmer and scriptable enough to run web tasks from cron.

Edbrowse is a text-only editor, browser and mail client with an interface modelled on /bin/ed. You type short line commands instead of using a mouse or full-screen menus. It renders HTML into text you can edit, can work on several files at once, and can query databases over ODBC. It also runs JavaScript. The engine has been swapped several times over the years: a home-grown one, then SpiderMonkey, duktape, quickjs, and now quickjs-ng.

It was written for blind users, drawing on author Karl Dahlke's years as a blind computer user. A line-oriented interface reads cleanly through a screen reader or speech synthesiser, and nothing depends on where things sit on screen. The site calls it a command-line philosophy piece in its own right.

The idea underneath is that the web can be a stream of text you edit and script, not a picture you look at. Many sighted users now use it for that reason. In the project's words: "A batch job, or cron job, can access web pages on the internet, submit forms, and send email, with no human intervention whatsoever." The README says it is "a fully command based browser, the only one of its kind as far as we know."

The commands are terse, one or two letters, and there is little built-in help. The user's guide is the way in, and it is worth reading before the first session.

## Install

```
brew install edbrowse
# Intended for Unix-like systems. Building from source needs pcre and libcurl development packages, and version 3.8.15 or later needs quickjs-ng.
```

## Try this

```
edbrowse --help
```
Prints the command-line options, a first look at how the program expects to be invoked.

```
cd doc; lynx -dump usersguide.html >usersguide.txt
```
From the README: converts the user's guide to plain text so you can read it in an editor before edbrowse is installed.

```
git clone https://github.com/edbrowse/edbrowse.wiki
```
Clones the project wiki, which holds tips, tricks and sample .ebrc configuration files.

## What's unique

It treats unattended web automation, such as cron jobs that submit forms and send mail, as a first-class use alongside ed-style editing. The project says that scripting is found nowhere else.

## Caveats

The README warns it is provided as-is and might trash your files or send bad data across the Internet, and the cryptic commands make the user's guide effectively required reading.

## Links

- [Homepage](https://edbrowse.org)
- [GitHub repository](https://github.com/edbrowse/edbrowse)
- [User's guide (online)](http://edbrowse.org/usersguide.html)
- [Wiki](https://github.com/edbrowse/edbrowse.wiki)
