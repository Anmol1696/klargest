"""
Models for working with heapq for adding data and keeping track of k largest values
"""
import heapq


class KLargest:
    """
    Implements a class to hold min heap of constant length
    for k largest values and additional information as keys

    Values, stored in `self.values` are the k largest values,
    which are stored and indexed as min heap
    Keys, stored in `self.keys` are any arbitary objects associated
    with the indexed values.
    """
    value_index = 0
    key_index = 1

    def __init__(self, k=0):
        self.heap = []  # Min heap of k largest values
        if not isinstance(k, int) or k < 0:
            raise Exception("k must be a positive int")
        self.k = k

    @property
    def root(self):
        """
        Return root of min heap
        """
        return self.heap[0][0] if len(self.heap) > 0 else None

    @property
    def values(self):
        """
        Return k largest values, not in any order
        """
        return (x[self.value_index] for x in self.heap)

    @property
    def keys(self):
        """
        Return keys related to k largest values, if specified with values
        NOTE: For now, only returns single key at index 1
        """
        return (x[self.key_index] for x in self.heap if len(x) > 1)

    def add(self, num, *args):
        """
        If given value is greater than root value,
        replace root node and heapify to maintaing min heap of k length
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, (num, *args))
        elif num > self.root:
            heapq.heapreplace(self.heap, (num, *args))

    @classmethod
    def from_input_iter(cls, k, input_iter, extractor=lambda x: x, **kwargs):
        """
        From an interger k, and input iterable form cls object and perform interation
        iterate over input iterator, to store k largest values in min heap
        extractor is the function to extract data from input
        Return class object with k largest values
        """
        # if k is zero, return zero value object
        if k <= 0:
            return cls(0)
        k_largest = cls(k)
        for line in input_iter:
            k_largest.add(*extractor(line))
        return k_largest


def process_stream_to_get_keys(k, input_iter, **kwargs):
    """
    Given input iterable, store k largest value in KLargest
    Return KLargest object keys
    """
    k_largest = KLargest.from_input_iter(k, input_iter, **kwargs)
    return k_largest.keys
