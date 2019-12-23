"""
sequence
"""

import numpy as np

from block import Block
from blockstack import BlockStack


class Sequence(list):
    """
    A list of reals, uniformly distributed [0,1)
    :param int length: length of list
    :param list[float] elems: optional initializer elements

    >>> s = Sequence(69)
    >>> type(s)
    <class 'sequence.Sequence'>
    >>> len(s)
    69
    >>> s = Sequence(3, [1,2,3])
    >>> len(s)
    3
    >>> isinstance(s[-1], float)
    True
    >>> print(s)
    [1.0, 2.0, 3.0]
    >>> bs = s.collect_and_merge()
    >>> len(bs)
    1
    >>> len(Sequence(3, [3,2,1]).collect_and_merge())
    3
    """

    def __init__(self, length, elems=None):
        if elems:
            assert len(elems) == length
            rlist = [float(elem) for elem in elems]
        else:
            rlist = np.random.rand(length)
        super().__init__(rlist)

    def collect_and_merge(self):
        """
        Decompose sequence into trends.
        :return: a list of blocks representing maximal trends
        :rtype: BlockStack
        """
        blockstack = BlockStack()
        for index in range(len(self)):
            new_block = Block(self, index, 1)
            blockstack.coalesce(new_block)
        return blockstack
