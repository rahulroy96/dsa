# Given strings str1 and str2, 
# find the minimum (contiguous) substring sub_str of str1, 
# such that every character of str2 appears in sub_str
# in the same order as it is present in str2.

def min_window(str1, str2):
    i = 0
    j = 0
    min_length = float("infinity")
    min_substring = ""
    while i < len(str1) and j < len(str2):
        while j < len(str2) and i < len(str1):
            if str1[i] == str2[j]:
                j+=1
            i+=1
        if i == len(str1) and j != len(str2):
            break

        start = i
        end = i
        j -= 1
        while j >= 0 and start >= 0:
            start -= 1
            if str1[start] == str2[j]:
                j -= 1
            
        length = end - start
        if length < min_length:
            min_length = length
            min_substring = str1[start:end]
        j = 0
        i = start + 1

    return min_substring


tests = [("abcdabfcdf", "abcdf"), ("abcbde", "abcd"), ("abcbde", "")]

for test in tests:
    print(f"input : {test}, output : {min_window(test[0], test[1])}")
