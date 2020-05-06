import collections
import heapq


class Solution:
    """
    Given a string, sort it in decreasing order based on the frequency of characters.

    Examples:
        Input: "tree"
        Output: "eert"

        Input: "cccaaa"
        Output: "cccaaa"

        Input: "Aabb"
        Output: "bbAa"

    Idea of solution:
        1. HashMap and Sort: HashMap to count the occurence and Sorting the HashMap based on the occurence, then build the string.
        2. HashMap and Heap: HashMap to count the occurence and add all the entry into Max-Heap, then build the string.
    """

    def frequencySortHashMapAndSort(self, s: str) -> str:
        """
        Args:
            s: a string

        Return:
            a new string with the characters from high occurence to low occurence.

        Time Compexity: O(n) if using Counter(), O(nlogn) if using dictionary as counter (Because we need to sort)
        Space Complexity: O(n)
        """
        cnt = collections.Counter(s)
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        return "".join(res)

    def frequencySortHashMapAndHeap(self, s: str) -> str:
        """
        Args:
            s: a string

        Return:
            a new string with the characters from high occurence to low occurence.

        Time Compexity: O(n)
        Space Complexity: O(n)
        """
        cnt = collections.Counter(s)
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        res = []
        while heap:
            v, k = heapq.heappop(heap)
            res += [k] * -v
        return ''.join(res)
