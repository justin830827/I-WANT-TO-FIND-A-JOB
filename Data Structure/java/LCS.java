import java.util.*;

/**
 * Given an unsorted array of integers, find the length of the longest
 * consecutive elements sequence. Your algorithm should run in O(n) complexity.
 * 
 * Idea of Solution: First turn the input into a set of numbers. That takes O(n)
 * and then we can ask in O(1) whether we have a certain number. Then go through
 * the numbers. If the number x is the start of a streak (i.e., x-1 is not in
 * the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not
 * in the set. The length of the streak is then simply y-x and we update our
 * global best with that. Since we check each streak only once, this is overall
 * O(n).
 * 
 * Time Complexity: O(n), Space Complexity: O(n)
 */
public class LCS {
    /**
     * @param nums: Given an unsorted array of integers.
     * @return the length of the longest consecutive elements sequence.
     */
    public int longestConsecutive(int[] nums) {
        // Initialize HashSet
        HashSet<Integer> set = new HashSet<>();
        for (int n : nums)
            set.add(n);
        // Main
        int res = 0;
        for (int n : nums) {
            if (!set.contains(n - 1)) {
                int tmp = n + 1;
                while (set.contains(tmp)) {
                    tmp++;
                }
                res = Math.max(res, tmp - n);
            }
        }
        return res;
    }
}