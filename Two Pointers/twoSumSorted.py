def twoSumSorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return []

test_cases = [
    {
        "nums": [2, 7, 11, 15],
        "target": 9,
        "expected": [0, 1]
    }
]

for test_case in test_cases:
    result = twoSumSorted(test_case["nums"], test_case["target"])
    print(result)