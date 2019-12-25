#!/usr/bin/env python3

from sequence import Sequence

s = Sequence(64)
print(s)
bs = s.collect_and_merge()
print(bs)
n = bs.rotate_and_merge()
print(bs)
print(n)
s = Sequence(64, s.rotate(n))
print(s)
bs = s.collect_and_merge()
print(bs)
