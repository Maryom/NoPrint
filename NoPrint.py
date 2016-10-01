#!/usr/bin/env python

import re
import fileinput

choice = raw_input("Please enter 1 to delete print or 2 to comment print: ")

if choice == '1':
    for line in fileinput.input(inplace = True):
        if not re.search(r'\bprint\b',line):
           print line,

elif choice == '2':
    for line in fileinput.input(inplace = True):
        line = re.sub(r"print", "#print", line)
        print line,
