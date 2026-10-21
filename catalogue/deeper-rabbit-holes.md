# Deeper rabbit holes

Real scientific or mathematical software you can actually run at home. Seismology, particle physics, groundwater, RNA folding, knots, digital evolution. Days-off material.

175 entries. [Back to the shelf](README.md)

## quick

- **[h3](../drafts/brew/h3.md)**: Uber's hexagonal geospatial index: turn a latitude and longitude into a short hex cell ID, then ask for that hexagon's corners or center.  
  `c-library, geospatial, hexagons, maps, math`
- **[hebcal](../drafts/brew/hebcal.md)**: A command-line Jewish calendar that prints holidays, Hebrew dates, Torah portions, candle-lighting times and daily study cycles for any Gregorian year.  
  `astronomy, calendar, cli, dates`
- **[opentimestamps-client](../drafts/brew/opentimestamps-client.md)**: Prove a file existed at a given time by anchoring its hash in Bitcoin, with no account, no fees, and no trusted notary.  
  `bitcoin, cryptography, network, protocol, timestamping`
- **[pict](../drafts/brew/pict.md)**: Microsoft's pairwise test generator turns a list of parameters and values into a small table of test cases that still covers every pair of values.  
  `combinatorics, covering-arrays, math, testing`
- **[primecount](../drafts/brew/primecount.md)**: Counts the primes up to 10^31 without listing them, using the combinatorial algorithms behind prime counting world records.  
  `library, math, number-theory, openmp, primes`
- **[primesieve](../drafts/brew/primesieve.md)**: A very fast prime number generator that counts or prints primes, twin primes and larger k-tuplets up to 2^64, and doubles as a CPU stress test.  
  `c++, math, number-theory, primes, stress-test`
- **[Prodigal](../drafts/brew/prodigal.md)**: Prodigal reads bacterial DNA in FASTA format and predicts where the protein-coding genes are, with no training data, in about ten seconds for E. coli.  
  `bacteria, bioinformatics, dna, genomics, science`
- **[satellite-tracker](../drafts/brew/satellite-tracker.md)**: A terminal app that tracks satellites in real time on a scrolling world map, using live orbital data and the SGP4 model to predict where they go next.  
  `astrodynamics, rust, satellites, science, sgp4, tui`
- **[spigot](../drafts/brew/spigot.md)**: A command-line calculator by Simon Tatham that prints digits of pi, e and other expressions one at a time, never rounding wrongly, until you stop it.  
  `calculator, exact-arithmetic, math, pi`
- **[sss-cli](../drafts/brew/sss-cli.md)**: Split a secret into shares with Shamir's scheme, then recover it from any threshold subset, with tamper detection built in.  
  `cryptography, math, rust, secret-sharing`

## afternoon

- **[Alloy Analyzer](../drafts/brew/alloy-analyzer.md)**: Write a small model of a system in a relational logic language, and a SAT-based analyzer hunts for examples and counterexamples to your design.  
  `formal-methods, gui, java, modeling, sat`
- **[Arcade Learning Environment](../drafts/brew/arcade-learning-environment.md)**: A framework that turns Atari 2600 games into environments for AI agents: send a joystick action, get back the screen, the score, and a game-over flag.  
  `atari, emulator, gymnasium, python, reinforcement-learning, research`
- **[Argyll CMS](../drafts/brew/argyll-cms.md)**: A suite of 47 command line tools that measure colour with a sensor and build ICC profiles for monitors, printers, scanners and cameras.  
  `color, display, icc, needs-hardware, science`
- **[aspcud](../drafts/brew/aspcud.md)**: A package dependency solver that hands the install-or-conflict puzzle to an answer set programming engine, so the logic is declared rather than coded.  
  `asp, cudf, logic-programming, packaging, solvers`
- **[Astrometry.net](../drafts/brew/astrometry-net.md)**: Give it a photo of the night sky with no location info and it works out where in the sky the camera was pointing.  
  `astronomy, fits, math, science, visual`
- **[Augustus](../drafts/brew/augustus.md)**: A gene finder that reads raw eukaryotic genome sequence and predicts where genes, exons, introns and alternative transcripts sit, and can be retrained for a new species.  
  `bioinformatics, gene-prediction, genomics, science`
- **[Badread](../drafts/brew/badread.md)**: A command-line simulator that generates deliberately flawed DNA long reads, with separate dials for chimeras, junk, adapters, glitches and error rates.  
  `genomics, python, science, sequencing, simulation`
- **[Baysor](../drafts/brew/baysor.md)**: Baysor assigns each detected RNA molecule in a spatial transcriptomics image to a cell, using positions and gene identity, with or without a prior segmentation.  
  `bayesian, bioinformatics, science, segmentation, spatial-transcriptomics`
- **[bedtools](../drafts/brew/bedtools.md)**: A suite of small Unix tools that treat stretches of a genome as sets, so you can intersect, merge and subtract them in a pipe.  
  `bioinformatics, genomics, science, sets, unix-pipes`
- **[BioSig](../drafts/brew/biosig.md)**: An open source library and set of converters for EEG, ECG and other biosignal file formats, built so researchers can read and write each other's recordings.  
  `ecg, eeg, file-formats, library, science`
- **[Bitwuzla](../drafts/brew/bitwuzla.md)**: An SMT solver that decides whether logical formulas over bit-vectors, floating-point numbers and arrays can be satisfied, the engine behind much program verification.  
  `bit-vectors, floating-point, logic, smt, solver, verification`
