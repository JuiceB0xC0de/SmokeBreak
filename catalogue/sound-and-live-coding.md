# Sound and live coding

Make noise, music, or audio structures from the terminal. Sequencers, synths, modem tones, morse, spatial audio, live-coded sound.

44 entries. [Back to the shelf](README.md)

## quick

- **[abcMIDI](../drafts/brew/abcmidi.md)**: Turns tunes written as plain text in abc notation into MIDI files, and back again, with a small kit of tools for transposing and inspecting them.  
  `abc-notation, audio, midi, music, text-to-music`
- **[adplay](../drafts/brew/adplay.md)**: A terminal player for 1990s AdLib and Sound Blaster OPL2 music files, using an emulated Yamaha chip, so no sound card is needed.  
  `adlib, audio, dos, opl2, retro`
- **[Alda](../drafts/brew/alda.md)**: A text-based music language: write notes in a plain file or REPL, run one command, and hear them played back through MIDI.  
  `audio, language, live-coding, midi, music`
- **[ebook2cw](../drafts/brew/ebook2cw.md)**: Turns a plain text file into Morse code audio, MP3 or OGG, so you can listen to a whole book sent in CW at the speed you choose.  
  `audio, cw, ham-radio, morse, text-to-speech`
- **[espeak-ng](../drafts/brew/espeak-ng.md)**: A tiny formant speech synthesizer that speaks over 100 languages from the terminal, built from modelled vocal-tract resonances instead of recordings.  
  `audio, formant-synthesis, language, speech, tts`
- **[libbs2b](../drafts/brew/libbs2b.md)**: A tiny headphone crossfeed filter that bleeds each stereo channel into the other ear, so music sounds less like it is stuck inside your skull.  
  `audio, crossfeed, dsp, headphones, library`
- **[libopenmpt](../drafts/brew/libopenmpt.md)**: A library and terminal player, openmpt123, that decodes tracker module music files, the compact song format of the demoscene and old PC games.  
  `audio, library, modules, retro, tracker`
- **[libxmp](../drafts/brew/libxmp.md)**: A C library that renders tracker module music (MOD, S3M, XM, IT and 90-plus other formats) into raw audio, keeping decades-old Amiga and PC songs playable.  
  `ancient, audio, library, preservation, tracker`
- **[mdxmini](../drafts/brew/mdxmini.md)**: A small C library and the mdxplay player that render MDX chiptunes, the FM-synth music format of Sharp's X68000 home computer, into audio.  
  `audio, c-library, chiptune, fm-synthesis, retro, x68000`
- **[minimodem](../drafts/brew/minimodem.md)**: A command-line software modem that turns text into audible FSK tones and decodes them back, using classic standards like Bell 103 and Bell 202.  
  `audio, fsk, modem, protocol, retro`
- **[morse](../drafts/brew/morse.md)**: A command-line Morse code trainer that adapts to your mistakes, plus a QSO generator that pipes simulated radio contacts into it for copying by ear.  
  `ancient, audio, ham-radio, morse, trainer`
- **[pmdmini](../drafts/brew/pmdmini.md)**: A small C library and a pmdplay command that play PMD chiptunes, the music format written for Japan's PC-98 computers in the 1990s.  
  `audio, chiptune, fm-synthesis, pc-98, retro`
- **[Rubber Band](../drafts/brew/rubberband.md)**: Change the speed of a recording without changing its pitch, or the pitch without the speed, from one command line.  
  `audio, dsp, library, pitch-shift, time-stretch`
- **[sc68](../drafts/brew/sc68.md)**: A player for Atari ST and Amiga soundchip music that ordinary players cannot open, with a command-line tool and a few extras installed by Homebrew.  
  `amiga, atari-st, audio, chiptune, retro`
- **[serialosc](../drafts/brew/serialosc.md)**: A daemon that turns monome grid and arc controllers into OSC devices, so any music software that speaks OSC can read their buttons and light their LEDs.  
  `audio, monome, needs-hardware, network, osc`
- **[SoX](../drafts/brew/sox.md)**: SoX is a command-line audio tool that converts sound files between formats and runs effects and filters on them, all from a shell pipeline.  
  `audio, cli, converter, effects`
- **[UADE](../drafts/brew/uade.md)**: Plays more than 200 old Amiga music formats by running the original Amiga player code inside a 68k CPU emulator, from the command line.  
  `amiga, audio, chiptune, emulation, retro, tracker`
- **[unixcw](../drafts/brew/unixcw.md)**: A Morse code tutor for the terminal: a small library and a few programs for learning to send and receive Morse.  
  `ancient, audio, morse, tui`
- **[xmp](../drafts/brew/xmp.md)**: A terminal player for tracker music files like MOD, S3M, XM and IT, the sample-and-pattern formats of the demoscene, with per-channel muting.  
  `audio, demoscene, retro, tracker, tui`

## afternoon

- **[AdPlug](../drafts/brew/adplug.md)**: A library that plays music from AdLib-era DOS games in dozens of original file formats, with no OPL sound chip required.  
  `adlib, audio, file-formats, library, opl, retro, reverse-engineering`
- **[aubio](../drafts/brew/aubio.md)**: A C library with command-line tools that listen to audio and print note onsets, pitch, beats and tempo as plain timestamps and numbers.  
  `audio, beat-tracking, cli, library, music-information-retrieval, pitch`
- **[ChucK](../drafts/brew/chuck.md)**: A programming language where time is a built-in concept, so you write code that makes sound and rewrite it while it plays.  
  `audio, generative, language, live-coding, music`
