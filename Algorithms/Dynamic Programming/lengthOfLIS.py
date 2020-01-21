from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Dynamic Programming solution for coinChange problem.

        Args:
            nums: Given an unsorted array of integers.

        Returns:
            The length of longest increasing subsequence.

        Time Complexity: O(n^2)
        Space Complexity: O(n) 

        """
        if not nums:
            return 0
        n, res = len(nums), 0
        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
