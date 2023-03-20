# Given an infinite stream of integers, nums, design a class to find the kth largest element in a stream.

import heapq 

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while self.k < len(self.heap):
            heapq.heappop(self.heap)

    # adds element in the heap
    def add(self, val):
        heapq.heappush(self.heap, val)
        while self.k < len(self.heap):
            heapq.heappop(self.heap)
        return self.return_Kth_largest()

        
    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.heap[0]