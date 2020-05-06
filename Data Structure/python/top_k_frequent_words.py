import collections
import heapq


class Solution:
    """
    Given a non-empty list of words, return the k most frequent elements.

    Your answer should be sorted by frequency from highest to lowest. If
    two words have the same frequency, then the word with the lower
    alphabetical order comes first.

    Examples:
        Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
        Output: ["i", "love"]

        Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
        Output: ["the", "is", "sunny", "day"]

    Idea of Solution: HashTable + Heap

    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Args:
            words: a non-empty list of words(string)
            k: the number of most frequent word

        Return:
            a list contain k most frequent words.

        Time Complexity: O(logk)
        Space Complexity: O(n)
        """
        cnt = collections.Counter(words)
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
