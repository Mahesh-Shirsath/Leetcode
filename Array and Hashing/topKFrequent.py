from collections import defaultdict

def topKFrequent(nums, k):
    freqs = defaultdict(int)
    for num in nums:
        freqs[num] += 1

    return sorted(freqs.keys(), key=lambda x: freqs[x], reverse=True)[:k]

test_cases = [
    {
        "nums": [1, 1, 1, 2, 2, 3],
        "k": 2,
        "expected": [1, 2]
    }
]

for test_case in test_cases:
    result = topKFrequent(test_case["nums"], test_case["k"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")