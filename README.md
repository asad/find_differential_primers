# README.md (diagnostic_primers)

## NOTE FOR USERS

The default branch for this repository is a development branch: `diagnostic_primers`. If you are looking for code to reproduce work in Pritchard *et al.* (2012) or Pritchard *et al.* (2013), please checkout the `master` branch, or download [release v0.1.3](https://github.com/widdowquinn/find_differential_primers/tree/v0.1.3).

* `diagnostic_primers`: 

[![codecov](https://codecov.io/gh/widdowquinn/find_differential_primers/branch/diagnostic_primers/graph/badge.svg)](https://codecov.io/gh/widdowquinn/find_differential_primers)
[![Build Status](https://travis-ci.org/widdowquinn/find_differential_primers.svg?branch=diagnostic_primers)](https://travis-ci.org/widdowquinn/find_differential_primers)

* `master`: 

[![codecov](https://codecov.io/gh/widdowquinn/find_differential_primers/branch/master/graph/badge.svg)](https://codecov.io/gh/widdowquinn/find_differential_primers)
[![Build Status](https://travis-ci.org/widdowquinn/find_differential_primers.svg?branch=master)](https://travis-ci.org/widdowquinn/find_differential_primers)

## NOTE FOR DEVELOPERS

The default master branch for development is `diagnostic_primers`. We would appreciate contributions, especially if you follow the guidelines on the [wiki](https://github.com/widdowquinn/find_differential_primers/wiki).

* Current test coverage (`diagnostic_primers`): [https://codecov.io/gh/widdowquinn/find_differential_primers/list/diagnostic_primers](https://codecov.io/gh/widdowquinn/find_differential_primers/list/diagnostic_primers)

## Overview
This repository contains code for automated finding of discriminatory (real-time) PCR or qPCR primers that distinguish among genomes or other biological sequences of interest. 

## Usage

This new version of `diagnostic_primers` (formerly `find_differential_primers`) now uses a subcommand model, like the tools `git` and `subversion`. These execute the following subtasks, some or all of which may be required in a primer design run.

* `process`: Validate the configuration file and stitch input contig fragments/replace ambiguity symbols as necessary.
* `prodigal`: Predict CDS locations on the input sequence
* `eprimer3`: Design amplifying primers on the input sequence
* `blastcheck`: Filter designed primers against a database of negative examples
* `primersearch`: Filter designed primers on their ability to amplify each input sequence
* `classify`: Classify designed primers by specificity for each class of input sequence

Each of these subcommands has specific help, accessible with `pdp.py <subcommand> -h` or `pdp.py <subcommand> --help`.

## FURTHER INFORMATION:
Please read the comments contained within the top of each '*.py' file as well as the Supporting Information (['Methods S1' document](doi:10.1371/journal.pone.0034498.s006)) of [doi:10.1371/journal.pone.0034498](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0034498).

## CONTRIBUTORS
* [Leighton Pritchard](https://github.com/widdowquinn)
* [Benjamin Leopold](https://github.com/cometsong)
* [Michael Robeson](https://github.com/mikerobeson)
* [Rory McLeod](https://github.com/rory-mcleod)

## CITATIONS
Please refer to the following for methodological details:

* Pritchard L _et al._ (2012) "Alignment-Free 
Design of Highly Discriminatory Diagnostic Primer Sets for _Escherichia coli_ O104:H4 Outbreak Strains." _PLoS ONE_ **7**(4): e34498. [doi:10.1371/journal.pone.0034498](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0034498) - _Method description and application to human bacterial pathogens, sub-serotype resolution_
* Pritchard L _et al._ (2013) "Detection of phytopathogens of the genus _Dickeya_ using a PCR primer 
prediction pipeline for draft bacterial genome sequences." _Plant Pathology_, **62**, 587-596
[doi:10.1111/j.1365-3059.2012.02678.x](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-3059.2012.02678.x/full) - _Application to plant pathogens, species-level resolution_
