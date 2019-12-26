"""
blockstack
"""


import collections


class BlockStack(collections.deque):
    """
    A stack of blocks.
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "{}.{}".format(self.__class__.__module__, self.__class__.__qualname__)

    def __str__(self):
        s = ""
        if self:
            s += "[\n"
            for block in self:
                s += "    {}\n".format(block.trend())
            s += "]"
        return s

    def latest(self):
        """most recent trend
        :return: top block of stack
        :rtype: Block

        >>> from sequence import Sequence
        >>> from block import Block
        >>> s = Sequence(3, [5, 2, 4])
        >>> b = Block(s, 0, 1)
        >>> bs = BlockStack()
        >>> bs.coalesce(b)
        >>> b = Block(s, 1, 2)
        >>> bs.coalesce(b)
        >>> bs.latest().trend()
        [2.0, 4.0]

        """
        if self:
            return self[-1]
        return None

    def coalesce(self, block):
        """ put block into top of stack
        :param Block block:
        :return: None

        >>> from sequence import Sequence
        >>> from block import Block
        >>> s = Sequence(4, [69, 1, 2, 4])
        >>> b = Block(s, 0, 1)
        >>> bs = BlockStack()
        >>> bs.coalesce(b)
        >>> b = Block(s, 1, 2)
        >>> bs.coalesce(b)
        >>> b = Block(s, 3, 1)
        >>> bs.coalesce(b)
        >>> print(bs)
        [
            [1.0, 2.0, 4.0]
            [69.0]
        ]
        """
        new_mean = block.mu()
        while self.latest() and (self.latest().mu() < new_mean):
            top_of_stack = self.pop()
            block = top_of_stack.merge(block)
            new_mean = block.mu()
        self.append(block)

    def rotate_and_merge(self):
        """rotate until there is only one trend
        :return: start of trend
        :rtype: int

        >>> from sequence import Sequence
        >>> from block import Block
        >>> s = Sequence(4, [69, 1, 2, 4])
        >>> b = Block(s, 0, 1)
        >>> bs = BlockStack()
        >>> bs.coalesce(b)
        >>> b = Block(s, 1, 2)
        >>> bs.coalesce(b)
        >>> b = Block(s, 3, 1)
        >>> bs.coalesce(b)
        >>> n = bs.rotate_and_merge()
        >>> print(n)
        1
        """
        while self[-1].mu() < self[0].mu():
            oldest = self.popleft()
            self.coalesce(oldest)
        return self[0].start
