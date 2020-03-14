class Solution:
    """
    Given n and k, return the kth permutation sequence.

    For example:
        The set [1,2,3,...,n] contains a total of n! unique permutations.
        By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
        1. "123" 2. "132" 3. "213" 4. "231" 5. "312" 6. "321"
    """

    def getPermutation(self, n: int, k: int) -> str:
        """
        Args:
            n: an interger between 1 and 9 inclusive.
            k: an integer between 1 and n! inclusive.

        Return:
            the kth permutation sequence.

        Note:
            The backtraking solution will lead to TLE

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) 
        """
        seen = [False] * n
        res = []
        self.helper(n, k, "", seen, res)
        return res[k-1]

    def helper(self, n, k, cur, seen, res):
        """
        Args:
            n: an interger between 1 and 9 inclusive.
            k: an integer between 1 and n! inclusive.
            cur: a List to save the current solution.
            seen: a list to record which point has been visited.
            res: a List to save the all possible solutions.

        Return:
            None
        """
        if len(cur) == n:
            res.append(cur[:])

        for i in range(1, n + 1):
            if seen[i-1]:
                continue
            cur += str(i)
            seen[i - 1] = True
            self.helper(n, k, cur, seen, res)
            cur = cur[:-1]
            seen[i - 1] = False
