#longest consecutive sequence

def longestConsecutiveSeq(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in nums_set:
            length = 1
            while num + length in nums_set:
                length += 1
        longest = max(longest, length)

    return longest

test_cases = [
    {
        "nums": [100, 4, 200, 1, 3, 2],
        "expected": 4
    }
]

for test_case in test_cases:
    result = longestConsecutiveSeq(test_case["nums"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")