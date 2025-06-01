from collections import defaultdict

def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    freqs = defaultdict(int)
    for letter in s:
        freqs[letter] += 1

    lettersFreq = len(freqs)
    for letter in t:
        freqs[letter] -= 1
        if freqs[letter] < 0:
            return False
        if freqs[letter] == 0:
            lettersFreq -= 1
    
    return lettersFreq == 0


test_cases = [
    {
        "s": "anagram",
        "t": "nagaram",
        "expected": True
    }
]

for test_case in test_cases:
    result = validAnagram(test_case["s"], test_case["t"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")