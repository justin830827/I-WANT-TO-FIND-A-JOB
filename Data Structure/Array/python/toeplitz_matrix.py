from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """Check whether a matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

        Args:
            matrix: an m x n matrix with integers.

        Returns:
            return True if and only if the matrix is Toeplitz.

        Example:
            Input:
                matrix = [
                    [1,2,3,4],
                    [5,1,2,3],
                    [9,5,1,2]
                ]
            Output: True

            Input:
                matrix = [
                    [1,2],
                    [2,2]
                ]
            Output: False

        Idea of solution:
            We only need to compare the previous row without the last element, i.e. row[:-1],
            and the current row start from the second one, i.e. row[1:] 

        Time Complexity: O(n^2)
        Space Complexity: O(1) 

        """
        if not matrix or not matrix[0]: return false
        
        for i in range(1,len(matrix)):
            if matrix[i-1][:-1] != matrix[i][1:]:
                return False
        return True