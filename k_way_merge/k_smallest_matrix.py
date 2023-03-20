# Find the kth smallest element in an (n×n) matrix, where each row and column
# of the matrix is sorted in ascending order. Although there can be repeating 
# values in the matrix, each element is considered unique and, therefore, 
# contributes to calculating the kth smallest element.

from heapq import *

def kth_smallest_element(matrix, k):

    heap = []

    for row in matrix:
        heappush(heap, [row[0], row])

    while k > 0:
        value, row = heappop(heap)
        k -= 1
        if len(row) > 1:
            heappush(heap, [row[1], row[1:]])
    
    return value


tests = [[[[2,6,8],[3,7,10],[5,8,11]], 3], [[[1,2,3],[4,5,6],[7,8,9]], 4]]

for test in tests:
    print(f"input : {test}, output: {kth_smallest_element(test[0], test[1])}")