from typing import List


class Solution:
    def isMonotonic_reverse(self, A: List[int]) -> bool:
        """Check the array if in asc order. If not, reverse the array to check.

        Args:
            A: Given a set of integers.

        Returns:
            return true if and only if the given array A is monotonic.

        Example:
            Input: [1,2,2,3]
            Output: true

            Input: [6,5,4,4]
            Output: true

            Input:[1,3,2]
            Output: false

        Idea of solution:
            First check the first and last element in which possible order, then compare if the array is asc.
            In other words, we only need to consider the array if asc order.

        Time Complexity: O(n)
        Space Complexity: O(1) 

        """
        if A[-1] < A[0]:
            A = A[::-1]

        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True

    def isMonotonic_onepass(self, A: List[int]) -> bool:
        """Loop only once and check both asc and desc

        Args:
            A: Given a set of integers.

        Returns:
            return true if and only if the given array A is monotonic.

        Time Complexity: O(n)
        Space Complexity: O(1) 

        """
        asc, des = 1, 1

        for i in range(1, len(A)):
            asc &= A[i] >= A[i-1]
            des &= A[i] <= A[i-1]
        return asc or des