- **[breseq](../drafts/brew/breseq.md)**: A pipeline that compares sequencing reads from an evolved microbe against its ancestor's genome and writes an annotated HTML report of every mutation it finds.  
  `bioinformatics, dna, evolution, genomics, science`
- **[bup](../drafts/brew/bup.md)**: A backup tool that cuts files into chunks with a rolling checksum and stores them as git packfiles, so repeated backups only add what changed.  
  `backup, deduplication, git, python, storage`
- **[CaDiCaL](../drafts/brew/cadical.md)**: A readable, competition-winning SAT solver: hand it a Boolean formula in DIMACS format and it tells you whether any assignment satisfies it.  
  `library, logic, math, sat, solver`
- **[cddlib](../drafts/brew/cddlib.md)**: A C library and set of command-line tools that convert convex polyhedra between inequalities and corner points, with exact rational arithmetic available.  
  `geometry, library, linear-programming, math, polyhedra`
- **[cdsclient](../drafts/brew/cdsclient.md)**: Command-line clients for the CDS astronomy archives in Strasbourg: pipe in sky coordinates, get back stars and sources from professional surveys.  
  `astronomy, catalogues, cli, network, science`
- **[clingo](../drafts/brew/clingo.md)**: A solver for answer set programming: describe a puzzle or combinatorial problem as logic rules, and clingo computes every solution that satisfies them.  
  `asp, declarative, logic, math, solver`
- **[CLooG](../drafts/brew/cloog.md)**: CLooG takes a polyhedron described as affine inequalities and prints the nested for-loops that visit every integer point inside it exactly once.  
  `compiler, library, loops, math, polyhedral`
- **[cmix](../drafts/brew/cmix.md)**: A lossless compressor that mixes about 2,000 predictive models and an LSTM to squeeze files smaller than almost anything, at the cost of hours of CPU and tens of gigabytes of RAM.  
  `compression, machine-learning, math, prediction`
- **[CoACD](../drafts/brew/coacd.md)**: Splits a 3D triangle mesh into a small set of convex pieces, chosen so collisions behave like the original shape.  
  `3d, geometry, math, mesh, physics`
- **[COLMAP](../drafts/brew/colmap.md)**: Feed it a folder of photos and it works out where each camera stood, then builds a 3D point cloud and mesh of the scene.  
  `3d, computer-vision, math, photogrammetry, science, visual`
- **[CppAD](../drafts/brew/cppad.md)**: A C++ template library that turns any function you can write in C++ into one that also gives exact derivatives, with no formulas worked out by hand.  
  `automatic-differentiation, c++, library, math`
- **[CryptoMiniSat](../drafts/brew/cryptominisat.md)**: A SAT solver that decides whether a Boolean formula can be satisfied, then hands back a working assignment or a proof that none exists.  
  `library, logic, math, sat, solver`
- **[cspice](../drafts/brew/cspice.md)**: NASA JPL's SPICE toolkit, the library and utilities real space missions use to compute where spacecraft, planets and instruments are and how they relate.  
  `library, math, orbital-mechanics, science, space`
- **[Cuba](../drafts/brew/cuba.md)**: A library from particle physics that integrates functions over many dimensions, with four different algorithms behind one calling interface so you can cross-check answers.  
  `integration, library, math, monte-carlo, physics, science`
- **[cuttlefish](../drafts/brew/cuttlefish.md)**: Builds compacted de Bruijn graphs from genome FASTA or sequencing reads, using disk-backed memory so it scales to collections of 150,000 bacterial genomes.  
  `bioinformatics, genomics, graphs, rust, science`
- **[DepQBF](../drafts/brew/depqbf.md)**: A research solver for quantified boolean formulae: SAT with 'for all' and 'exists' bolted on, a step up the complexity ladder you can run on a file.  
  `c-library, complexity, logic, math, qbf, solver`
- **[Dynare](../drafts/brew/dynare.md)**: Free software where you write a macroeconomic model nearly as it appears on paper, and it solves, simulates and estimates it for you.  
  `economics, math, octave, science, simulation`
- **[eccodes](../drafts/brew/eccodes.md)**: ECMWF's toolkit for reading and writing GRIB and BUFR, the packed binary formats weather centres use to exchange forecasts and observations.  
  `bufr, file-formats, grib, library, science, weather`
- **[Enzyme](../drafts/brew/enzyme.md)**: An LLVM plugin that computes derivatives of existing compiled code, so C, Rust, Julia or Fortran functions get gradients without being rewritten.  
  `automatic-differentiation, compilers, llvm, math`
- **[E (eprover)](../drafts/brew/eprover.md)**: A research-grade automated theorem prover: give it axioms and a conjecture in first-order logic, and it searches for a proof.  
  `logic, math, science, theorem-proving`
- **[FastANI](../drafts/brew/fastani.md)**: Estimates how similar two bacterial genomes are in seconds, using MinHash mapping instead of alignment, and shows where species boundaries fall.  
  `bioinformatics, genomics, minhash, science`
- **[FastGA](../drafts/brew/fastga.md)**: A whole-genome aligner that compares two genome assemblies directly through their indexes and finds all local alignments, for example two 2 Gbp bat genomes in about five minutes on 8 cores.  
  `alignment, bioinformatics, genomics, science`
