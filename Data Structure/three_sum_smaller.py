class Solution:
    """
    Given an array of n integers nums and a target, find the number of index triplets i, j, k
    with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    Idea of solution:
        Use the same technique on 3sum and 3sum cloest problems, fix the first elements and use
        two pointer to search the results.
    """

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Args:
            nums: Given an array of integers.
            target: an integer.

        Returns:
            return the number of index triplets that the sum is smaller than target

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res
