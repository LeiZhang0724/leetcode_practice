# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
from typing import Dict, Tuple, List


def two_sum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):  # i+1, otherwise will loop from first item
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# test case 1
# [3,2,4], 6
# test case 2
# [3,3], 6
