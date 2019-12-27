#!/usr/bin/env python3
"""
Demo the modules.
"""

import sys

from sequence import Sequence

"""
elems = sys.argv[1:]
if elems:
    s = Sequence(elems)
else:
    size = 365 * 100  # a lifetime of days
    s = Sequence(size)
"""


def buck_the_trend(s):
    bs = s.collect_and_merge()
    forward_trends = len(bs)         # number of trends in random sequence
    bs.rotate_and_merge()             # rotate to single trend

    # how many in the opposite direction?
    s = Sequence(bs[0].trend())       # make it a sequence
    s.reverse()                       # turn it around
    backward_trends = len(s.collect_and_merge()) # trends in opposite direction
    return(forward_trends, backward_trends)

years = 70      # the Biblical "three score and ten"
f = 0
b = 0   # in pessimal forward lives
days = 365*years
trials = 100
for i in range(trials):   # multiple trials
    s = Sequence(days)
    (forward_trends, backward_trends) = buck_the_trend(s)
    f += forward_trends
    b += backward_trends

mean_forward_trends = f/trials
mean_backward_trends = b/trials

print("Average number of upward trends in a random life: ", mean_forward_trends)
print("Average number of upward trends in a pessimal life: ", mean_backward_trends)
print("Average upward trend length in a random life: {} years".format(years/mean_forward_trends))
print("Average upward trend length in a pessimal life: {} years".format(years/mean_backward_trends))
