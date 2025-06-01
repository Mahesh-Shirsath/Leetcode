#product of array except self

def productOfArray(nums):
    count_zero, product = 0, 1
    for i in nums:
        if i == 0:
            count_zero += 1
        else:
            product *= i
        if count_zero == 2:
            return [0] * len(nums)

    if count_zero == 1:
        for i, num in enumerate(nums):
                nums[i] = 0 if num != 0 else product
        return nums
    
    for i, num in enumerate(nums):
        nums[i] = int(product / num)
    
    return nums
    # result = [1] * len(nums)

    # for i in range(1, len(nums)):
    #     result[i] = result[i - 1] * nums[i - 1]

    # right = 1
    # for i in range(len(nums) - 1, -1, -1):
    #     result[i] *= right
    #     right *= nums[i]

    # return result

test_cases = [
    {
        "nums": [1, 2, 3, 4],
        "expected": [24, 12, 8, 6]
    }
]

for test_case in test_cases:
    result = productOfArray(test_case["nums"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")