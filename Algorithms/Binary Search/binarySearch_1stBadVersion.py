# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Basic problem to use the binary search template

        Args:
            n: Given n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

        Returns:
            the first bad version.

        Example:
            Given n = 5, and version = 4 is the first bad version.

            call isBadVersion(3) -> false
            call isBadVersion(5) -> true
            call isBadVersion(4) -> true

            Then 4 is the first bad version.

        Time Complexity: O(log(n))
        Space Complexity: O(1) 

        """
        left, right = 1, n
        while left < right:
            pivot = left + (right - left) // 2
            if isBadVersion(pivot):
                right = pivot
            else:
                left = pivot + 1

        return left
