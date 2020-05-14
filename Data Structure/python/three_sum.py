from typing import List


class Solution:
    """
    Args:
        nums: Given an array of integers with negative value and duplicates.

    Returns:
        return all unique triplets in the array which gives the sum of zero.

    Idea of Solution:
       The idea is to sort an input array and then run through all indices of a possible first element of a triplet.
       For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array.
       Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort first
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # Break the loop if there is no possible solution. i.e. the min in array is greater than 0.
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Two pointer
            left, right = i + 1, len(nums) - 1
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Remove duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                if target > 0:
                    right -= 1
                if target < 0:
                    left += 1
        return res
