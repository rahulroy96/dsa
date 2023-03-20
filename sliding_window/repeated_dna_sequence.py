# Given a string s that represents a DNA sequence, and a number k, 
# return all the contiguous sequences (substrings) of length k that 
# occur more than once in the string. The order of the returned 
# subsequences does not matter. If no repeated subsequence is found, 
# the function should return an empty set.

def find_repeated_sequences(sequence, k):
    subsequence_set = set()
    result = set()
    if len(sequence) < k:
        return result
    for start in range(len(sequence) - k):
        end = start + k
        hash_value = hash(sequence[start:end])
        if hash_value in subsequence_set:
            result.add(sequence[start:end])
        else:
            subsequence_set.add(hash_value)
    return result


tests = [("AAAAACCCCCAAAAACCCCCC", 8), ("GGGGGGGGGGGGGGGGGGGGGGGGG", 12)]

for test in tests:
    print(f"input : {test}, output: {find_repeated_sequences(test[0], test[1])}")