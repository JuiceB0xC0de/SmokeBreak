---
name: netlistsvg
title: netlistsvg
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [quick, schematics, svg, verilog, visual, yosys]
homepage: https://github.com/nturley/netlistsvg
scout_score: 8
status: draft
---

# netlistsvg

**TLDR;** Turns a Yosys JSON netlist into an SVG schematic, so synthesised Verilog redraws itself as gates, wires and registers.

netlistsvg reads a JSON netlist, usually written by Yosys's `write_json` command, and draws it as an SVG schematic. The JSON can also be written by hand in JSON5. Output goes to `out.svg` unless you ask for another file. The README's examples include a digital counter and an analog resistor divider.

It reads one module, either the first one or the one marked top. Each cell type is matched against aliases in a skin file, which is an ordinary SVG. The skin supplies the icon and port positions for each cell. Cell types with no match get a generic box. Layout is handled by elkjs, a JavaScript port of the Eclipse ELK layered algorithm. The README compares it to `dot` in Graphviz.

The drawing follows the synthesised netlist, not your original HDL. How you run Yosys changes what you see. `prep` keeps inner modules as boxes, `-flatten` reduces everything to low-level logic cells, and `aigmap` rewrites the design as AND and NOT cells. The same Verilog can therefore be drawn three ways, which shows what a synthesis tool does to your code.

The skin is plain SVG with `s:` attributes tagging aliases, ports and sizes. You can restyle or replace the icons without touching code.

## Install

```
brew install netlistsvg
# Yosys is only needed to produce the JSON from Verilog; the Homebrew formula depends on node.
# Alternative from npm: npm install -g netlistsvg
```

## Try this

```
netlistsvg --help
```
Prints the usage and options for the renderer.

```
yosys -p "prep -top my_top_module -flatten; write_json output.json" input.v
```
Synthesises your Verilog into a flattened netlist of low-level logic cells and writes it as JSON.

```
netlistsvg output.json -o schematic.svg
```
Renders the JSON as a schematic in schematic.svg, which you can open in a browser.

## What's unique

The icons live in a plain SVG skin file, so you can restyle the schematic without code. The drawing comes from the synthesised netlist rather than the source HDL.

## Caveats

The README says the skin file format is unspecified until 1.0, it renders only one module, and I could not confirm recent activity from the README alone.

## Links

- [Project homepage (GitHub)](https://github.com/nturley/netlistsvg)
- [Online demo](https://nturley.github.io/netlistsvg)
- [Yosys write_json command docs](https://yosyshq.readthedocs.io/projects/yosys/en/latest/cmd/write_json.html)
