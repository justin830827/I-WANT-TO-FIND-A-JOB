class Solution:
    def search(self, reader, target):
        """

        Args:
            reader: ArrayReader,the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed)
            target: the value as our target in nums

        Returns:
            If target exists, then return its index, otherwise return -1.

        Time Complexity: O(log(n))
        Space Complexity: O(1) 
        """
        left, right = 0, 1
        while left < right:
            pivot = left + (right-left) // 2
            if reader.get(pivot) == target:
                return pivot

            if reader.get(pivot) < target:
                right *= 2
                left = pivot + 1
            else:
                right = pivot
        return -1
