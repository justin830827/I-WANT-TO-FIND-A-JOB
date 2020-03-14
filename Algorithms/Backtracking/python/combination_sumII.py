from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Basic problem to use the Combination template

        Args:
            candidates: a list of integers, may contain duplicates.
            target:  a interger to meet the requirement.

        Returns:
            Each number in candidates may only be used once in the combination.
            return all possible solutions with sum == target.

        Example:
            Input: candidates = [10,1,2,7,6,1,5], target = 8
            A solution set is:
            [
                [1, 7],
                [1, 2, 5],
                [2, 6],
                [1, 1, 6]
            ]

        * Note: we need to sort before performing backtracking in the array with duplicates.

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) 
        """
        res = []
        if not candidates:
            return res
        self.helper(sorted(candidates), res, 0, [], target)

        return res

    def helper(self, arr: List[int], res: List[int], start: int, cur: List[int], target: int) -> None:
        """Main backtracking function

        Args:
            res: a list to save the all possible solutions.
            arr: the same input. i.e. Given a set of distinct integers.
            cur: a list to save the current solution.
            start: the index start point for exploring.
            target: a interger to meet the requirement. 

        Returns:
            None

        * Note: the performance can be slightly better if we choose the remaining = tartget - arr[i] (i.e. O(1)),
        intead of sum all the list (i.e. O(n)). However, consider the time complexity of backtracking is larger than O(n),
        it is relative trivial to optimize it here. 

        """

        if sum(cur) == target:
            res.append(cur[:])

        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            if sum(cur) < target:
                cur.append(arr[i])
                self.helper(arr, res, i + 1, cur, target)
                cur.pop()

    # TODO: This question has a DP solution, will do later.
    def dp(self):
        """Dynamic Programming solution
        """
        return None
