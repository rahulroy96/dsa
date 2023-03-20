# Given an array of positive integers nums and a positive integer target, 
# find the window size of the shortest contiguous subarray whose sum is 
# greater than or equal to the target value. If no subarray is found,
# 0 is returned.

def min_sub_array_len(nums, target):
    start, end, current_sum = 0, 0, 0
    minimum_length = float("infinity")

    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum - nums[start] >= target:
            current_sum -= nums[start]
            start += 1
        if current_sum >= target and end - start + 1 < minimum_length:
            minimum_length = end - start + 1


    return minimum_length if minimum_length != float("infinity") else 0

tests = [([1,-1,0], 1), ([3,7,1,2,8,4,5], 10), ([3,7,1,2,8,4,5], 20), ([3,7,1,2,8,4,5], 21), ([1, 2, 1, 3], 5), 
([1, 1, 1, 1, 1, 1, 1, 1], 11)]

for test in tests:
    print(f"input : {test}, output: {min_sub_array_len(test[0], test[1])}")