from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Basic problem to use the Permutation template

        Args:
            candidates: Given a set of distinct integers.

        Returns:
            return all possible solutions.

        Example:
            Input: [1,2,3]
            Output:
            [
                [1,2,3],
                [1,3,2],
                [2,1,3],
                [2,3,1],
                [3,1,2],
                [3,2,1]
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
            res: A List to save the all possible solutions.
            nums: The same input. i.e. Given a set of distinct integers.
            cur: A List to save the current solution.
            visited: A list to record which point has been visited.

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
