def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    return s == s[::-1]

test_cases = [
    {
        "s": "racecar",
        "expected": True
    }
]

for test_case in test_cases:
    result = validPalindrome(test_case["s"])
    print(result)