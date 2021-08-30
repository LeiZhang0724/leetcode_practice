# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
from typing import Dict, Tuple, List

def two_sum( nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []