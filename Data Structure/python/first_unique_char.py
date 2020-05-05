import collections


class Solution:
    """
    Given a string containing only lowercase letters, find the first non-repeating
    character in it and return it's index. If it doesn't exist, return -1.

    Example:
        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.

    Idea of solution:
        1. HashTable: record the occurence in Hash Table and loop over to find the first char with occurence = 1
        2. Array:  record the occurence in array(size = 26) and loop over to find the first char with occurence = 1
    """

    def firstUniqCharHashTable(self, s: str) -> int:
        """
        Args:
            s: a string with lowercase letters.

        Return
            the index of first unique char if the unique char exists, else -1

        Time Complexity: O(n)
        Space Complexity: O(26) => O(1)
        """
        cnt = collections.Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

    def firstUniqCharArray(self, s: str) -> int:
        """
        Args:
            s: a string with lowercase letters.

        Return
            the index of first unique char if the unique char exists, else -1

        Time Complexity: O(n)
        Space Complexity: O(26) => O(1)
        """
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for i, c in enumerate(s):
            if cnt[ord(c) - ord('a')] == 1:
                return i
        return -1
