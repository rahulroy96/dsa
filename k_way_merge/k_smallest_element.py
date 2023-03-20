# Given m number of sorted lists in ascending order and an integer k,
# find the kth smallest number among all the given lists.

from heapq import *

def k_smallest_number(lists, k):
    value = 0
    min_heap = []
    for element_list in lists:
        if not element_list:
            continue
        heappush(min_heap, [element_list[0], element_list])
    
    for i in range(k):
        if not min_heap:
            break
        value, element_list = heappop(min_heap)
        if len(element_list) > 1:
            element_list.pop(0)
            heappush(min_heap, [element_list[0], element_list])

    return value


tests = [[[[2,6,8],[3,7,10],[5,8,11]], 5], [[[1,2,3],[4,5],[6,7,8,15],[10,11,12,13],[5,10]], 50]]

for test in tests:
    print(f"input : {test}, output: {k_smallest_number(test[0], test[1])}")