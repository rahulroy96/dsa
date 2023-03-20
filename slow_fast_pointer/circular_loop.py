
# An input array containing non-zero integers is given, where the value at 
# each index represents the number of places to skip forward (if the value 
# is positive) or backward (if the value is negative). When skipping forward 
# or backward, wrap around if you reach either end of the array. For this 
# reason, we are calling it a circular array. Determine if this circular array
# has a cycle. A cycle is a sequence of indices in the circular array 
# characterized by the following:
# 
# The same set of indices is repeated when the sequence is traversed in accordance with the aforementioned rules.
# The length of the sequence is at least two.
# The loop must be in a single direction, forward or backward.


def circular_next(i, arr):
    return (i + arr[i])%len(arr)

def circular_array_loop(arr):  
    i = 0
    for i in range(len(arr)):
        slow = i           
        fast = i
        while(True):
            if arr[i] * arr[fast] < 0 or arr[fast]* arr[slow] < 0 or arr[slow] * arr[i]<0:
                break
            elif slow == fast:
                return True
            slow = circular_next(slow, arr)
            fast = circular_next(fast, arr)
            fast = circular_next(fast, arr)            

    return False

tests = [[3,2,1,1,-4,1]]

for test in tests:
    print(f"input : {test}, output: {circular_array_loop(test)}")