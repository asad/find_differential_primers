#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_parsing.py

Test instantiation, methods and attributions of the GenomeData class

This test suite is intended to be run from the repository root using:

nosetests -v

(c) The James Hutton Institute 2017
Author: Leighton Pritchard

Contact:
leighton.pritchard@hutton.ac.uk

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

Copyright (c) 2017 The James Hutton Institute

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

import os
import unittest

from diagnostic_primers.GenomeCollection import GenomeCollection

from nose.tools import assert_equal


class TestParser(unittest.TestCase):

    """Class defining tests of config file parsing and writing."""

    def setUp(self):
        """Set parameters for tests."""
        self.datadir = os.path.join('tests', 'test_input', 'config')
        self.config = os.path.join(self.datadir, 'testin.conf')
        self.configtest = os.path.join(self.datadir, 'testout.conf')
        self.confignew = os.path.join(self.datadir, 'new.conf')

    def test_parse_config():
        """Test basic config file parsing."""
        gc = GenomeCollection("test", config_file=self.config)
        assert_equal(16, len(gc))
        assert_equal(['Pectobacterium', 'atrosepticum_NCBI',
                      'betavasculorum_NCBI', 'gv1', 'gv2', 'gv3', 'gv7',
                      'wasabiae_NCBI'],
                     gc.groups())

    def test_parse_and_write():
        """Test basic parsing/generation of config file."""
        gc = GenomeCollection("test", config_file=self.config)
        gc.write(self.confignew)
        with open(self.confignew, 'r') as ofh:
            with open(self.configtest, 'r') as ifh:
                assert_equal(ifh.read(), ofh.read())