- **[FastK](../drafts/brew/fastk.md)**: A k-mer counter by Gene Myers that turns DNA reads into frequency histograms, tables and per-read profiles, with set-logic tools for combining the results.  
  `bioinformatics, c, dna, genomics, science`
- **[FastME](../drafts/brew/fastme.md)**: Builds evolutionary trees from distance matrices or sequence alignments, using Balanced Minimum Evolution to beat Neighbor Joining at similar speed.  
  `biology, math, phylogenetics, science`
- **[Flecs](../drafts/brew/flecs.md)**: A small C and C++ library that organizes simulations as plain data plus functions, handling millions of entities per frame, with a browser explorer for inspecting the running program.  
  `c, cpp, ecs, games, generative, library, simulation`
- **[Flye](../drafts/brew/flye.md)**: Flye assembles whole genomes from noisy long sequencing reads using repeat graphs, and a bacterial genome runs on a laptop in a couple of CPU hours.  
  `assembly, bioinformatics, genomics, graphs, science`
- **[FORM](../drafts/brew/form.md)**: A symbolic algebra system from high-energy physics that rewrites huge expressions by pattern matching and keeps them on disk instead of in RAM.  
  `math, physics, symbolic-algebra, term-rewriting`
- **[fplll](../drafts/brew/fplll.md)**: A lattice reduction toolkit: feed it a matrix of integer vectors and it returns a better basis, or solves shortest and closest vector problems.  
  `cryptography, lattices, library, math`
- **[FreeSASA](../drafts/brew/freesasa.md)**: Give it a protein structure file and it reports how much of each atom's surface a water molecule could touch, using a rolling-ball algorithm from the 1970s.  
  `biophysics, c-library, pdb, proteins, science`
- **[FriCAS](../drafts/brew/fricas.md)**: A free computer algebra system for exact, symbolic mathematics, forked from Axiom, with its algebra library written in a strongly typed language called Spad.  
  `axiom, computer-algebra, math, spad, symbolic`
- **[fst](../drafts/brew/fst.md)**: A Rust library that stores huge sorted sets and maps as compact finite state machines you can search directly, including typo-tolerant queries.  
  `automata, data-structures, library, rust, search`
- **[Gambit](../drafts/brew/gambit.md)**: Gambit computes Nash equilibria and quantal response equilibria for finite games, from a GUI, a set of command-line solvers, or Python.  
  `game-theory, math, nash-equilibrium, python, science`
- **[Gecode](../drafts/brew/gecode.md)**: A C++ constraint solver: you describe variables and rules, and it searches for assignments that satisfy them, with MiniZinc front ends installed alongside.  
  `c++, constraint-programming, math, minizinc, solver`
- **[gemmi](../drafts/brew/gemmi.md)**: A command-line toolkit for reading, searching and converting protein structure files, with a CIF-aware grep that can sweep the whole Protein Data Bank archive.  
  `cif, cli, crystallography, library, proteins, science`
- **[geogram](../drafts/brew/geogram.md)**: A C++ geometry library from Inria research code, with Delaunay, Voronoi, remeshing and boolean ops, plus a mesh viewer and demo programs to poke at.  
  `c++, delaunay, geometry, library, mesh, visual, voronoi`
- **[gmp-ecm](../drafts/brew/gmp-ecm.md)**: A command-line implementation of the Elliptic Curve Method, which hunts for prime factors of large integers using arithmetic on elliptic curves.  
  `cryptography, factoring, math, number-theory`
- **[GMT (Generic Mapping Tools)](../drafts/brew/gmt.md)**: About 100 command-line tools that turn tables and grids of data into publication-quality maps, contour plots, 3D views and animations.  
  `geoscience, maps, plotting, science, visual`
- **[Gnuastro](../drafts/brew/gnuastro.md)**: An official GNU package of 27 command-line programs for astronomical images and tables, from cropping and warping to NoiseChisel source detection, all sharing one interface.  
  `astronomy, fits, gnu, images, science`
- **[gpredict](../drafts/brew/gpredict.md)**: A desktop app that tracks satellites in real time, draws their orbits on maps and radar plots, and predicts when they will pass over you.  
  `gui, orbits, satellites, science, simulation`
- **[graph-tool](../drafts/brew/graph-tool.md)**: A Python network analysis library with a C++ Boost core, known for fast graph algorithms and statistical community detection that tries to avoid overfitting.  
  `graphs, library, math, network-science, python, statistics`
- **[Grin](../drafts/brew/grin.md)**: A small, deliberately minimal implementation of Mimblewimble, a cryptocurrency protocol with no addresses, no visible amounts, and a chain that can shed old data.  
  `cryptocurrency, cryptography, mimblewimble, protocol`
- **[GTS: the GNU Triangulated Surface Library](../drafts/brew/gts.md)**: A C library and small toolset for 3D triangle meshes, with robust boolean operations, Delaunay triangulation and STL conversion, hiding behind many other programs.  
  `c, geometry, library, math, mesh`
- **[HEALPix](../drafts/brew/healpix.md)**: A way of cutting a sphere into equal-area pixels, built for mapping the cosmic microwave background, with command-line tools for analysing full-sky maps.  
  `astronomy, cosmology, fits, math, science, sphere`
- **[HElib](../drafts/brew/helib.md)**: A C++ library for homomorphic encryption: add and multiply numbers while they stay encrypted, so the machine doing the math never sees the data.  
  `c++, cryptography, homomorphic-encryption, library, math`
