from typing import List


class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Idea of Solution:
        Use hash table to save the previous index with desired difference (tagret - nums[i]) as Keys.

    Example:
        Input: [2, 7, 11, 15], target = 9,
        Output: [0, 1].
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums: Given an array of integers.
            target: the value which can be sum of any two intergers in nums.

        Returns:
            return the indices with the exact one solution of any two intergers in nums

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                return [table[nums[i]], i]
            else:
                table[target - nums[i]] = i
