# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

test_cases = [
    [73, 74, 75, 71, 69, 72, 76, 73],
    [30, 40, 50, 60],
    [30, 60, 90],
]

for test_case in test_cases:
    print(dailyTemperatures(test_case))