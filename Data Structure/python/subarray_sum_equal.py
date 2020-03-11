from typing import List


class Solution:
    """
    Args:
        nums: an array of integers with negative numbers and duplicates.
        k: the target value of sum of subarray.

    Returns:
        return the total number of continuous subarrays whose sum equals to k.

    Idea of Solution:
        we know the key to solve this problem is SUM[i, j]. So if we know SUM[0, i - 1]
        and SUM[0, j], then we can easily get SUM[i, j]. To achieve this, we just need
        to go through the array, calculate the current sum and save number of all seen 
        PreSum to a HashMap.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cur, cnt = 0, 0, {0: 1}
        for n in nums:
            cur += n
            res += cnt.get(cur - k, 0)
            cnt[cur] = cnt.get(cur, 0) + 1
        return res
