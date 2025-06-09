# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/
from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), key=lambda x: x[0])
    ans, prev = 0, 0
    for pos, spd in cars:
        time = (target - pos) / spd
        if time > prev:
            ans += 1
            prev = time
    return ans

test_cases = [
    [12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]],
    [10, [6, 2, 17], [3, 5, 10]],
]

for test_case in test_cases:
    print(carFleet(*test_case))
