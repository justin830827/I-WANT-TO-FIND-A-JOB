from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Basic problem to use the Combination template

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
        self.helper(res, [], candidates, target, 0, 0)
        return res

        return res

    def helper(self, res: List[int], cur: List[int], candidates: List[int], target: int, start: int, cur_sum: int) -> None:
        """Main backtracking function

        Args:
            res: A List to save the all possible solutions.
            cur: A List to save the current solution.
            candidates: The same input. i.e. Given a set of distinct integers.
            target: A interger to meet the requirement.
            start: the index start point for exploring.
            cur_sum: the sum of cur array.


        Returns:
            None

        * Note: the performance can be slightly better if we choose the remaining = tartget - arr[i] (i.e. O(1)),
        intead of sum all the list (i.e. O(n)). However, consider the time complexity of backtracking is larger than O(n),
        it is relative trivial to optimize it here. 

        """
        if cur_sum == target:
            res.append(cur[:])

        for i in range(start, len(candidates)):
            if cur_sum < target:
                cur.append(candidates[i])
                cur_sum += candidates[i]
                self.helper(res, cur, candidates, target, i, cur_sum)
                cur_sum -= cur.pop()

    # TODO: This question has a DP solution, will do later.
    def dp(self):
        """Dynamic Programming solution
        """
        return None
