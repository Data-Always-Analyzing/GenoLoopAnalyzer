# cython: language_level=3

cdef class Loop:
    cdef public int start1, end1, start2, end2

    def __init__(self, int start1, int end1, int start2, int end2):
        self.start1 = start1
        self.end1 = end1
        self.start2 = start2
        self.end2 = end2

    cpdef bint is_overlapping(self, Loop other, int bin_size):
        # 重叠的条件是任一端的起始或结束位置之间的距离小于或等于bin_size
        return (abs(self.start1 - other.start1) <= bin_size and abs(self.end1 - other.end1) <= bin_size) or \
               (abs(self.start2 - other.start2) <= bin_size and abs(self.end2 - other.end2) <= bin_size)
