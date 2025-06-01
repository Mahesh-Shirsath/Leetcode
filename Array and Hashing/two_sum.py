def two_sum(nums, target):
    pair_idx = {}

    for index, value in enumerate(nums):
        if target - value in pair_idx:
            return [pair_idx[target - value], index]
        pair_idx[value] = index

    return []

test_cases = [
    {
        "nums": [2, 7, 11, 15],
        "target": 9,
        "expected": [0, 1]
    },
    {
        "nums": [3, 2, 4],
        "target": 6,
        "expected": [1, 2]
    },
    {
        "nums": [3, 3],
        "target": 6,
        "expected": [0, 1]
    }
]

for test_case in test_cases:
    result = two_sum(test_case["nums"], test_case["target"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")