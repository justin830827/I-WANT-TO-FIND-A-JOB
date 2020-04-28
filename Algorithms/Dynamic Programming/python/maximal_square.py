class Solution:
    """
    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example:
        Input: 
            1 0 1 0 0
            1 0 1 1 1
            1 1 1 1 1
            1 0 0 1 0
    Output: 4

    Idea of solution:
        Using dynamic programing the maximum edge on the current cell. To achieve,
        We need to compare the cell on matrix[i-1][j-1], matrix[i-1][j], matrix[i][j].
        Find the minimum amoing the cells if the current cell is equal to "1".

    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Args:
            matrix: a 2D array with '1' and '0'

        Return
            the largest area of square of '1'

        Time Complexity: O(mn)
        Sapce Complexity: O(mn)
        """
        res = 0
        if not matrix:
            return res
        dp = [[0 for _ in range(len(matrix[0]) + 1)]
              for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res ** 2
