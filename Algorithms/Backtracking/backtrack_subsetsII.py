from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Basic problem to use the Backtracking template

        Args:
            nums: Given a set of integers with duplicate.

        Returns:
            return all possible subsets (the power set).

        * Note: we need to sort before performing backtracking in the array with duplicates 

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) 

        """
        res = []
        self.helper(sorted(res), [], nums, 0)
        return res

    def helper(self, res: List[List[int]], cur: List[int], nums: List[int], start: int) -> None:
        """Main backtracking function

        Args:
            res: A List to save the all possible solutions.
            nums: The same input. i.e. Given a set of distinct integers.
            cur: A List to save the current solution.
            start: the index start point for exploring. 

        Returns:
            None

        """
        res.append(cur[:])
        for i in range(start, len(nums)):

            # Skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue

            cur.append(nums[i])
            self.helper(res, cur, nums, i + 1)
            cur.pop()
