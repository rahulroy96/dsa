# Given two strings—s and t, find the smallest window substring of t. 
# The smallest window substring is the shortest sequence of characters in s 
# that includes all of the characters present in t. The frequency of each 
# character in this sequence should be greater than or equal to the frequency 
# of each character in t. The order of the characters doesn’t matter here.


def min_window(s, t):
    required_count = {}
    window_count = {}
    
    for ch in t:
        required_count[ch] = 1 + required_count.get(ch, 0)

    required_matched_char = len(required_count)
    current_matched_char = 0
    if required_matched_char == 0:
        return ""

    start, end = 0, 0
    min_window = float("infinity")
    result = ""
    while end < len(s):
        ch = s[end]
        window_count[ch] = 1 + window_count.get(ch, 0)
        if ch in required_count and window_count[ch] == required_count[ch]:
            current_matched_char += 1
        while required_matched_char == current_matched_char:
            if end - start + 1 < min_window:
                min_window = end - start + 1
                result = s[start:end+1]
            window_count[s[start]] -= 1
            if s[start] in required_count and window_count[s[start]] < required_count[s[start]]:
                current_matched_char -= 1
            start += 1
        end += 1
        
    return result


tests = [("abcdabfcdf", "abcdf"), ("abcbde", "abcd"), ("abcbde", ""), ("ABDFGDCKAB" , "ABCD")]

for test in tests:
    print(f"input : {test}, output : {min_window(test[0], test[1])}")