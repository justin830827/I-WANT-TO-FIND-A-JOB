from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Args:
            nums: Given a non-empty integer array of size n.

        Returns:
            return the minimum number of moves required to make all array elements equal.

        Example:
            Input: date1 = "2019-06-29", date2 = "2019-06-30"
            Output: 1

            Input: date1 = "2020-01-15", date2 = "2019-12-31"
            Output: 15

        Idea of solution:
            Adding 1 to n - 1 elements is the same as subtracting 1 from one
            element, w.r.t goal of making the elements in the array equal. So,
            best way to do this is make all the elements in the array equal
            to the min element. sum(array) - n * minimum
        
        Time complexity: O(n)
        Space complexity: O(1)
        """
        return sum(nums) - len(nums) * min(nums)