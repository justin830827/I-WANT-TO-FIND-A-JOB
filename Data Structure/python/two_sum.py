from typing import List


class Solution:
    """
    Args:
        nums: Given an array of integers.
        target: the value which can be sum of any two intergers in nums.

    Returns:
        return the indices with the exact one solution of any two intergers in nums

    Idea of Solution:
        Use hash table to save the previous index with desired difference (tagret - nums[i]) as Keys

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                return [table[nums[i]], i]
            else:
                table[target - nums[i]] = i
