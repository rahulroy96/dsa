# Given a sorted integer array nums and two integers—k and num—return the k 
# closest integers to num in this array. Ensure that the result is sorted 
# in ascending order. The integer a is closer to num than an integer b 
# if the following are true:
# |a - num| < |b - num|, or
# |a - num| = |b - num| and a < b


def find_closest_elements(nums, k, num):

    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == num:
            left = mid
            break
        elif nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    print(left)
    left = left - 1
    right = left + 1
    while right - left - 1  < k:
        if left == -1:
            right += 1
        elif right == len(nums) or abs(nums[right] - num) >= abs(nums[left] - num):
            left -= 1
        else:
            right += 1

    return nums[left+1:right]


tests = [([1,2,3,4,5], 4, 3), ([1,2,3,4,5], 4, -1), ([1,2,3,4,5,6,7], 5, 7), ([-29,-11,-3,0,5,10,50,63,198], 6, 8)]

for test in tests:
    print(f"input : {test}, output: {find_closest_elements(test[0], test[1], test[2])}")