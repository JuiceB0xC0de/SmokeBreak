---
name: jolie
title: Jolie
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, jvm, language, microservices, protocols]
homepage: https://www.jolie-lang.org/
scout_score: 8
status: draft
---

# Jolie

**TLDR;** A programming language where the basic unit is a service, not an object or function, so one program can run locally, remotely, or over several protocols at once.

Jolie is a language for building systems out of services. A program is a service with input ports (a location, a protocol, and interfaces) and a main block that handles operations. Its homepage puts the premise this way: "The basic building blocks of software are not objects or functions, but rather services that can be relocated and replicated as needed. A composition of services is a service."

It is contract-first. You declare types and interfaces up front, with operations such as requestResponse and oneWay, and the interpreter handles data transformation between types. The same logic can be exposed over several protocols on separate ports. The homepage shows HTTP/JSON, SOAP, and a binary protocol called SODEP. Its sample takes a JSON HTTP request with a name field and returns a greeting string.

Workflow is built into the syntax. The homepage example `login( credentials )() { checkCredentials }; { publish( x ) | edit( y ) }` uses `;` for sequence and `|` for parallel. Fault handling uses scope and install, so handlers can be changed at runtime. Java and JavaScript can be embedded, and new protocols can be added through a Java API.

The idea underneath is that microservice concerns like communication, protocols, and composition become language constructs instead of framework glue. The homepage also pitches it for splitting a monolith across machines without changing its logic. The brew package ships a toolbox beyond the interpreter, including converters such as wsdl2jolie, openapi2jolie, jolie2java, and jolie2wsdl, plus joliedoc and joliemock.

## Install

```
brew install jolie
# pulls in openjdk as a dependency; Jolie runs on the Java runtime
```

## Try this

```
jolie --help
```
Lists the interpreter's options, a safe first look before you write any service.

```
joliedoc --help
```
Shows how to generate documentation from a service's interfaces.

```
joliemock --help
```
Shows the options for the mock tool, which comes with the package.

## What's unique

Services, ports, protocols, and parallel composition are part of the language itself, not a framework on top. One program can be served over HTTP/JSON, SOAP, and a binary protocol simultaneously.

## Caveats

I could not reach the download or docs pages, so install steps and maintenance status are unverified. The homepage shows a 2014-2024 copyright range but no release dates.

## Links

- [Jolie homepage](https://www.jolie-lang.org/)
