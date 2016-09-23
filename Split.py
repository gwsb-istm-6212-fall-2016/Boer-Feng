#!/usr/bin/env python

"""
A filter that split lines of text into one word per line.
"""

import fileinput
import re

def process(line):
    """For each line of input, split lines of text into one word per line."""
    line = re.findall(r'\w+',line)
    
    for word in line:
          print(word.strip())
        



for line in fileinput.input():
    process(line)
