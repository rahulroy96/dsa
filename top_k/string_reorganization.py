# Given a string, rearrange it so that any two adjacent characters are not the 
# same. If such a reorganization of the characters is possible, output any 
# possible valid arrangement. Otherwise, return an empty string.

from collections import Counter
import heapq

def reorganize_string(input_string):
    freq = Counter(input_string)
    print(freq)
    max_heap = []

    for k, v in freq.items():
        heapq.heappush(max_heap, [-v, k])

    result = ""
    prev = None

    while max_heap or prev:
        if prev and len(max_heap) == 0:
            return ""
        
        count, char = heapq.heappop(max_heap)
        count += 1
        result = result + char

        if prev:
            heapq.heappush(max_heap, prev)
        
        if count != 0:
            prev = [count, char]
        else:
            prev = None

    return result

tests = ["abb", "abccdba", "abccba"]

for test in tests:
    print(f"input : {test}, output: {reorganize_string(test)}")
    
