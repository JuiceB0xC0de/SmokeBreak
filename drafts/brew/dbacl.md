---
name: dbacl
title: dbacl
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bayesian, old-school, spam, text-classification, unix]
homepage: https://dbacl.sourceforge.net/
scout_score: 5
status: draft
---

# dbacl

**TLDR;** A set of small Unix tools that learn from example text and then say which category a new document most resembles, using Bayesian statistics.

dbacl is a collection of command-line utilities for classifying text. You give it collections of example documents, one per category. It learns a model of each, then computes the probability that a new piece of text belongs to each category. The decision step can weigh the cost of different mistakes, so a wrongly discarded email can count for more than a wrongly kept one.

The homepage lists uses such as junk email filtering, web page screening, automated answering machines, email prioritization, topical news gathering, and even playing chess. The author is candid that the tools do not do all of this directly: "by concentrating on simple, powerful, and easily integrated tools these applications become possible." The pieces are meant to be glued together in shell scripts.

The idea underneath is a door into statistical text classification, the same family of techniques behind early spam filters. You combine prior beliefs with observed text and choose the class that minimizes expected cost. The name suggests a digram model, meaning two-character sequences, but the homepage does not spell out the mechanism. Reading the man page and tutorial is where the details would be.

The formula installs eight executables: bayesol, dbacl, hmine, hypex, mailcross, mailfoot, mailinspect and mailtoe. dbacl is the core, and the mail* names point at email-oriented helpers. The homepage does not describe the other tools in detail.

## Install

```
brew install dbacl
```

## Try this

```
dbacl --help
```
Prints the core classifier's options, the best way to see how training and classifying are invoked.

```
bayesol --help
```
Shows the options of the decision tool, which applies misclassification costs to pick a class.

```
mailinspect --help
```
Shows what the mail inspection helper expects, as a hint of how the tools are meant to work on email.

## What's unique

Most spam filters of its era were single applications. dbacl is a set of small composable Unix tools with a cost-aware decision step, built for shell scripts.

## Caveats

Maintenance status is unknown, the homepage shows no release dates and links to CVS, and it gives no example commands, so expect to read the man page.

## Links

- [Homepage](https://dbacl.sourceforge.net/)
