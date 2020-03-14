class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    The goal is to reach the last index in the minimum number of jumps.

    Example:
        Input: [2,3,1,1,4]
        Output: 2
    """

    def jump(self, nums: List[int]) -> int:
        """
        Args:
            nums: an array of non-negative integers.

        Returns:
            return the minimum number of jumps to last index.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        max_reach, cur_end, res = 0, 0, 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if i == cur_end:
                res += 1
                cur_end = max_reach
        return res