- **[HMMER](../drafts/brew/hmmer.md)**: A toolkit for building statistical profiles of protein or DNA families and searching sequence databases for distant relatives that BLAST-style pairwise search can miss.  
  `bioinformatics, hmm, protein, science, sequence-search`
- **[HyPhy](../drafts/brew/hyphy.md)**: Fits evolutionary models to gene sequences and a tree, then tests where natural selection or recombination left marks. It is the engine behind datamonkey.org.  
  `biology, evolution, phylogenetics, science, statistics`
- **[Icarus Verilog](../drafts/brew/icarus-verilog.md)**: A free Verilog compiler and simulator runtime that lets you write digital circuits as code and run them on your laptop, no hardware needed.  
  `compiler, digital-logic, hardware-design, simulation, verilog`
- **[InChI](../drafts/brew/inchi.md)**: Turns a molecule's structure into a canonical text string and a 27-character hash, so chemical structures can be searched and compared like words.  
  `c-library, cheminformatics, chemistry, identifiers, science`
- **[IQ-TREE 3](../drafts/brew/iqtree3.md)**: Command-line software that builds evolutionary trees from DNA or protein alignments by maximum likelihood, and can also simulate sequences to test itself against.  
  `biology, phylogenetics, science, statistics`
- **[JAGS](../drafts/brew/jags.md)**: A command-line Gibbs sampler that runs Bayesian models written in the BUGS language, so you can do MCMC simulation at home.  
  `bayesian, math, mcmc, simulation, statistics`
- **[Jellyfish](../drafts/brew/jellyfish.md)**: Jellyfish counts every substring of length k in DNA sequence files, quickly and with little memory, a basic step in many genome analyses.  
  `bioinformatics, dna, genomics, k-mers, science`
- **[Julius](../drafts/brew/julius.md)**: A speech recognition decoder from 1997 that turns audio into words using models you supply, small enough to run on a microcontroller-class budget.  
  `ancient, audio, japanese, science, speech-recognition`
- **[KataGo](../drafts/brew/katago.md)**: A Go engine that taught itself to play at top levels from self-play alone, and tells you estimated score and territory, not just win rate.  
  `ai, game, go, neural-network, self-play`
- **[kim-api](../drafts/brew/kim-api.md)**: A shared interface and curated catalogue of interatomic potentials, so one model ID runs unchanged in LAMMPS, ASE, DL_POLY and other molecular simulation codes.  
  `library, molecular-dynamics, science, simulation`
- **[Kissat](../drafts/brew/kissat.md)**: A competition-winning SAT solver in plain C that decides whether a Boolean formula can be satisfied, and a door into how modern solvers work.  
  `logic, math, sat, science, solver`
- **[KraftKit](../drafts/brew/kraftkit.md)**: Build and boot unikernels, tiny single-purpose VMs that bundle an app with a minimal library OS, using a Docker-like workflow and the kraft command.  
  `containers, firecracker, go, qemu, unikernel, virtualization`
- **[Kraken 2](../drafts/brew/kraken2.md)**: Kraken 2 labels DNA sequencing reads with the organisms they came from by matching k-mer minimizers against a reference database.  
  `bioinformatics, genomics, k-mer, metagenomics, needs-big-disk, science`
- **[kwok](../drafts/brew/kwok.md)**: Builds Kubernetes clusters full of fake nodes and pods, so you can watch a control plane cope with thousands of machines on a laptop.  
  `control-plane, kubernetes, scale, simulation`
- **[LAMMPS](../drafts/brew/lammps.md)**: A molecular dynamics simulator from Sandia National Laboratories: write a script describing atoms and forces, and it steps the physics forward for you.  
  `materials, molecular-dynamics, mpi, science, simulation`
- **[lastz](../drafts/brew/lastz.md)**: A DNA pairwise aligner from Penn State's Miller Lab that lines up whole chromosomes, short reads, or a sequence against itself, and still takes BLASTZ's old command-line syntax.  
  `alignment, bioinformatics, dna, genomics, science`
- **[Leela Zero](../drafts/brew/leela-zero.md)**: An open reimplementation of AlphaGo Zero: a Go engine whose neural network learned the game purely from self-play, trained in public by volunteers.  
  `ai-history, alphago, go, gtp, mcts, neural-network, opencl`
- **[Lensfun](../drafts/brew/lensfun.md)**: An open database of camera lens characteristics plus a library that uses it to undo distortion, colour fringing and vignetting in photos.  
  `image-processing, library, optics, photography`
- **[libaribcaption](../drafts/brew/libaribcaption.md)**: A C++ library that decodes and renders ARIB STD-B24, the closed-caption system of Japanese digital TV, so video players can display captions as a television does.  
  `broadcast, c++, captions, library, protocol`
- **[libchaos](../drafts/brew/libchaos.md)**: A C++11 library that builds hash functions and random generators from chaotic systems, with time, space and key as the dials.  
  `c++, hashing, library, math, random`
- **[libpostal](../drafts/brew/libpostal.md)**: A C library that parses street addresses from any country into labeled parts, trained on a billion addresses built from OpenStreetMap data.  
  `addresses, c, library, nlp, openstreetmap`
