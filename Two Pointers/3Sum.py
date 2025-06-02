def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return result

test_cases = [
    {
        "nums": [-1, 0, 1, 2, -1, -4],
        "expected": [[-1, -1, 2], [-1, 0, 1]]
    }
]

for test_case in test_cases:
    result = threeSum(test_case["nums"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")