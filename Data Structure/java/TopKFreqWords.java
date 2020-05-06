import java.util.*;

/**
 * Given a non-empty list of words, return the k most frequent elements.
 * 
 * Your answer should be sorted by frequency from highest to lowest. If two
 * words have the same frequency, then the word with the lower alphabetical
 * order comes first.
 * 
 * Examples:
 * 
 * Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 * 
 * Output: ["i", "love"]
 * 
 * Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
 * "is"], k = 4
 * 
 * Output: ["the", "is", "sunny", "day"]
 * 
 * Idea of Solution: HashTable + Heap
 * 
 */

public class TopKFreqWords {
    /***
     * 
     * @param words: a non-empty list of words(string)
     * @param k:     the number of most frequent word
     * @return a list contain k most frequent words.
     * 
     *         Time Complexity: O(nlogk), Space Complexity: O(n)
     */
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> cnt = new HashMap<>();
        for (String word : words) {
            cnt.put(word, cnt.getOrDefault(word, 0) + 1);
        }

        PriorityQueue<String> heap = new PriorityQueue<>((a, b) -> {
            if (cnt.get(b) == cnt.get(a))
                return a.compareTo(b);
            return cnt.get(b) - cnt.get(a);
        });
        heap.addAll(cnt.keySet());

        List<String> res = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            res.add(heap.poll());
        }
        return res;
    }
}