import collections
from typing import List


class Solution:
    """
    You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
    Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
    Find out how many ways to assign symbols to make sum of integers equal to target S.

    Example:
        Input: nums is [1, 1, 1, 1, 1], S is 3. 
        Output: 5
    """

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        Args:
            nums: an integer array.

        Return:
            the number of how many ways to assign symbols to make sum of integers equal to target S.

        Idea of solution:

        Time Complextiy: O(n)
        Space Complexity: O(n)
        """
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        for n in nums:
            step = collections.defaultdict(int)
            for c in cnt:
                step[c + n] += cnt[c]
                step[c - n] += cnt[c]
            cnt = step
        return cnt[S]
