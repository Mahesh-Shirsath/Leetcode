# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List


def maxArea( height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
    

# Example usage:
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
