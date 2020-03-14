from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Basic problem to use the Combination template

        Args:
            nums: a list of distinct integers.

        Returns:
            return all possible subsets (the power set).

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) 

        """
        res = []
        self.helper(res, [], nums, 0)
        return res

    def helper(self, res: List[List[int]], cur: List[int], nums: List[int], start: int) -> None:
        """Main backtracking function

        Args:
            res: a list to save the all possible solutions.
            nums: the same input. i.e. Given a set of distinct integers.
            cur: a list to save the current solution.
            start: the index start point for exploring. 

        Returns:
            None

        """
        res.append(cur[:])
        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.helper(res, cur, nums, i + 1)
            cur.pop()
