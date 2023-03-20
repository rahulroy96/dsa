# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# 
# Starting with any positive integer, replace the number by the sum of the 
# squares of its digits. Repeat the process until the number equals 1 
# (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return TRUE if n is a happy number, and FALSE if not.


def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit ** 2
        number = number // 10
    return total_sum

def is_happy_number(n):
    slow = n
    fast = sum_of_digits(n)
    
    while slow != fast and fast != 1:
        slow = sum_of_digits(slow)
        fast = sum_of_digits(sum_of_digits(fast))
    
    if fast == 1:
        return True
    return False

tests = [2147483646, 1, 19, 8]

for test in tests:
    print(f"input : {test}, output: {is_happy_number(test)}")