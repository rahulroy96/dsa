# Given a string, input_string find the longest substring without repeating
# characters, and return the length of that longest substring.

def find_longest_substring(input_string):
    start = 0
    window = {}
    max_length = float('-inf')
    for end in range(len(input_string)):
        ch = input_string[end]
        if ch in window and start <= window[ch]:
            start = window[ch] + 1
        
        window[ch] = end
        max_length = max(max_length, end - start + 1)

    return max_length if max_length != float("-inf") else 0


tests = ["malayalam", "abccdba", "abcdbea", "aaaabaaa"]

for test in tests:
    print(f"input : {test}, output: {find_longest_substring(test)}")