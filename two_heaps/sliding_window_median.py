# Given an integer array nums and an integer k, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can only see the 
# k numbers in the window. Each time the sliding window moves right by one position, 
# return the median of the current window.

from heapq import *

def median_sliding_window(nums, k):
    max_heap = []
    min_heap = []
    median = []

    for i in range(k):
        heappush(max_heap, -nums[i])
    
    for i in range(k//2):
        top = -heappop(max_heap)
        heappush(min_heap, top)

    end = k
    outgone_dict = {}
    

    while True:
        if k&1 == 0:
            median.append(-max_heap[0]/2.0 + min_heap[0]/2.0)
        else:
            median.append(-max_heap[0]/1.0)

        if end >= len(nums):
            break

        outgoing_num = nums[end - k]
        incoming_num = nums[end]
        end += 1
        outgone_dict[outgoing_num] = 1 + outgone_dict.get(outgoing_num, 0)
        balance = 0
        if max_heap and outgoing_num <= -max_heap[0]:
            balance -= 1
        else:
            balance += 1

        if max_heap and incoming_num <= -max_heap[0]:
            heappush(max_heap, -incoming_num)
            balance += 1
        else:
            heappush(min_heap, incoming_num)
            balance -= 1

        if balance >  0:
            top = -heappop(max_heap)
            heappush(min_heap, top)
            balance -= 1
        elif balance < 0:
            top = heappop(min_heap)
            heappush(max_heap, -top)
            balance += 1
        
        while max_heap and -max_heap[0] in outgone_dict and outgone_dict[-max_heap[0]] > 0:
            outgone_dict[-max_heap[0]] -= 1
            heappop(max_heap)
    
        while min_heap and min_heap[0] in outgone_dict and outgone_dict[min_heap[0]] > 0:
            outgone_dict[min_heap[0]] -= 1
            heappop(min_heap)

    return median

