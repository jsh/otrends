#!/usr/bin/env python3

from sequence import Sequence
import sys


elems = sys.argv[1:]
if elems:
    s = Sequence(len(elems), elems)
else:
    size = 64
    s = Sequence(size)

print("original list: {}".format(s))
bs = s.collect_and_merge()
print("trends before rotation: {}".format(bs))
n = bs.rotate_and_merge()
print("trend after rotation by {}: {}".format(n, bs))
