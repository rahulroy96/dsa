# Given two sorted integer arrays, nums1 and  nums2, and the number of data elements in each array, 
# m and n, implement a function that merges the second array into the first one. You have to modify 
# nums1 in place.

def merge_sorted(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = len(nums1) - 1

    # max_heap = []

    while j >= 0 and k >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


    return nums1