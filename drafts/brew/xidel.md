---
name: xidel
title: xidel
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, cli, html, json, scraping, xpath, xquery]
homepage: https://www.videlibri.de/xidel.html
scout_score: 5
status: draft
---

# xidel

**TLDR;** A single-binary command-line tool that fetches HTML, XML or JSON and queries it with XPath, XQuery, CSS selectors or JSONiq, including a full query language you can script in.

Xidel takes a URL, file or stdin and runs a query against the parsed document. The query can be XPath 3.0, XQuery 3.0, CSS 3 selectors, JSONiq, or a pattern-matching template. It follows redirects, keeps cookies, can follow links and submit forms, and prints results as plain text, XML, HTML, JSON or shell variables.

It began as the backend of the VideLibri library service and was released as a standalone tool in 2012. The author says the point is "to make it easy for anyone to parse any webpage", and he would rather people learn to write queries than ask him how to scrape a particular site.

The idea underneath is that XPath and XQuery are real query languages, not just selector syntax. XQuery is Turing-complete, so one command line can fetch pages, loop, branch and build new documents. The pattern-matching mode is stranger: you write a sample snippet of the page with placeholders like `{.}`, and Xidel matches it against the real document and extracts the values.

With `--output-format bash`, results can be eval'd straight into shell variables, which makes it a bridge between web documents and shell scripts.

## Install

```
brew install xidel
```

## Try this

```
xidel -e "(1 + 2 + 3) * 1000000000000 + 4 + 5 + 6 + 7.000000008"
```
Evaluates an XPath arithmetic expression with arbitrary precision. No input document is needed.

```
xidel https://example.org -f //a -e //title
```
Follows every link on the page and prints the title of each linked page.

```
xidel --xquery '<table>{for $i in 1 to 1000 return <tr><td>{$i}</td><td>{if ($i mod 2 = 0) then "even" else "odd"}</td></tr>}</table>' --output-format xml
```
Builds an HTML table of 1000 numbers labelled even or odd, using only an XQuery expression.

## What's unique

It bundles a full XPath/XQuery 3.0 interpreter, CSS selectors, JSONiq and template-style pattern matching in one binary. Most scraping tools offer only selectors.

## Caveats

The last official release is 0.9.8 from 2018, the homepage recommends unreleased 0.9.9 development builds, XPath 3.1 support is partial, and JSONiq is deprecated.

## Links

- [Xidel homepage (author's VideLibri site)](https://www.videlibri.de/xidel.html)
- [Online test service (CGI, from the README)](https://www.videlibri.de/cgi-bin/xidelcgi?data=<html><title>foobar</title></html>&extract=//title&raw=true)
