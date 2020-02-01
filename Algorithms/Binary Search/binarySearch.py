from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Basic problem to use the binary search template

        Args:
            nums: Given a sorted (in ascending order) integer array. n: [1,1000], elements range: [-9999,9999]
            target: the value as our target in nums

        Returns:
            If target exists, then return its index, otherwise return -1.

        Time Complexity: O(log(n))
        Space Complexity: O(1) 

        """
        left, right = 0, len(nums)
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot
        return -1
