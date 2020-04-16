class Solution:
    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Idea of Solution:
        1. Compare reversed string:
            rebuild a string to filter the non-related character and check if string is equal to its reversed.
        2. Two pointer
    """
    def isPalindromeCompare(self, s: str) -> bool:
        """
        Args:
            s: a string contains alphannumeric characters

        Returns:
            return if the input s is a palindrome

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = ""
        for c in s.lower():
            if c.isalpha() or c.isnumeric():
                res += c
        return res == res[::-1]
    
    def isPalindromeTwoPointer(self, s: str) -> bool:
        """
        Args:
            s: a string contains alphannumeric characters

        Returns:
            return if the input s is a palindrome

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True