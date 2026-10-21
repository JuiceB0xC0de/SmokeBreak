---
name: glslviewer
title: glslViewer
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [generative, glsl, live-coding, opengl, quick, shaders, visual]
homepage: https://patriciogonzalezvivo.com/2015/glslViewer/
scout_score: 6
status: draft
---

# glslViewer

**TLDR;** A console tool that renders GLSL shaders in a window and reloads them whenever you save the file, driven by stdin or OSC.

glslViewer is described by its README as "a flexible console-base OpenGL Sandbox to display 2D/3D GLSL shaders without the need of an UI." You give it a fragment shader, optionally a vertex shader, textures, cubemaps or a 3D model (OBJ, PLY, LST, GLTF), and it opens a window and draws. Edit the file in any editor and the picture updates on save.

There is no built-in editor or control panel. The interface is plain text: commands go in through POSIX stdin/stdout or through OSC messages. These can add or remove #defines and set custom uniforms (float, int, vec2, vec3, vec4). Any script, language or UI can steer a running shader, and the README mentions wrapping it with your own UI or a Python module.

Underneath is the idea of a shader as a function from pixel position (and time, and whatever uniforms you feed it) to colour, run for every pixel in parallel. Having a viewer that stays out of the way makes that easy to explore. It resolves #include dependencies and generates defines for platform, buffers, render passes, geometry attributes and materials.

The feature list goes well beyond a basic viewer: video, camera and audio textures, PBR 3D models, headless rendering, PNG sequence export, a HoloPlay Looking Glass mode and a screensaver mode. Homebrew installs three executables: glslViewer, glslScreenSaver and glslThumbnailer.

## Install

```
brew install glslviewer
# needs a machine with OpenGL and a display; the formula pulls in ffmpeg and glfw
```

## Try this

```
glslViewer --help
```
Lists the command-line options, a good first look at what inputs and modes it accepts.

```
glslScreenSaver --help
```
Shows how the screensaver executable that ships with the formula is invoked.

```
glslThumbnailer --help
```
Shows the options for the thumbnailer executable that comes with the formula.

## What's unique

It is a shader sandbox with no UI of its own, controlled by stdin/stdout and OSC so any script can drive a live shader. It packs video, audio, camera, 3D models and headless export into one console tool.

## Caveats

The README and homepage show no release date or recent activity, and the README gives no install commands, only wiki pages for compiling from source.

## Links

- [Homepage](https://patriciogonzalezvivo.com/2015/glslViewer/)
- [GitHub repository and README](https://github.com/patriciogonzalezvivo/glslViewer)
- [Wiki: Installing](https://github.com/patriciogonzalezvivo/glslViewer/wiki/Installing)
- [Wiki: Using GlslViewer](https://github.com/patriciogonzalezvivo/glslViewer/wiki/Using-GlslViewer)
