---
name: anyquery
title: Anyquery
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, cli, mcp, plugins, sql, sqlite]
homepage: https://anyquery.dev
scout_score: 6
status: draft
---

# Anyquery

**TLDR;** A SQLite-based query engine that turns GitHub, Notion, Spotify, Gmail, CSV files and 40+ other sources into tables you can SELECT from and JOIN.

Anyquery is a SQL engine built on SQLite. Plugins expose each external service or file type as a table, so a query against your GitHub issues, a Google Sheet or a Parquet file uses the same dialect. Sources named in the brief include GitHub, Notion, Spotify, Gmail, Airtable, Apple Notes, Chrome, Todoist, CSV, Parquet and logs, with 40+ in total. Some sources, such as Notion, Airtable and Google Sheets, also accept INSERT, UPDATE and DELETE.

The pitch is that you stop learning one API or CLI per service. Because everything is a SQLite table, you can JOIN across sources that were never meant to meet. The homepage says it runs locally and that API tokens never leave the machine.

You can reach it three ways: an interactive shell, a MySQL-compatible server that tools like Metabase and TablePlus can connect to, and an MCP server so an LLM client can run real SQL against your own accounts. The underlying idea is old and appealing: if everything looks like a table, one query language covers all of it.

## Install

```
brew install anyquery
# then add plugins for the sources you want:
anyquery i github spotify notion
# some plugins need their own API tokens
```

## Try this

```
anyquery i github spotify notion
```
Installs your first plugins so those services show up as tables.

```
anyquery server &
```
Starts the MySQL-compatible server in the background so other tools can query your data.

```
mysql -u root -h 127.0.0.1 -P 8070
```
Connects a MySQL client to the running server, where you can run SELECT * FROM github; and similar queries.

## What's unique

Most tools in this space cover one source. This one puts 40+ apps, files and databases behind a single SQLite dialect, with JOINs across them, and ships an MCP server with one command.

## Caveats

Maintained by one person, with mixed signals on recent activity; the core is AGPL-3.0, each plugin has its own license, and some plugins need API tokens.

## Links

- [Homepage](https://anyquery.dev)
- [Documentation](https://anyquery.dev/docs)
- [Integrations registry](https://anyquery.dev/integrations)
- [GitHub repository](https://github.com/julien040/anyquery)
