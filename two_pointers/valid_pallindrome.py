# Write a function that takes a string s as input and checks whether it’s a palindrome or not.

def is_palindrome(s):

  left = 0
  right = len(s) - 1
  while left <= right:
      if s[left] != s[right]:
          return False
      left = left + 1
      right = right -1 
  return True

tests = ["malayalam", "abccdba", "abccba"]

for test in tests:
    print(f"input : {test}, output: {is_palindrome(test)}")