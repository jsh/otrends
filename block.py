"""
block

"""


class Block:
    """
    An annotated subsequnce of reals.
    :param list[float] s: The underlying sequence
    :param int location: The start of the subsequence
    :param int length: The length of the subsequence
    >>> from sequence import Sequence
    >>> s = Sequence(69)
    >>> b = Block(s, 0, 1)
    >>> c = Block(s,1, 1)
    >>> type(b)
    <class 'block.Block'>
    >>> len(b.seq)
    69
    >>> b.length == 1
    True
    >>> b.location == 0
    True
    >>> b.mu() == b.sum()
    True
    >>> print(b)  #doctest: +ELLIPSIS
    trend: [...]
        start: ..., length: ..., mean: ...
        (seq: [...])
    >>> merger = b.merge(c)
    >>> merger.length == 2
    True
    >>> merger.location == 0
    True
    >>> merger.sum() == b.sum() + c.sum()
    True
    """

    def __init__(self, seq, location, length):
        self._seq = seq
        self._location = location
        self._length = length
        self._sum = sum(seq[location : location + length])

    def __repr__(self):
        return "{}.{}({},{},{})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self._seq,
            self._location,
            self._length,
        )

    def __str__(self):
        return "trend: {}\n    start: {}, length: {}, mean: {}\n    (seq: {})".format(
            self.trend(), self._location, self._length, self.mu(), self.seq
        )

    @property
    def seq(self):
        """the underlying sequence, of which the subsequence is a part."""
        return self._seq

    @property
    def location(self):
        "the subsequence start."
        return self._location

    @property
    def length(self):
        "the subsequence length."
        return self._length

    def sum(self):
        """report block sum
        """
        return self._sum

    def mu(self):
        """report block mean."""
        return self._sum / self._length

    def trend(self):
        """return block subsequence."""
        return self._seq[self._location : self._location + self._length]

    def merge(self, neighbor):
        """ merge a block with its neigbor to the right."""
        assert self.location + self.length == neighbor.location
        assert self.seq == neighbor.seq
        merger = Block(self.seq, self.location, self.length + neighbor.length)
        return merger
