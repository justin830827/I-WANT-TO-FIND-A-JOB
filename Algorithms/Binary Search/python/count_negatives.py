class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """

        Args:
            grid: Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

        Returns:
            Return the number of negative numbers in grid.

        Time Complexity: O(nlog(n))
        Space Complexity: O(1) 
        """
        res = 0
        for row in grid:
            left = self.search(row)
            res += len(row) - left
        return res
    
    def search(self, arr):
        """
        Args:
            arr: a sorted arr with postive and negative numbers.

        Returns:
            Return the leftmost index of negetive numbers in arr. 
        
        Time Complexity: O(log(n))
        Space Complexity: O(1) 

        """
        left, right = 0, len(arr)
        while left < right:
            pivot = left + (right - left) // 2
            if arr[pivot] < 0:
                right = pivot
            else:
                left = pivot + 1
        return left