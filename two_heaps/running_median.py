# Implement a data structure that’ll store a dynamically growing list of 
# integers and provide access to their median in O(1).

from heapq import *

class MedianOfStream:

  def __init__(self):
    self.max_heap = []
    self.min_heap = []
  
  # This function should take a number and store it
  def insert_num(self, num):

    if self.max_heap and num >= -self.max_heap[0]:
      heappush(self.min_heap, num)
    else:
      heappush(self.max_heap, -num)
    
    if len(self.max_heap) > len(self.min_heap) + 1:
      top = heappop(self.max_heap)
      heappush(self.min_heap, -top)
    elif len(self.min_heap) > len(self.max_heap) + 1:
      top = heappop(self.min_heap)
      heappush(self.max_heap, -top)
    
  # This function should return the median of the stored numbers
  def find_median(self):
    if len(self.max_heap) > len(self.min_heap):
      return -self.max_heap[0]
    elif len(self.max_heap) < len(self.min_heap):
      return self.min_heap[0]
    else:
      return (-self.max_heap[0] + self.min_heap[0])/2
    
median = MedianOfStream()
median.insert_num(1)
median.insert_num(2)
median.insert_num(2)
median.insert_num(3)
median.insert_num(4)
median.insert_num(5)
print(median.find_median())