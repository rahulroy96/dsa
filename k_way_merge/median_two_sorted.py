# You’re given two sorted integer arrays, nums1 and nums2, of size m and n, 
# respectively. Your task is to return the median of the two sorted arrays. 
# The overall run time complexity should be O(log(m+n)).

def find_median(nums1, nums2):
    right_long = len(nums1) // 2
    left_long = right_long - 1

    right_short = (len(nums2) + 1) // 2
    left_short = right_short - 1

    print(left_short, right_short, left_long, right_long)
    while right_short < len(nums2) and right_long < len(nums1) and not (nums1[right_long] >= nums2[left_short] and nums1[left_long] <= nums2[right_short]):
        if nums1[left_long] > nums2[right_short] and right_short < len(nums2):
            temp = left_short
            left_short = (left_short + len(nums2)) // 2
            left_long = left_long - (left_short - temp)
        elif nums1[left_long] > nums2[right_short] and right_short >= len(nums2) - 1:
            if len(nums1) == len(nums2):
                return (nums2[-1] + nums1[0]) / 2.0
            elif (len(nums1) + len(nums2)) & 1 == 1:
                return nums1[left_long + 1] / 1.0
            else:
                return (nums1[right_long + 1] + nums1[right_long]) / 2.0
        elif nums1[right_long] < nums2[left_short] and left_short != 0:
            temp = left_short
            left_short = left_short // 2
            left_long = left_long + temp - left_short
        elif nums1[right_long] < nums2[left_short] and left_short == 0:
            if len(nums1) == len(nums2):
                return (nums1[-1] + nums2[0]) / 2.0
            elif (len(nums1) + len(nums2)) & 1 == 1:
                return nums1[right_long + 1] / 1.0
            else:
                return (nums1[right_long + 1] + nums1[right_long]) / 2.0
        
        right_short = left_short + 1
        right_long = left_long + 1
        print(left_short, right_short, left_long, right_long)
        
    if (len(nums1) + len(nums2)) & 1 == 0:
        return (max(nums1[left_long], nums2[left_short]) + min(nums1[right_long], nums2[right_short])) / 2.0
    else:
        return (max(nums1[right_long], nums2[right_short]) ) / 1.0

tests = [[[1, 2] , [3, 4]], [[1, 5, 8] , [4, 7, 9]], [[5, 7, 8, 13, 17, 22, 29] , [30, 32, 39, 41]]]

for test in tests:
    print(f"input : {test}, output: {find_median(test[0], test[1])}")