#!/usr/bin/env python
# Reads fdupes(-r -1) output and create relative symbolic links for each duplicate
# usage: fdupes -r1 . | ./lndupes.py

import os
from os.path import dirname, relpath, basename, join
import sys

lines = sys.stdin.readlines()

for line in lines:
    files = line.strip().split(' ')
    first = files[0]
    print "First: %s "% first
    for dup in files[1:]:
        rel = os.path.relpath(dirname(first), dirname(dup))
        print "Linking duplicate: %s to %s" % (dup, join(rel,basename(first)))
        os.unlink(dup)
        os.symlink(join(rel,basename(first)), dup)
