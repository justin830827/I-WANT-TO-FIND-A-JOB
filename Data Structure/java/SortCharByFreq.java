import java.util.*;

/**
 * Given a string, sort it in decreasing order based on the frequency of
 * characters.
 * 
 * Examples: Input: "tree" Output: "eert"
 * 
 * Input: "cccaaa" Output: "cccaaa"
 * 
 * Input: "Aabb" Output: "bbAa"
 * 
 * Idea of solution:
 * 
 * 1. HashMap and Sort: HashMap to count the occurence and Sorting the HashMap
 * based on the occurence, then build the string.
 * 
 * 2. HashMap and Heap: HashMap to count the occurence and add all the entry
 * into Max-Heap, then build the string.
 */
public class SortCharByFreq {
    /**
     * 
     * @param s: a string
     * @return a new string with the characters from high occurence to low
     *         occurence.
     * 
     *         Time Compexity: O(nlogn) Space Complexity: O(n)
     */
    public String frequencySortHashMapAndSort(String s) {
        HashMap<Character, Integer> cnt = new HashMap<>();

        for (char c : s.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }
        List<Character> chars = new ArrayList(cnt.keySet());
        Collections.sort(chars, (a, b) -> (cnt.get(b) - cnt.get(a)));

        StringBuilder sb = new StringBuilder();
        for (Object c : chars) {
            for (int i = 0; i < cnt.get(c); i++) {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    /**
     * 
     * @param s: a string
     * @return a new string with the characters from high occurence to low
     *         occurence.
     * 
     *         Time Compexity: O(n) Space Complexity: O(n)
     */
    public String frequencySortHashMapAndHeap(String s) {
        HashMap<Character, Integer> cnt = new HashMap<>();
        for (char c : s.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }

        PriorityQueue<Character> heap = new PriorityQueue<>((a, b) -> (cnt.get(b) - cnt.get(a)));
        heap.addAll(cnt.keySet());

        StringBuilder sb = new StringBuilder();
        while (!heap.isEmpty()) {
            char c = heap.poll();
            for (int i = 0; i < cnt.get(c); i++) {
                sb.append(c);
            }
        }
        return sb.toString();
    }

}