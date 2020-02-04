from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Basic problem to use the Backtracking template

        Args:
            candidates: Given a set of distinct integers.
            target:  A interger to meet the requirement.

        Returns:
            return all possible solutions with sum == target.

        Example:
            candidates = [2,3,6,7], target = 7

            Thus, res = [ [7], [2,2,3] ] 

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) 
        """
        res = []
        if not candidates:
            return res
        self.helper(candidates, res, 0, [], target)

        return res

    def helper(self, arr: List[int], res: List[int], start: int, cur: List[int], target: int) -> None:
        """Main backtracking function

        Args:
            res: A List to save the all possible solutions.
            arr: The same input. i.e. Given a set of distinct integers.
            cur: A List to save the current solution.
            start: the index start point for exploring.
            target: A interger to meet the requirement. 

        Returns:
            None

        * Note: the performance can be slightly better if we choose the remaining = tartget - arr[i] (i.e. O(1)),
        intead of sum all the list (i.e. O(n)). However, consider the time complexity of backtracking is larger than O(n),
        it is relative trivial to optimize it here. 

        """

        if sum(cur) == target:
            res.append(cur[:])

        for i in range(start, len(arr)):
            if sum(cur) < target:
                cur.append(arr[i])
                self.helper(arr, res, i, cur, target)
                cur.pop()

    # TODO: This question has a DP solution, will do later.
    def dp(self):
        """Dynamic Programming solution
        """
        return None
