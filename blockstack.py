"""
blockstack
"""

import collections


class BlockStack(collections.deque):
    """
    A stack of blocks.
    >>> from sequence import Sequence
    >>> from block import Block
    >>> s = Sequence(3, [1, 2, 3])
    >>> b = Block(s, 0, 1)
    >>> bs = BlockStack()
    >>> type(bs)
    <class 'blockstack.BlockStack'>
    >>> bs.coalesce(b)
    >>> print(bs)
    latest trend: [1.0]
        length: 1
    >>> b = Block(s, 1, 2)
    >>> bs.coalesce(b)
    >>> print(bs)
    latest trend: [1.0, 2.0, 3.0]
        length: 1
    >>> s = Sequence(3, [5, 2, 3])
    >>> b = Block(s, 0, 1)
    >>> bs = BlockStack()
    >>> bs.coalesce(b)
    >>> print(bs)
    latest trend: [5.0]
        length: 1
    >>> b = Block(s, 1, 2)
    >>> bs.coalesce(b)
    >>> print(bs)
    latest trend: [2.0, 3.0]
        length: 2
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "{}.{}".format(self.__class__.__module__, self.__class__.__qualname__)

    def __str__(self):
        if not self:
            return ""
        return "latest trend: {}\n    length: {}".format(
            self.latest().trend(), len(self)
        )

    def push(self, block):
        """push block on top of stack
        :param Block block: block to push
        """
        self.append(block)

    def latest(self):
        """most recent trend
        :return: top block of stack
        :rtype: Block
        """
        if self:
            return self[-1]
        return None

    def coalesce(self, block):
        """
        :param Block block:
        :return: None
        """
        new_mean = block.mu()
        while self.latest() and (self.latest().mu() < new_mean):
            top_of_stack = self.pop()
            block = top_of_stack.merge(block)
            new_mean = block.mu()
        self.append(block)
