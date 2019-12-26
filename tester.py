#!/usr/bin/env python3

from sequence import Sequence
import sys

try:
    l = sys.argv[1:]
    print(l)
    size = len(l)
    s = Sequence(size, l)
except:
    l = None
    size = 64
    s = Sequence(size)

print("original list: {}".format(s))
bs = s.collect_and_merge()
print("trends before rotation: {}".format(bs))
n = bs.rotate_and_merge()
print("trends after rotation: {}".format(bs))
# print(n)
# s = Sequence(size, s.rotate(n))
# print(s)
# bs = s.collect_and_merge()
# print(bs)
