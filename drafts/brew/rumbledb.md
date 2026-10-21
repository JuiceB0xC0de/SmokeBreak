---
name: rumbledb
title: RumbleDB
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, java, json, jsoniq, query-language, spark, xml, xquery]
homepage: https://rumbledb.org/
scout_score: 5
status: draft
---

# RumbleDB

**TLDR;** A query engine that runs JSONiq and XQuery over messy nested data, on a laptop or scaled out across a Spark cluster.

RumbleDB takes a query written in JSONiq, a language built around FLWOR clauses (for, let, where, order by, return) for nested data, and runs it on Apache Spark. You point it at JSON, JSON Lines, XML, CSV, Parquet, Avro, libSVM or plain text, on local disk, HDFS, S3 or Azure blob storage. Results can come back as JSON, XML, CSV, Parquet, YAML and other formats. It also accepts W3C XQuery.

The stated reason it exists is a disagreement with the DataFrame approach. In the README's words: "RumbleDB exposes a query language rather than a DataFrame API, for more flexibility, more productivity but also because a lot of data simply will not fit in DataFrames." Data with missing fields, varying shapes and deep nesting does not fit a rigid table, and a declarative language can describe it directly.

The homepage says JSON navigation, FLWOR clauses and downward XML navigation are parallelized automatically across cores or a cluster, with count and sum-style pushdowns applied for you. You write the query, and Spark does the distribution. It also bundles RumbleML, which exposes Spark ML estimators and transformers as JSONiq function items, so model training can happen inside the query language.

The door here is the idea of a query language for trees instead of tables. XQuery and JSONiq come from the document-and-semi-structured-data world, and RumbleDB connects that tradition to big-data infrastructure.

## Install

```
brew install rumbledb
# Needs a JVM and Spark; the formula pulls in apache-spark and openjdk@21.
# Other routes listed on the homepage: pip install jsoniq, Docker, a standalone jar, or a thin jar for an existing Spark install.
```

## Try this

```
rumbledb --help
```
Lists the command-line options of the engine.

```
pip install jsoniq
```
Installs the Python edition, which the homepage lists as an installation route and which can be used from Jupyter.

## What's unique

It is a declarative nested-data query language on top of Spark rather than a DataFrame API, and it speaks both JSONiq and W3C XQuery. It also runs Spark ML inside the query language.

## Caveats

It is heavy, since it needs a JVM and Spark, and the homepage's 95% W3C compliance figure is self-reported; it appears maintained, but I could not confirm release dates.

## Links

- [Homepage](https://rumbledb.org/)
- [Documentation (latest official release)](https://docs.rumbledb.org/)
- [Jupyter sandbox notebook (Colab)](https://colab.research.google.com/github/RumbleDB/rumble/blob/master/RumbleSandbox.ipynb)
- [Source on GitHub](https://github.com/RumbleDB/rumble)
