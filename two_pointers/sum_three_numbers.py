# Given an array of integers, nums, and an integer value, target,
#  determine if there are any three integers in nums whose sum 
# equals the target. Return TRUE if three such integers are found 
# in the array. Otherwise, return FALSE.

def find_sum_of_three(nums, target):
   nums.sort()
   length = len(nums)
   for i in range(length):
      j = i+1
      k = length - 1
      while (j < k):
         three_sum = nums[i] + nums[j] + nums[k]
         if three_sum == target:
            return True
         elif three_sum > target:
            k-=1
         else:
            j+=1
   return False


tests = [([1,-1,0], -1), ([3,7,1,2,8,4,5], 10), ([3,7,1,2,8,4,5], 20), ([[3,7,1,2,8,4,5]], 21)]

for test in tests:
    print(f"input : {test}, output: {find_sum_of_three(test[0], test[1])}")