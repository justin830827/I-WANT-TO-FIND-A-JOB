from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Args:
            matrix: a m x n integer matrix.

        Returns:
            a list with spiral order of matrix.

        Example:
            Input:
            [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
            ]
            Output: [1,2,3,6,9,8,7,4,5]

        Time Complexity: O(n)
        Space Complexity: O(1) 
        """
        res = []
        if not matrix: return res
        m, n = len(matrix), len(matrix[0])
        rs, re, cs, ce = 0, m-1, 0, n-1
        while rs <= re and cs <= ce:
            # start from left to right
            for i in range(cs, ce + 1):
                res.append(matrix[rs][i])
            rs += 1
            for i in range(rs, re + 1):
                res.append(matrix[i][ce])
            ce -= 1
            if rs <= re:
                for i in range(ce, cs - 1, -1):
                    res.append(matrix[re][i])
                re -= 1
            if cs <= ce:
                for i in range(re, rs - 1, -1):
                    res.append(matrix[i][cs])
                cs += 1
        return res