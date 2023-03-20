# Write a function that takes a string as input and checks whether 
# it can be a valid palindrome by removing at most one character from it.

def check_pal(s, left, right):
  while(left < right):
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

def is_palindrome(s):
  left = 0
  right = len(s) - 1
  count = 0
  flag = True
  while(left < right and count==0):
    if s[left] != s[right]:
      flag = check_pal(s, left+1, right)
      if not flag:
        flag = check_pal(s, left, right-1)
      count = 1
    else:
      left += 1
      right -= 1
  return flag


tests = ["malayalam", "madame", "dead", "tebbem", "eeccccbebaeeabebccceea"]

for test in tests:
    print(f"input : {test}, output: {is_palindrome(test)}")