import collections
import heapq


class Solution:
    """
    Given a non-empty array of integers, return the k most frequent elements.

    Examples:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Input: nums = [1], k = 1
        Output: [1]

    Idea of solution:
        1. HashTable + Heap
        2. BucketSort
    """

    def topKFrequentHashTableAndHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Args:
            nums: a non-empty array of integers
            k: a integer indicates the number of frequent elements

        Return:
            the k most frequent elements.

        Time Complexity: O(nlogk)
        Space Complexity: O(n)

        """
        cnt = collections.Counter(nums)
        # The following returns have the same time complexity.
        # return [e for e, _ in cnt.most_common(k)]
        return heapq.nlargest(k, cnt, cnt.get)
