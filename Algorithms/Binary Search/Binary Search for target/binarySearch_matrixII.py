class Solution:
    def searchMatrix(self, matrix, target):
        """
        Args:
            matrix: Given a sorted (in ascending order) integer m x n matrix on both rows and columns.
            target: the value as our target in matrix.

        Returns:
            If target exists, then return true, otherwise return false.

        * NOTE: this is not the optimized solution.
        Time Complexity: O(mlog(n)) 
        Space Complexity: O(1) 
        """
        if not matrix:
            return False

        for row in matrix:
            if self.search(row, target):
                return True
        return False

    def search(self, arr, target):
        """
        Args:
            arr: Given a sorted (in ascending order) integer array.
            target: the value as our target in arr.

        Returns:
            If target exists, then return true, otherwise return false.

        """
        left, right = 0, len(arr)
        while left < right:
            pivot = left + (right-left) // 2
            if arr[pivot] == target:
                return True
            if arr[pivot] < target:
                left = pivot + 1
            else:
                right = pivot
        return False
