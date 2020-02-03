from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """This solution with the similar idea on Leetcode #33 one-pass solution.
        Args:
            Given a sorted (in ascending order) integer array with duplicates is rotated at some pivot unknown to you beforehand.
            (i.e. [0,0,2,2,2,6,7] might become [2,6,7,0,0,2,2]).

        Returns:
            If target exists, then return True. Otherwise, return False.

        The idea of the solution:
            The idea is very similar to the previous one which the array only contains unique elements.
            The difference between these two problems is that we need to consider the following situation.

            Assume nums = [1,3,1,1,1], target = 3.
            If we use the same solution as prior, our old solution will not able to identify which side is sorted subarray.
            One way to handle that is to update the left index if nums[left] == nums[pivot] and left < pivot such that we ensure there is only one side is sorted.

            Thus, we will have the values in this case.
            1st iteration:
            nums[pivot] = 1, left = 0, right = 5
            Since nums[left] == nums[pivot] and left < pivot, left updates until nums[left] == 3, where left = 1.

            nums[left:right] = [3,1,1,1], then we can identify the sorted array is on the right side.

            Now, consider the opposite case, which nums = [1,1,1,3,1].
            1st iteration:
            Since nums[left] == nums[pivot] and left < pivot, left updates until nums[left] == 1 where left = 2 = pivot.
            In this case, we can find there is no element on left side, we update left = pivot + 1 and search right-sided subarray.

        Time Complexity: O(n), worst case. O(log(n)) on average.
        Space Complexity: O(1) 
        """
        left, right = 0, len(nums)
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return True

            while nums[left] == nums[pivot] and left < pivot:
                left += 1

            if nums[pivot] >= nums[left]:
                if nums[left] <= target < nums[pivot]:
                    right = pivot
                else:
                    left = pivot + 1
            else:
                if nums[pivot] < target <= nums[right-1]:
                    left = pivot + 1
                else:
                    right = pivot
        return False

    def counter(self, nums: List[int], target: int) -> bool:
        """ This is a cheating solution

        Args:
            Given a sorted (in ascending order) integer array with duplicates is rotated at some pivot unknown to you beforehand.
            (i.e. [0,0,2,2,2,6,7] might become [2,6,7,0,0,2,2]).

        Returns:
            If target exists, then return True. Otherwise, return False.

        The idea of the solution:
            Since the worst case might be O(n), we simply treat is as a regular array and check if element in the array.

        Time Complexity: O(n)
        Space Complexity: O(1) 
        """
        return nums.count(target) > 0
