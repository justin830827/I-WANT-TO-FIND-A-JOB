from typing import List


class Solution:
    """
    Given an integer array nums, find the contiguous subarray within an array
    (containing at least one number) which has the largest product.

    Example:
        Input: [2,3,-2,4]
        Output: 6

        Input: [-2,0,-1]
        Output: 0

    Idea of solution:
        We first don't consider 0 in the array, the problem will be
        very simple. if there is only odd number of negative integer, then the
        maximum will be the prod of subarray berfore/affter the negative integer.

        For example: 
            1. arr = [+,+,-,+] => max = arr[0] * arr[1] or arr[3] 
            2. arr = [+,-,+,-,-,+] => max = arr[0] or arr[2:] or arr[5] or arr[:4].

        Either way we can have max from prefix or postfix of product of subarray.
        Now, if we consider 0 in the array, then we only start the value next to 0 on
        both prefix or postfix.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """
        Args:
            nums: an integer array with both negative and positive integers.

        Returns:
            the maximum product of subaray.

        Time Complexity: O(n)
        Space Complexity: O(1) 
        """
        pos = neg = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                pos, neg = neg, pos
            pos = max(nums[i], pos * nums[i])
            neg = min(nums[i], neg * nums[i])
            res = max(res, pos)
        return res
