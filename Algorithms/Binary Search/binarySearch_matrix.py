from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Args:
            matrix: Given a sorted (in ascending order) integer m x n matrix.
            target: the value as our target in matrix

        Returns:
            If target exists, then return true, otherwise return false.

        Time Complexity: O(log(m) + log(n))
        Space Complexity: O(1) 
        """
        if not matrix:
            return False

        left, right = 0, len(matrix)
        while left < right:
            pivot = left + (right - left) // 2
            if not matrix[pivot]:
                return False
            if matrix[pivot][0] <= target <= matrix[pivot][-1]:
                return self.search(matrix[pivot], target)

            if matrix[pivot][0] > target:
                right = pivot
            else:
                left = pivot + 1
        return False

    def search(self, arr, target):
        """
        Args:
            arr: Given a sorted (in ascending order) integer array.
            target: the value as our target in arr

        Returns:
            If target exists, then return true, otherwise return false.

        """

        left, right = 0, len(arr)
        while left < right:
            pivot = left + (right - left) // 2
            if arr[pivot] == target:
                return True

            if arr[pivot] < target:
                left = pivot + 1
            else:
                right = pivot
        return False
