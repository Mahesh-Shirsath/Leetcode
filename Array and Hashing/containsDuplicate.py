def containsDuplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)

    return False

    #return len(nums) != len(set(nums))

test_cases = [
    {
        "nums": [1, 2, 3, 1],
        "expected": True
    }
]

for test_case in test_cases:
    result = containsDuplicate(test_case["nums"])
    print(result)