- **[libquantum](../drafts/brew/libquantum.md)**: A C library that simulates quantum registers, gates and measurements on an ordinary computer, with Shor's and Grover's algorithms included.  
  `c, library, quantum, science, simulation`
- **[link-grammar](../drafts/brew/link-grammar.md)**: A parser that draws English sentences as ASCII diagrams of typed links between words, from a 1991 theory of grammar that still runs.  
  `language, library, linguistics, nlp, parser`
- **[ltl2ba](../drafts/brew/ltl2ba.md)**: Turns a linear temporal logic formula, such as 'always, if request then eventually grant', into a Büchi automaton you can feed to the Spin model checker.  
  `automata, formal-methods, logic, math, model-checking`
- **[MAFFT](../drafts/brew/mafft.md)**: A multiple sequence alignment program that lines up many protein or DNA sequences at once, with speed and accuracy settings you pick between.  
  `bioinformatics, fft, math, science, sequences`
- **[Magics](../drafts/brew/magics.md)**: ECMWF's own weather-map plotting library: feed it GRIB, BUFR or NetCDF data and it draws contours, wind fields and graphs as PNG, PDF or SVG.  
  `library, python, science, visual, weather`
- **[Manifold](../drafts/brew/manifold.md)**: A C++ geometry library whose mesh Boolean operations are meant to always return a valid closed solid, with a web playground to try it.  
  `c++, cad, geometry, library, math, mesh`
- **[Maxima](../drafts/brew/maxima.md)**: A free computer algebra system descended from MIT's 1960s Macsyma: type an expression, get exact symbolic answers for calculus, algebra and more.  
  `computer-algebra, lisp, math, plotting, symbolic`
- **[METIS](../drafts/brew/metis.md)**: Classic C programs that split big graphs and meshes into balanced pieces and reorder sparse matrices, the quiet machinery behind a lot of scientific computing.  
  `c, graphs, math, science, sparse-matrices`
- **[Metview](../drafts/brew/metview.md)**: ECMWF's own weather-forecaster workstation, with an icon-driven GUI and a Python API, installable with one brew command.  
  `meteorology, python, science, visual, weather`
- **[miniprot](../drafts/brew/miniprot.md)**: Aligns a protein sequence to a whole genome, finding the introns and frameshifts in between, which is how new genomes get their genes marked.  
  `alignment, bioinformatics, genomics, proteins, science`
- **[MiniSat](../drafts/brew/minisat.md)**: A small, readable SAT solver that decides whether a Boolean formula can be satisfied, and a classic door into constraint solving.  
  `constraint-solving, math, sat`
- **[MiniZinc](../drafts/brew/minizinc.md)**: A constraint modelling language where you describe a puzzle or scheduling problem and let interchangeable solvers find the answer.  
  `constraints, language, math, optimisation, solvers`
- **[Minuit2](../drafts/brew/minuit2.md)**: CERN's C++ function minimizer, descended from 1970s Fortran MINUIT, that fits parameters and reports asymmetric errors for chi-square and likelihood fits.  
  `c++, library, math, science, statistics`
- **[MMseqs2](../drafts/brew/mmseqs2.md)**: A fast search and clustering suite for protein and nucleotide sequences, built as a much quicker alternative to BLAST for huge datasets.  
  `bioinformatics, clustering, proteins, science, search`
- **[MODFLOW 6](../drafts/brew/modflow6.md)**: The USGS's groundwater simulator: describe an aquifer, its wells and rivers in text files, and mf6 computes how the water moves through it.  
  `fortran, groundwater, hydrology, science, simulation`
- **[Montage](../drafts/brew/montage.md)**: Caltech's astronomy toolkit that reprojects, background-matches and stitches FITS sky images into custom mosaics, as about seventy small command-line programs.  
  `astronomy, c, fits, image-processing, python, science`
- **[MrBayes](../drafts/brew/mrbayes.md)**: A command-line program that estimates evolutionary trees from DNA, protein or trait data using Bayesian MCMC, the standard way to ask how species are related.  
  `bayesian, math, mcmc, phylogenetics, science`
- **[msieve](../drafts/brew/msieve.md)**: A public-domain C library and small command-line tool that factors big integers, from quick trial division up to the quadratic sieve and an unfinished number field sieve.  
  `c, cryptography, factoring, math, number-theory`
- **[msolve](../drafts/brew/msolve.md)**: A command-line solver that finds exact solutions to systems of polynomial equations using Groebner bases, returning rational boxes instead of floating-point guesses.  
  `computer-algebra, groebner-bases, math, polynomials, science`
- **[MUMmer](../drafts/brew/mummer.md)**: A suite for aligning whole genomes using suffix trees: feed it two FASTA files, get back coordinates, SNPs, and a classification of rearrangements.  
  `alignment, bioinformatics, fasta, genomics, science`
- **[nauty](../drafts/brew/nauty.md)**: Research-grade software that finds the symmetries of graphs, plus about fifty tools that generate every non-isomorphic graph of a given size.  
  `combinatorics, graphs, math, science`
- **[NEST](../drafts/brew/nest.md)**: A simulator for networks of spiking neurons, running since 1994 and scaling from a laptop to supercomputers, driven from Python.  
  `neuroscience, python, science, simulation`
- **[ngspice](../drafts/brew/ngspice.md)**: An open source SPICE simulator: describe an analog or digital circuit as a text netlist, run it, and plot the voltages and currents.  
  `circuits, electronics, simulation, spice`
