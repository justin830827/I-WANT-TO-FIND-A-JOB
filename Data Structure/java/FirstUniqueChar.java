import java.util.*;

/**
 * Given a string containing only lowercase letters, find the first
 * non-repeating character in it and return it's index. If it doesn't exist,
 * return -1.
 * 
 * Example: s = "leetcode" return 0.
 * 
 * s = "loveleetcode", return 2.
 * 
 * Idea of solution:
 * 
 * 1. HashTable: record the occurence in Hash Table and loop over to find the
 * first char with occurence = 1
 * 
 * 2. Array: record the occurence in array(size = 26) and loop over to find the
 * first char with occurence = 1
 */

public class FirstUniqueChar {
    /**
     * 
     * @param s: a string with lowercase letters.
     * @return the index of first unique char if the unique char exists, else -1
     * 
     *         Time Complexity: O(n) Space Complexity: O(26) => O(1)
     */
    public int firstUniqCharHashTable(String s) {
        HashMap<Character, Integer> cnt = new HashMap<>();
        for (char c : s.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            if (cnt.get(s.charAt(i)) == 1)
                return i;
        }
        return -1;
    }

    /**
     * 
     * @param s: a string with lowercase letters.
     * @return the index of first unique char if the unique char exists, else -1
     * 
     *         Time Complexity: O(n) Space Complexity: O(26) => O(1)
     */
    public int firstUniqCharArray(String s) {

        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }

        for (int i = 0; i < s.length(); i++) {
            if (cnt[s.charAt(i) - 'a'] == 1)
                return i;
        }
        return -1;
    }

}