class Solution:
    """
    Given an array nums of n integers and an integer target, are there elements a, b,
    c, and d in nums such that a + b + c + d = target. Find all unique quadruplets in
    the array which gives the sum of target.

    Idea of solution:
        Use the same technique on 3sum and 3sum cloest, 3sum smaller problems, but add
        one more loop so that we fix the first and second element and two pointer to
        search the results.
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Args:
            nums: Given an array of integers.
            target: an integer.

        Returns:
            return the number of index triplets that the sum is smaller than target

        Time Complexity: O(n^3)
        Space Complexity: O(1)
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    cur = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                    if cur < target:
                        left += 1
                    else:
                        right -= 1
        return res
