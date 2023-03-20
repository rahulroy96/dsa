# Given a sorted integer array, nums, and an integer value, target, the array 
# is rotated by some arbitrary number. Search and return the index of target 
# in this array. If the target does not exist, return -1.

def binary_search_rotated(nums, target):
    low = 0
    high = len(nums) - 1

    while (low <= high):
        mid = (low + high) // 2
        print(low, mid, high )

        if nums[mid] == target:
            return mid   
        elif target > nums[mid] and target <= nums[high]:
            low = mid + 1
        elif target < nums[mid] and target >= nums[low]:
            high = mid - 1
        elif target > nums[mid] and target > nums[high]:
            high = mid - 1
        elif target < nums[mid] and target < nums[low]:
            low = mid + 1
    return -1

tests = [([6,7,1,2,3,4,5], 3), ([6,7,1,2,3,4,5], 6), ([4,5,6,1,2,3], 3), ([4,5,6,1,2,3], 6)]

for test in tests:
    print(f"input : {test}, output: {binary_search_rotated(test[0], test[1])}")