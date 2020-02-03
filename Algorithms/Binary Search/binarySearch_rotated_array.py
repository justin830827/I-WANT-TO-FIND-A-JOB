from typing import List


class Solution:
    def two_pass_search(self, nums: List[int], target: int) -> int:
        """This is Two-pass solution in the rotated array problem. 

        Args:
            Given a sorted (in ascending order) integer array is rotated at some pivot unknown to you beforehand.
            (i.e. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        Returns:
            If target exists, then return its index, otherwise return -1.

        The idea of the solution:
            In order to perform binary search, we need to make sure the array is sorted. In this case, the array can be viewd as two part of sorted array.
            Let's assume nums = [4,5,6,7,0,1,2].
            [4,5,6,7] and [0,1,2] are two sorted arrays. Thus, we can employ this idea to find the rotate index and perform the Binary Search on two subarrays.

            How to find the rotated index ?
            Ans: Find the index of minimum in nums

            Since we use Binary search find rotated index first and then perform another Binary Search on desired subarray,
            this appoarch called two-pass search. There is anotehr one-pass approach on the other function.

        Time Complexity: O(log(n))
        Space Complexity: O(1) 

        """

        def find_rotate_index() -> int:
            """Find rotated index. i.e. Find the index of minimum in nums.

            Returns:
                The roated index

            """
            left, right = 0, len(nums)
            while left < right:
                pivot = left + (right - left) // 2
                if nums[pivot] > nums[-1]:
                    left = pivot + 1
                else:
                    right = pivot
            return left

        def binary_search(left: int, right: int) -> int:
            """Perform Binary Search within nums[left : right]

            Args:
                left: left index of nums
                right: right index of nums

            Returns:
                If target exists, then return its index, otherwise return -1.
            """
            while left < right:
                pivot = left + (right - left) // 2
                if nums[pivot] == target:
                    return pivot

                if nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot
            return -1

        left, right = 0, len(nums)

        # Handle corner cases
        if not nums:
            return -1
        if right == 1:
            return 0 if nums[0] == target else -1

        # Get the rotated index
        rotate_index = find_rotate_index()

        if nums[rotate_index] == target:
            return rotate_index

        # If rotate_index == 0 means nums no rotation, search whole nums.
        if rotate_index == 0:
            return binary_search(left, right)

        # If target < nums[0] means the target if on the right-sided nums. Otherwise, return left-sided nums search
        if target < nums[0]:
            return binary_search(rotate_index, right)
        return binary_search(left, rotate_index)

    def one_pass_search(self, nums: List[int], target: int) -> int:
        """This is one-pass solution in the rotated array problem. 

        Args:
            Given a sorted (in ascending order) integer array is rotated at some pivot unknown to you beforehand.
            (i.e. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        Returns:
            If target exists, then return its index, otherwise return -1.

        The idea of the solution:
            In order to perform binary search, we need to make sure the array is sorted. In this case, the array can be viewd as two part of sorted array.
            Let's assume nums = [4,5,6,7,0,1,2].
            [4,5,6,7] and [0,1,2] are two sorted arrays. Thus, we can check if target in the sorted subarray

            Identify target in which subarray:
            1. If nums[0] < nums[pivot]: left is sorted, vice versa.
            2. If target in that subarray, update right index. Otherwise, update left index.


        Time Complexity: O(log(n))
        Space Complexity: O(1) 

        """
        left, right = 0, len(nums)
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot

            # left-sided is sorted
            if nums[pivot] > nums[0]:

                # target on left-sided subarray
                if nums[0] <= target < nums[pivot]:
                    right = pivot

                # tatget is on right-sided subarray
                else:
                    left = pivot + 1
            # right-sided is sorted
            else:
                # target on the right-sided subarray
                if nums[pivot] < target <= nums[-1]:
                    left = pivot + 1

                # target on the left-sided subarray
                else:
                    right = pivot
        return -1