- **[ns-3](../drafts/brew/ns-3.md)**: A discrete-event network simulator used in research and teaching, where you model Wi-Fi, cellular and Internet protocols in software instead of on real hardware.  
  `network, research, science, simulation, wifi`
- **[OctoMap](../drafts/brew/octomap.md)**: A C++ library that turns robot sensor readings into a 3D map of occupied, free and unknown space, stored as an octree.  
  `3d, c++, library, mapping, octree, robotics`
- **[ODE (Open Dynamics Engine)](../drafts/brew/ode.md)**: A C/C++ physics library that simulates rigid bodies, joints and contacts, the kind of engine that moves vehicles and walking creatures in games.  
  `c, library, physics, rigid-body, simulation`
- **[Open Babel](../drafts/brew/open-babel.md)**: A chemical toolbox that converts, searches and analyzes molecular data across dozens of file formats, as command-line programs and a programmer's library.  
  `chemistry, cli, file-formats, library, science`
- **[OpenFst](../drafts/brew/openfst.md)**: A library and about 60 pipeable shell tools for weighted finite-state transducers, the machinery behind speech recognition and machine translation.  
  `automata, cpp, formal-languages, library, nlp, speech`
- **[OpenSlide](../drafts/brew/openslide.md)**: A C library and small toolset for reading gigapixel pathology slide scans from many vendor formats without loading the whole image into memory.  
  `image-formats, library, microscopy, pathology, science`
- **[OpenTURNS](../drafts/brew/openturns.md)**: A C++ and Python library for uncertainty quantification: give it distributions and a model, get back sensitivities, reliability estimates and output distributions.  
  `math, python, science, simulation, statistics, uncertainty`
- **[OpenVDB](../drafts/brew/openvdb.md)**: A C++ library from DreamWorks for storing sparse 3D volumes like smoke, clouds and fire, and the data structure behind much film VFX.  
  `c++, gpu, library, simulation, vfx, volumetrics`
- **[osmcoastline](../drafts/brew/osmcoastline.md)**: Turns the coastline ways in an OpenStreetMap planet file into closed land and water polygons, including a special case for Antarctica.  
  `geospatial, gis, maps, openstreetmap, spatialite`
- **[Packmol](../drafts/brew/packmol.md)**: Packmol packs hundreds or thousands of molecules into boxes, spheres, or membranes without overlaps, building the starting point for molecular dynamics simulations from a short text file.  
  `chemistry, molecular-dynamics, science, simulation`
- **[PAML](../drafts/brew/paml.md)**: Nine command-line programs that fit evolutionary models to DNA and protein alignments by maximum likelihood, then test hypotheses about selection and divergence times.  
  `biology, phylogenetics, science, statistics`
- **[PARI/GP](../drafts/brew/pari.md)**: A number theory calculator with its own small language, built in Bordeaux since the early 1980s, for factoring, elliptic curves and other exact arithmetic.  
  `cas, language, math, number-theory`
- **[PBC](../drafts/brew/pbc.md)**: A C library for pairing-based cryptography, written for a degree and now openly 'frozen in amber', with a door into bilinear maps on elliptic curves.  
  `c, cryptography, elliptic-curves, library, math`
- **[PLINK 1.9](../drafts/brew/plink1.md)**: A single-binary genetics toolkit that filters, converts and tests genotype data for disease associations, the standard workhorse of genome-wide studies, now openly labelled legacy.  
  `genetics, genomics, science, statistics`
- **[preCICE](../drafts/brew/precice.md)**: A coupling library that connects separate physics solvers, such as fluid and structure codes, so they exchange data mid-run without being rewritten.  
  `cfd, library, multi-physics, science, simulation`
- **[primer3](../drafts/brew/primer3.md)**: Primer3 reads a DNA sequence and prints ranked PCR primer pairs, using a plain text-in, text-out format and thermodynamic scoring.  
  `biology, dna, pcr, science`
- **[Prover9 and Mace4](../drafts/brew/prover9.md)**: Prover9 tries to prove theorems in first-order and equational logic from axioms you write, and Mace4 hunts for finite counterexamples when a claim is false.  
  `logic, math, science, theorem-proving`
- **[PyMOL](../drafts/brew/pymol.md)**: A molecular viewer for spinning proteins and other biomolecules in 3D, built on open-source code that commercial licenses pay for.  
  `gui, molecules, python, science, visual`
- **[qd](../drafts/brew/qd.md)**: A C++ and Fortran-90 library that swaps ordinary floating-point numbers for double-double (~31 digits) and quad-double (~62 digits) types, from David H. Bailey's lab.  
  `c++, fortran, library, math, precision`
- **[RAxML-NG](../drafts/brew/raxml-ng.md)**: Infers evolutionary trees from aligned DNA or protein sequences by maximum likelihood, the real method biologists use to work out who descends from whom.  
  `bioinformatics, maximum-likelihood, phylogenetics, science`
- **[RDKit](../drafts/brew/rdkit.md)**: An open-source chemistry toolkit for Python: parse molecules, search substructures, compute fingerprints, and feed chemical structure into machine learning.  
  `chemistry, library, machine-learning, python, science`
- **[Rocq](../drafts/brew/rocq.md)**: Rocq, formerly Coq, is a proof assistant where you write theorems and programs together and a small kernel checks every step.  
  `language, math, ocaml, proofs, type-theory`
