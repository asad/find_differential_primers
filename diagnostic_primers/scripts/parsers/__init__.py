# -*- coding: utf-8 -*-
"""Module providing parser definitions

(c) The James Hutton Institute 2017-2019

Author: Leighton Pritchard
Contact: leighton.pritchard@hutton.ac.uk

Leighton Pritchard,
Information and Computing Sciences,
James Hutton Institute,
Errol Road,
Invergowrie,
Dundee,
DD6 9LH,
Scotland,
UK

The MIT License

Copyright (c) 2017-2019 The James Hutton Institute
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys

from argparse import ArgumentParser

from diagnostic_primers.scripts.parsers import (
    blastscreen_parser,
    classify_parser,
    common_parser,
    config_parser,
    dedupe_parser,
    eprimer3_parser,
    extract_parser,
    fdp_parsers,
    filter_parser,
    nucmer_parser,
    plot_parser,
    primer3_parser,
    primersearch_parser,
    scheduler_parser,
)


# Process command-line
def parse_cmdline(args=None):
    """Parse command-line arguments for pdp script.

    :param args:  arguments to parse

    The script offers a single main parser, with subcommands for the actions:

    process - process/check input data (stitch fragments/fix sequence problems)
    prodigal - run Prodigal to predict CDS features, and update .conf file
    eprimer3 - run ePrimer3 to predict primer pairs, and update .conf file
    check_blast - check/filter designed primers against negative example
                  BLAST database
    primersearch - check/filter designed primers against complete genome
                   negative examples
    classify - classify designed primers against input genome/classes
    """
    # Main parent parser
    parser_main = ArgumentParser(prog="pdp")
    subparsers = parser_main.add_subparsers(
        title="subcommands", description="valid subcommands", help="additional help"
    )

    # Common parser to be included with all the subcommand parsers
    parser_common = common_parser.build()
    parser_scheduler = scheduler_parser.build()
    parser_nucmer = nucmer_parser.build()

    # Add subcommand parsers to the main parser's subparsers
    config_parser.build(subparsers, parents=[parser_common])
    filter_parser.build(
        subparsers, parents=[parser_common, parser_nucmer, parser_scheduler]
    )
    eprimer3_parser.build(subparsers, parents=[parser_common, parser_scheduler])
    primer3_parser.build(subparsers, parents=[parser_common, parser_scheduler])
    dedupe_parser.build(subparsers, parents=[parser_common])
    blastscreen_parser.build(subparsers, parents=[parser_common, parser_scheduler])
    primersearch_parser.build(subparsers, parents=[parser_common, parser_scheduler])
    classify_parser.build(subparsers, parents=[parser_common])
    extract_parser.build(subparsers, parents=[parser_common, parser_scheduler])
    plot_parser.build(subparsers, parents=[parser_common])

    # Parse arguments
    if args is None:
        args = sys.argv[1:]
    return parser_main.parse_args(args)


def parse_fdp(args=None):
    """Parser for find_differential_primers.py back-compatibility.

    :param args:  arguments to parse
    """
    # find_differential_primers-specific parsers
    parser_fdp_io = fdp_parsers.build_io_parser()
    parser_logs = fdp_parsers.build_log_parser()
    parser_prod = fdp_parsers.build_prodigal_parser()
    parser_ep3 = fdp_parsers.build_eprimer3_parser()
    parser_blast = fdp_parsers.build_blast_parser()
    parser_psearch = fdp_parsers.build_primersearch_parser()
    parser_classify = fdp_parsers.build_classify_parser()
    parser_scheduling = fdp_parsers.build_scheduling_parser()

    # Build parser
    parser_main = ArgumentParser(
        prog="find_differential_primers.py",
        parents=[
            parser_fdp_io,
            parser_logs,
            parser_prod,
            parser_ep3,
            parser_blast,
            parser_psearch,
            parser_classify,
            parser_scheduling,
        ],
    )

    # Parse arguments
    if args is None:
        args = sys.argv[1:]
    return parser_main.parse_args(args)
