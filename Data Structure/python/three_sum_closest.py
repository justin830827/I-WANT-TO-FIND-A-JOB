from typing import List


class Solution:
    """
    Args:
        nums: Given an array of integers with negative value and duplicates.

    Returns:
        return the sum of the three integers is cloest to target. Assume that each input would have exactly one solution.

    Idea of Solution:
        Similar to 3 Sum problem, use 3 pointers to point current element, next element and the last element.
        If the sum is less than target, it means we have to add a larger element so next element move to the next.
        If the sum is greater, it means we have to add a smaller element so last element move to the second last element.
        Keep doing this until the end. Each time compare the difference between sum and target, 
        if it is less than minimum difference so far, then replace result with it, otherwise keep iterating.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Two Pointer
            left, right = i + 1, len(nums) - 1
            while left < right:
                cloest = nums[i] + nums[left] + nums[right]
                if cloest == target:
                    return cloest
                if abs(target - cloest) < abs(target - res):
                    res = cloest
                if cloest > target:
                    right -= 1
                if cloest < target:
                    left += 1
        return res