- **[ROOT](../drafts/brew/root.md)**: CERN's C++ data analysis framework, built for the Large Hadron Collider, with an interactive C++ interpreter and Python bindings for histograms, fits and plots.  
  `cpp, data-analysis, physics, python, science, visual`
- **[rrdtool](../drafts/brew/rrdtool.md)**: A time-series database whose files are created at full size and wrap around like a ring buffer, so a decade of graphs never outgrows its disk space.  
  `database, graphing, monitoring, old-school, time-series`
- **[S2 Geometry](../drafts/brew/s2geometry.md)**: A C++ library for geometry on a sphere instead of a flat map, built with geographic data in mind.  
  `cpp, geometry, geospatial, library, math`
- **[SAC: Seismic Analysis Code](../drafts/brew/sac.md)**: A decades-old interactive program for filtering and inspecting seismometer recordings, with its own command language, now carried on by the community under Apache 2.0.  
  `needs-data, science, seismology, x11`
- **[SymbiYosys (sby)](../drafts/brew/sby.md)**: A driver for formal hardware verification: describe a circuit's properties in one file and sby either proves them or hands back a waveform showing how they break.  
  `formal-verification, hardware, proofs, verilog, yosys`
- **[seqwish](../drafts/brew/seqwish.md)**: Turns a pile of pairwise sequence alignments into a variation graph, so many genomes collapse into one shared structure.  
  `bioinformatics, genomics, graphs, pangenome, rust`
- **[SExtractor](../drafts/brew/sextractor.md)**: Reads an astronomical image and writes a catalogue of every star and galaxy it finds, with measurements for each: real survey-grade astronomy software.  
  `astronomy, catalogues, images, science`
- **[Shamrock](../drafts/brew/shamrock.md)**: An open-source astrophysical fluid simulation code written in SYCL, so one codebase runs on NVIDIA, AMD, Intel GPUs or plain CPUs.  
  `astrophysics, gpu, hpc, science, simulation, sycl`
- **[SHTOOLS](../drafts/brew/shtools.md)**: A Fortran 95 library, with a Python interface, for spherical harmonics: transform gravity, magnetic and topography maps of whole planets into frequencies and back.  
  `fortran, geophysics, library, math, python, science`
- **[Singular](../drafts/brew/singular.md)**: A computer algebra system for polynomial ideals, algebraic geometry and singularity theory: real research mathematics you can run in a terminal.  
  `algebra, algebraic-geometry, math, science`
- **[Siril](../drafts/brew/siril.md)**: Siril stacks hundreds of noisy telescope frames into one clean image, with calibration, colour correction and deconvolution, using real astronomy methods on your own data.  
  `astronomy, fits, gui, image-processing, science`
- **[skani](../drafts/brew/skani.md)**: Compares two DNA genomes and prints how similar they are and how much of each lines up, fast enough to search tens of thousands of genomes in seconds.  
  `bioinformatics, dna, genomics, rust, science`
- **[Sollya](../drafts/brew/sollya.md)**: A scripting environment for building floating-point math functions with proven error bounds, the kind of work that sits underneath every libm.  
  `floating-point, libm, math, numerical-analysis`
- **[spglib](../drafts/brew/spglib.md)**: A C library that takes a crystal's atom positions and tells you its space group, with a tolerance setting so slightly distorted real structures still count.  
  `crystallography, library, math, science, symmetry`
- **[Spin](../drafts/brew/spin.md)**: Spin checks models of concurrent programs against assertions, so you can test a mutual exclusion algorithm like Peterson's before it ever runs as real code.  
  `concurrency, formal-verification, language, model-checking`
- **[Spot](../drafts/brew/spot.md)**: A toolkit of Unix-style filters for temporal logic formulas and omega-automata: simplify an LTL formula, turn it into an automaton, test translators against each other.  
  `automata, cli, formal-methods, library, logic, math, model-checking`
- **[staq](../drafts/brew/staq.md)**: A command-line toolkit that compiles and transforms quantum circuits by editing the OpenQASM syntax tree directly, so the output still reads like your source.  
  `c++, compilers, openqasm, quantum, science`
- **[STP](../drafts/brew/stp.md)**: A constraint solver that takes logical puzzles about bitvectors and answers satisfiable or not, the same engine that sits under symbolic-execution bug finders like KLEE.  
  `bitvectors, logic, smt, solver, symbolic-execution`
- **[sylph](../drafts/brew/sylph.md)**: Sylph tells you which microbial species are in a metagenomic sample by comparing k-mers against genome databases, in seconds rather than hours.  
  `bioinformatics, genomics, k-mers, metagenomics, science`
- **[TFEL/MFront](../drafts/brew/tfel.md)**: A code generator from CEA and EDF that turns short material-law descriptions into C++ for many finite element solvers, with a local tester.  
  `c++, code-generation, mechanics, science`
- **[UNU.RAN](../drafts/brew/unuran.md)**: A C library that draws random numbers from almost any probability distribution, including truncated and empirical ones, and refuses methods that don't fit.  
  `c-library, math, random-numbers, statistics`
- **[Vampire](../drafts/brew/vampire.md)**: A research-grade automated theorem prover: give it a logical problem in TPTP format and it tries to prove it, refute it, or build a model.  
  `formal-methods, logic, math, smt, theorem-proving`
