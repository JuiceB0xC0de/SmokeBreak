---
name: gotestwaf
title: gotestwaf
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, api, http, owasp, security, waf]
homepage: https://lab.wallarm.com/test-your-waf-before-hackers/
scout_score: 5
status: draft
---

# gotestwaf

**TLDR;** Fires OWASP-style attack requests at a web application firewall or API gateway, then reports which ones were blocked and which slipped through.

GoTestWAF is a Go command-line tool from Wallarm that tests web application security products: WAFs, API gateways, IPS, API security proxies. Point it at a URL and it sends malicious HTTP requests built from YAML test cases, then sorts each response into blocked, bypassed, or unresolved. The result is a scored report in the console, or as PDF, HTML, or JSON.

The core idea is a three-part model: payload, encoder, placeholder. A test case lists payloads, encoders (Base64, JSUnicode, URL, XML Entity and others), and places in the request to put them (URL path, URL parameter, header, JSON body, SOAP body, gRPC, or a raw request). The tool sends every combination, so 2 payloads x 3 encoders x 1 placeholder becomes 6 requests. One short file expands into many request shapes, and you can see where a filter stops recognising the same attack once it is wrapped differently.

Wallarm's stated reason for open-sourcing it: WAF evaluation tends to focus on false positives and ignore false negatives, and there was no simple way for a developer or QA engineer to produce a coverage report. A response counts as blocked by default on a 403 status, or by a regex you supply. It counts as bypassed on a 200 or 404, or a pass regex. Those criteria are configurable, and that is where much of the learning sits.

With an OpenAPI 3.0 file, it builds valid requests from your own API description and substitutes attack vectors into them. That tests the filter against traffic shaped like the real application's, not blind fuzzing.

## Install

```
brew install gotestwaf
# Docker route from the README: docker pull wallarm/gotestwaf
# Only run it against systems you are authorized to test. PDF reports in native mode need Google Chrome; otherwise use --reportFormat html.
```

## Try this

```
gotestwaf --help
```
Lists the flags for target URL, report format, block and pass criteria, and OpenAPI input.

```
make modsec
```
From a cloned repo, starts a demo ModSecurity CRS container on port 8080 to use as a safe target.

```
docker run --rm --network="host" -v ${PWD}/reports:/app/reports wallarm/gotestwaf --url=http://127.0.0.1:8080 --noEmailReport
```
Scans the local ModSecurity demo, skips the email prompt, and saves the report into ./reports.

## What's unique

One YAML test expands across encoders and request locations, and the OpenAPI mode wraps attacks in requests valid for your own API. Bypass results are therefore more meaningful than raw fuzzing.

## Caveats

Maintenance status is unclear from the README, the OWASP Core Rule Set tests need a conversion step, gRPC checks need a live endpoint, and the default block and pass criteria can misjudge some responses.

## Links

- [Homepage (Wallarm blog post)](https://lab.wallarm.com/test-your-waf-before-hackers/)
- [GitHub repository and README](https://github.com/wallarm/gotestwaf)
- [Docker Hub image](https://hub.docker.com/r/wallarm/gotestwaf)
