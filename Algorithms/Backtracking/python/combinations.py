class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    Example:
        Input: n = 4, k = 2
        Output:
        [
            [2,4],
            [3,4],
            [2,3],
            [1,2],
            [1,3],
            [1,4],
        ]
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Args:
            n: an integer indicates the end number of [1.....n]
            k: an integer indicates the length of combinations.

        Return:
            a list of all the combination
        """
        res = []
        self.helper(res, [], n, k, 1)
        return res

    def helper(self, res, cur, n, k, start):
        """
        Args:
            res: a list to save the all possible solutions.
            cur: a list to save the current solution.
            n: an integer indicates the end number of [1.....n]
            k: an integer indicates the length of combinations.
            start: the index start point for exploring.

        Return:
            None
        """
        if len(cur) == k:
            res.append(cur[:])
            return

        for i in range(start, n + 1):
            cur.append(i)
            self.helper(res, cur, n, k, i + 1)
            cur.pop()

    def helper_optimized(self, res, cur, n, k, start):
        """
        Args:
            res: a list to save the all possible solutions.
            cur: a list to save the current solution.
            n: an integer indicates the end number of [1.....n]
            k: an integer indicates the length left of current combination.
            start: the index start point for exploring.

        Return:
            None

        Note: one trick here is we only run the combinations with valid length
        """
        if k == 0:
            res.append(cur[:])
            return

        for i in range(start, n - k + 2):
            cur.append(i)
            self.helper(res, cur, n, k - 1, i + 1)
            cur.pop()
