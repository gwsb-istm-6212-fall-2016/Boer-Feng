#!/usr/bin/env python

"""
A filter that removes fifteen common words of English text.
"""

import fileinput


def process(line):
    """For each line of input, split lines of text into one word per line."""
    return(line.strip())

stop = ["the", "be","to","of","and", "in", "a", "that", "have", "I", "it","for", "not","on","with"]

for line in fileinput.input():
    text = process(line)
    if text not in stop:
        print(text)
