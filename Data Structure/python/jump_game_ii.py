class Solution:
    """
    Args:
        nums: an array of non-negative integers.

    Returns:
        return the minimum number of jumps to last index.

    Example:
        Input: [2,3,1,1,4]
        Output: 2
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def jump(self, nums: List[int]) -> int:
        max_reach, cur_end, res = 0, 0, 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if i == cur_end:
                res += 1
                cur_end = max_reach
        return res