class Solution:
    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place and use only constant extra memory.

    Example:
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1

    Idea of solution: 
        1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
        2. Find the largest index l greater than k such that a[k] < a[l].
        3. Swap the value of a[k] with that of a[l].
        4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
    """

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Args:
            nums: an integer array.

        Return:
            None, modify nums in-place instead.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        k, l = -1, -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                k = i - 1
        if k > -1:
            l = k + 1
            for j in range(k + 1, len(nums)):
                if nums[j] > nums[k]:
                    l = j
            # Swap
            nums[k], nums[l] = nums[l], nums[k]
        self.reverse(nums, k + 1, len(nums) - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """Reverse the array between start and end index
        Args:
            nums: an integer array.
            start: the begining index.
            end: the ending index.

        Return:
            None, modify nums in-place instead.

        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
