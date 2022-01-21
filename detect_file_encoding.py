#!/usr/bin/python3

"""
Script which takes one or more file paths and reports on their detected
encodings

Example::

    % chardetect somefile someotherfile
    somefile: windows-1252 with confidence 0.5
    someotherfile: ascii with confidence 1.0

If no paths are provided, it takes its input from stdin.
"""

# -*- coding: utf-8 -*-
import re
import sys
from chardet.cli.chardetect import main as chrdet

def main():
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    return chrdet()

if __name__ == '__main__':
    print("Please input path to file")
    for x in range(3):
        main()
    print("Closing")
    sys.exit()

