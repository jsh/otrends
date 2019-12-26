"""
sequence
"""

import numpy as np

from block import Block
from blockstack import BlockStack


class Sequence(list):
    """
    A list of reals
    :param int or list args: optional initializer elements

    >>> s = Sequence(69)
    >>> type(s)
    <class 'sequence.Sequence'>
    >>> len(s)
    69
    >>> s = Sequence([1,2,3])
    >>> len(s)
    3
    >>> isinstance(s[-1], float)
    True
    >>> print(s)
    [1.0, 2.0, 3.0]
    """

    def __init__(self, arg):
        if isinstance(arg, int):  # size of random list
            elems = np.random.rand(arg)
        elif isinstance(arg, list):  # elements of list
            elems = arg
            elems = [float(elem) for elem in elems]
        else:
            raise TypeError
        super().__init__(elems)

    def collect_and_merge(self):
        """
        Decompose sequence into trends.
        :return: a list of blocks representing maximal trends
        :rtype: BlockStack

        >>> s = Sequence([1,2,3])
        >>> bs = s.collect_and_merge()
        >>> len(bs)
        1
        >>> len(Sequence([3,2,1]).collect_and_merge())
        3
        """
        blockstack = BlockStack()
        for index in range(len(self)):
            new_block = Block(self, index, 1)
            blockstack.coalesce(new_block)
        return blockstack

    def rotate(self, index):
        """
        Move sequence index..end to beginning
        :param int index:
        >>> s = Sequence([1,2,3])
        >>> s.rotate(2)
        [3.0, 1.0, 2.0]
        """
        return Sequence(self[index:] + self[:index])
