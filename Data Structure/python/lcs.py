from typing import List


class Solution:
    """
    Args:
        nums: Given an unsorted array of integers.

    Returns:
        return the length of the longest consecutive elements sequence.

    Idea of Solution:
        First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1)
        whether we have a certain number. Then go through the numbers. If the number x is the 
        start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and
        stop at the first number y not in the set. The length of the streak is then simply y-x
        and we update our global best with that. Since we check each streak only once, this is
        overall O(n).

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in hashset:
                y = n + 1
                while y in hashset:
                    y += 1
                res = max(res, y - n)
        return res
