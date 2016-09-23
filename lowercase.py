#!/usr/bin/env python

"""
A filter that transform text into lower case.
"""

import fileinput


def process(line):
    """For each line of input,strip characters."""
    print(line.strip())


for line in fileinput.input():
    """For each line of input, transform text into lower case."""
    process(line.lower())
