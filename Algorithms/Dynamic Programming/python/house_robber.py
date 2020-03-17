from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Dynamic Programming solution for House Robber problem.

        Args:
            nums: Given a list of non-negative integers representing the amount of money of each house.

        Returns:
            Return the maximum amount of money without robbing two adjacent houses.

        Time Complexity: O(n)
        Space Complexity: O(1) 

        """
        if not nums:
            return 0
        pre_max = cur_max = 0
        for n in nums:
            pre_max, cur_max = cur_max, max(pre_max + n, cur_max)
        return cur_max

    def rob_circle(self, nums: List[int]) -> int:
        """Dynamic Programming solution for House Robber problem if the houses arranged in a circle.

        Args:
            nums: Given a list of non-negative integers representing the amount of money of each house.

        Returns:
            Return the maximum amount of money without robbing two adjacent houses.

        Time Complexity: O(n)
        Space Complexity: O(1) 

        """
        return nums[0] if len(nums) == 1 else max(self.rob(nums[1:]), self.rob(nums[:-1]))
