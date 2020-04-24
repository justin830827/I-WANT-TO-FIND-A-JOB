class Solution:
    """
    Given a range [m, n] where 0 <= m <= n <= 2147483647,
    return the bitwise AND of all numbers in this range, inclusive.

    Examples:
        Input: [5,7]
        Output: 4

        Input: [0,1]
        Output: 0

    Idea of solution:
        Core solution: finding the common prefix from [m,n]
        1. Bit shift: shift both numbers to the right, until the numbers become equal,
           i.e. the numbers are reduced into their common prefix. Then we append zeros
           to the common prefix in order to obtain the desired result, by shifting the
           common prefix to the left.
        2. Brian Kernighan's Algorithm:
           When doing AND bit operation between number and number-1, the rightmost bit
           of one in the original number would be turned off (from one to zero).
    
    """
    def rangeBitwiseAndShift(self, m: int, n: int) -> int:
        """
        Args:
            m: the lower bound of range
            n: the upper bound of range
        
        Return:
            the bitwise AND of all numbers in this range, inclusive.

        Time Complexity: O(32) => O(1)
        Space Complexity: O(1)
        """
        if m == 0: return 0
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift

    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        Args:
            m: the lower bound of range
            n: the upper bound of range
        
        Return:
            the bitwise AND of all numbers in this range, inclusive.

        Time Complexity: O(32) => O(1)
        Space Complexity: O(1)
        """
        while m < n:
            n = n & (n-1)
        return m & n
