import java.util.*;

/**
 * Given a non-empty array of integers, return the k most frequent elements.
 * 
 * Examples:
 * 
 * Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2]
 * 
 * Input: nums = [1], k = 1 Output: [1]
 * 
 * Idea of solution:
 * 
 * 1. HashTable + Heap
 * 
 * 2. BucketSort
 */
public class TopKFreqElements {
    /***
     * 
     * @param nums: a non-empty array of integers.
     * @param k:    a integer indicates the number of frequent elements.
     * @return the k most frequent elements.
     * 
     *         Time Complexity: O(nlogk), Space Complexity: O(n)
     */
    public int[] topKFrequentHashTableAndHeap(int[] nums, int k) {
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for (int num : nums) {
            cnt.put(num, cnt.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> cnt.get(b) - cnt.get(a));
        heap.addAll(cnt.keySet());

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = heap.poll();
        }
        return res;
    }

}