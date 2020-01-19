class Solution:
    def rob(self, nums) -> int:
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
        preMax = curMax = 0
        for num in nums:
            preMax, curMax = curMax, max(preMax + num, curMax)
        return curMax

    def rob_circle(self, nums) -> int:
        """Dynamic Programming solution for House Robber problem if the houses arranged in a circle.

        Args:
            nums: Given a list of non-negative integers representing the amount of money of each house.

        Returns:
            Return the maximum amount of money without robbing two adjacent houses.

        Time Complexity: O(n)
        Space Complexity: O(1) 

        """
        if len(nums) == 1:
            return nums[0]
        res = 0
        preMax = curMax = 0
        for num in nums[1:]:
            preMax, curMax = curMax, max(preMax + num, curMax)
        res = max(res, curMax)
        preMax = curMax = 0
        for num in nums[:-1]:
            preMax, curMax = curMax, max(preMax + num, curMax)
        res = max(res, curMax)
        return res
