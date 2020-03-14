from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Basic problem to use the Permutation template

        Args:
            candidates: a list of integers, may contain duplicates.

        Returns:
            return all possible solutions.

        Example:
            Input: [1,1,2]
            Output:
            [
                [1,1,2],
                [1,2,1],
                [2,1,1]
            ]

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) 
        """
        res, visited = [], [False for _ in range(len(nums))]
        if not nums:
            return res
        self.helper(nums, res, [], visited)

        return res

    def helper(self, nums, res, cur, visited):
        """Main backtracking function

        Args:
            res: a list to save the all possible solutions.
            nums: the same input. i.e. Given a set of distinct integers.
            cur: a List to save the current solution.
            visited: a list to record which point has been visited.

        Returns:
            None

        """
        if len(cur) == len(nums):
            res.append(cur[:])

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            cur.append(nums[i])
            visited[i] = True
            self.helper(nums, res, cur, visited)
            cur.pop()
            visited[i] = False