- **[PocketSphinx](../drafts/brew/cmu-pocketsphinx.md)**: A small, old-school speech recognizer from Carnegie Mellon that turns audio into line-delimited JSON, and can force-align a known transcript to word-level timestamps.  
  `audio, cli, cmu, json, speech-recognition`
- **[Codec 2](../drafts/brew/codec2.md)**: An open source speech codec that squeezes intelligible voice into 700 to 3200 bits per second, built for amateur digital radio.  
  `audio, c, codec, radio, speech`
- **[Csound](../drafts/brew/csound.md)**: A sound synthesis language from 1985 where you write instruments and a score as text, and the computer renders them into audio.  
  `audio, language, music, synthesis`
- **[ecasound](../drafts/brew/ecasound.md)**: A command-line multitrack audio recorder and effects processor, where oscillators and MIDI controllers can drive effect parameters while the sound plays.  
  `audio, cli, effects, multitrack, old-school, tui`
- **[Faust](../drafts/brew/faust.md)**: A functional language for sound: write a synth or effect once, then compile it to plugins, apps, web audio, and objects for Max, Pure Data and SuperCollider.  
  `audio, compiler, dsp, language, plugins, synthesis`
- **[FluidSynth](../drafts/brew/fluid-synth.md)**: A software synthesizer that turns MIDI into sound using SoundFont instrument banks, the software version of a hardware MIDI synth.  
  `audio, library, midi, soundfont, synthesizer`
- **[Icecast](../drafts/brew/icecast.md)**: Free server software from Xiph.org that takes an audio stream from a source and serves it to listeners over HTTP, the machinery behind many internet radio stations.  
  `audio, http, internet-radio, network, streaming`
- **[JACK](../drafts/brew/jack.md)**: A real-time audio server that lets any program's sound output feed another program's input, treating audio and MIDI as one patchable graph.  
  `audio, daemon, midi, real-time, routing`
- **[LADSPA SDK](../drafts/brew/ladspa-sdk.md)**: The reference kit for LADSPA, a deliberately tiny 2000-era audio plugin standard, with three small command-line hosts and example plugins you can run.  
  `ancient, audio, c, linux-audio, plugins`
- **[libltc](../drafts/brew/libltc.md)**: A small C library that turns audio into SMPTE timecode and back, using the Manchester-biphase buzz that film and video gear records onto an audio track.  
  `audio, c, library, smpte, timecode`
- **[libmapper](../drafts/brew/libmapper.md)**: A C library where instruments and software announce signals on a network, and mappings between them can be rewired at runtime with no central broker.  
  `c, instruments, library, live-performance, networking, osc`
- **[libmysofa](../drafts/brew/libmysofa.md)**: A small C library that reads SOFA files of head-related transfer functions, so you can ask how a sound from any direction reaches each ear.  
  `audio, c, hrtf, library, spatial-audio`
- **[Liquidsoap](../drafts/brew/liquidsoap.md)**: A scripting language for building radio stations and video streams, where playlists, crossfades and fallbacks are operators you wire together in a short file.  
  `audio, ffmpeg, language, radio, streaming, video`
- **[ltc-tools](../drafts/brew/ltc-tools.md)**: Command-line tools that generate and decode linear timecode, the SMPTE clock signal from film and video that is carried as an audible audio tone.  
  `audio, jack, protocol, smpte, timecode`
- **[mt32emu (Munt)](../drafts/brew/mt32emu.md)**: A software emulation of the Roland MT-32 synthesiser modules, the sound module behind a generation of DOS game music, usable as a library or through a Qt app.  
  `audio, emulation, library, midi, vintage-hardware`
- **[Open JTalk](../drafts/brew/open-jtalk.md)**: A Japanese text-to-speech system built from a chain of speech research tools, with a trained voice and dictionary you can inspect.  
  `audio, japanese, speech, tts`
- **[Snapcast](../drafts/brew/snapcast.md)**: Snapcast turns any audio source into a synchronized multiroom system, with every client playing the same stream within a fraction of a millisecond.  
  `audio, multiroom, network, streaming, sync`
- **[SoundTouch](../drafts/brew/sound-touch.md)**: A small C++ audio library, with a bundled command-line tool called soundstretch, that changes tempo and pitch independently or together, and can estimate a track's BPM.  
  `audio, bpm, library, pitch-shift, time-stretch, wav`
- **[STK (Synthesis ToolKit)](../drafts/brew/stk.md)**: A C++ library from Stanford's CCRMA of readable physical-model instruments and synthesis building blocks, written to teach how sound is made sample by sample.  
  `audio, c++, library, physical-modelling, synthesis`
- **[Vamp Plugin SDK](../drafts/brew/vamp-plugin-sdk.md)**: A plugin format for audio analysis: plugins listen to a file and return pitch curves, onset times and spectra instead of sound.  
  `audio, c++, dsp, library, music-information-retrieval`
- **[WaoN](../drafts/brew/waon.md)**: WaoN listens to a WAV file and writes out the notes it hears as a MIDI file, running a synthesiser's job in reverse.  
  `audio, fft, midi, old, transcription`
- **[zita-convolver](../drafts/brew/zita-convolver.md)**: A C++ library that convolves audio with very long impulse responses, like reverbs, at zero delay and moderate CPU cost, using non-uniform FFT partitions.  
  `audio, c++, convolution, dsp, library, reverb`
