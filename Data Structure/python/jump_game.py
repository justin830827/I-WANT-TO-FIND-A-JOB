class Solution:
    """
    Args:
        nums: an array of non-negative integers.

    Returns:
        return true if you are able to reach the last index. Otherwise, false.

    Example:
        Input: [2,3,1,1,4]
        Output: true

        Input: [3,2,1,0,4]
        Output: false
    
    Idea of solution:
        we use the benefits of Greedy approach. Record the maximum index it can reach,
        if we our current index is greater than the maximum reachable index, then
        we know it is impossible to reach at the end of array.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i in range(len(nums)):
            if i > step:
                return False
            step = max(step, i + nums[i])
        return True