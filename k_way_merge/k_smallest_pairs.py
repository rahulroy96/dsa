# Given two lists, and an integer k, find k pairs of numbers with the smallest 
# sum so that in each pair, each list contributes one number to the pair.

from heapq import *

def k_smallest_pairs(list1, list2, k):
    result = []
    min_sum_heap = []

    i = 0
    for i in range(min(k, len(list1))):
        heappush(min_sum_heap, [list1[i] + list2[0], i, 0])

    while k > 0 and min_sum_heap:
        _, i, j = heappop(min_sum_heap)
        result.append([list1[i], list2[j]])
        k -= 1
        next_j = j + 1
        if next_j < len(list2):
            heappush(min_sum_heap, [list1[i] + list2[next_j], i, next_j])
    
    return result


tests = [[[1,2,300], [1,11,20,35,300], 30], [[1,1,2], [1,2,3], 1]]

for test in tests:
    print(f"input : {test}, output: {k_smallest_pairs(test[0], test[1], test[2])}")