- **[Verilator](../drafts/brew/verilator.md)**: Verilator compiles Verilog and SystemVerilog hardware designs into C++ models, so you can simulate a circuit you wrote as a fast native program.  
  `c++, hardware-design, hdl, simulation, systemverilog, verilog`
- **[VeryFastTree](../drafts/brew/veryfasttree.md)**: A multithreaded, vectorized fork of FastTree-2 that builds phylogenetic trees from alignments with up to millions of sequences, using the same flags.  
  `bioinformatics, parallel, phylogenetics, science, simd`
- **[Voro++](../drafts/brew/voro++.md)**: A C++ library that computes a 3D Voronoi cell around each particle one at a time, returning volume, centroid, and face count per cell.  
  `c++, geometry, library, math, science`
- **[VROOM](../drafts/brew/vroom.md)**: An open-source engine that takes vehicles, pickups and deliveries with time windows and capacities, and returns optimized routes in milliseconds.  
  `c++, math, operations-research, optimization, routing`
- **[vsearch](../drafts/brew/vsearch.md)**: An open-source command-line tool that clusters, searches and de-chimeras DNA sequence files, a free alternative to USEARCH for microbiome amplicon work.  
  `bioinformatics, microbiome, science, sequences`
- **[wcslib](../drafts/brew/wcslib.md)**: The reference C library for FITS World Coordinate System transforms, which map pixels in astronomical images to positions on the sky, plus a few small utilities.  
  `astronomy, fits, library, math, projections, science`
- **[WCSTools](../drafts/brew/wcstools.md)**: Fifty-odd small command-line programs that turn pixel positions in astronomical images into sky coordinates, and back, by reading the WCS stored in FITS headers.  
  `ancient, astronomy, c, fits, science`
- **[Yices 2](../drafts/brew/yices2.md)**: An SMT solver from SRI that takes logical and arithmetic constraints and returns either a satisfying assignment or a verdict that none exists.  
  `formal-methods, library, logic, math, smt, solver`
- **[Yosys](../drafts/brew/yosys.md)**: Yosys turns Verilog hardware descriptions into gate-level netlists through a chain of scriptable passes, so you can watch a circuit get synthesized step by step.  
  `formal-methods, fpga, hardware, synthesis, verilog`
- **[zfp](../drafts/brew/zfp.md)**: A compressor for grids of floating-point numbers that lets you read and write single elements without unpacking the whole array.  
  `compression, floating-point, hpc, library, science`

## days-off

- **[ACL2](../drafts/brew/acl2.md)**: A Lisp-based programming language and theorem prover where you write models of computer systems, then ask the machine to prove things about them.  
  `formal-verification, lisp, math, theorem-prover`
- **[BEAST](../drafts/brew/beast.md)**: A Bayesian sampler that infers time-measured evolutionary trees from DNA or RNA sequences, used for real research in viral spread and phylogenetics.  
  `bayesian, biology, java, mcmc, phylogenetics, science`
- **[CP2K](../drafts/brew/cp2k.md)**: A Fortran package that simulates atoms and electrons from an input file, covering DFT, tight-binding and classical force fields in one code, free under the GPL.  
  `chemistry, fortran, mpi, physics, science, simulation`
- **[DAMASK grid solver](../drafts/brew/damask-grid.md)**: A spectral FFT solver that simulates how polycrystalline metal deforms, grain by grain, from a voxel microstructure and a load case.  
  `crystal-plasticity, materials, mpi, science, simulation`
- **[GROMACS](../drafts/brew/gromacs.md)**: A molecular dynamics engine that simulates proteins, lipids and other particles moving under Newtonian physics, driven entirely by the command-line gmx tool.  
  `biophysics, molecular-dynamics, science, simulation`
- **[LibBi](../drafts/brew/libbi.md)**: A modelling language and compiler for Bayesian state-space models, built around particle filters that can run on multi-core CPUs, GPUs and clusters.  
  `bayesian, gpu, math, science, simulation, statistics`
- **[Mathematical Components (math-comp)](../drafts/brew/math-comp.md)**: A large library of machine-checked mathematics for the Coq/Rocq proof assistant, behind formal proofs of the Four Colour and Feit-Thompson theorems.  
  `coq, formal-verification, library, math, proof-assistant, rocq`
- **[NWChem](../drafts/brew/nwchem.md)**: An open-source computational chemistry package from a US national lab, built to run quantum and classical molecular simulations from one processor up to thousands.  
  `chemistry, mpi, science, simulation`
- **[OpenFAST](../drafts/brew/openfast.md)**: A research-grade wind turbine simulator that couples aerodynamics, waves, controls and structural flex into one time-domain model of a whole turbine.  
  `engineering, fortran, science, simulation, wind-energy`
- **[ppl](../drafts/brew/ppl.md)**: A C++ library for convex polyhedra and other numerical abstractions, with exact linear programming and a few demo tools you can run from the shell.  
  `c++, library, math, polyhedra, verification`
- **[PYTHIA](../drafts/brew/pythia.md)**: A research-grade Monte Carlo generator that simulates high-energy particle collisions, the same kind of tool collider physicists use, and you can build it at home.  
  `c++, monte-carlo, physics, science, simulation`
- **[SimGrid](../drafts/brew/simgrid.md)**: A research library for simulating distributed systems, so you can predict how clusters, networks and data centers behave without building them.  
  `distributed-systems, library, mpi, science, simulation`
