import java.util.*;

/**
 * Given an array of integers and an integer k, you need to find the total
 * number of continuous subarrays whose sum equals to k.
 * 
 * Idea of Solution: we know the key to solve this problem is SUM[i, j]. So if
 * we know SUM[0, i - 1] and SUM[0, j], then we can easily get SUM[i, j]. To
 * achieve this, we just need to go through the array, calculate the current sum
 * and save number of all seen PreSum to a HashMap.
 * 
 * Time Complexity: O(n), Space Complexity: O(n)
 */

public class SubarraySumEqual {
    /**
     * @param nums: an array of integers with negative numbers and duplicates.
     * @param k:    the target value of sum of subarray.
     * @return the total number of continuous subarrays whose sum equals to k.
     */
    public int subarraySum(int[] nums, int k) {
        int res = 0, cur = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for (int n : nums) {
            cur += n;
            res += map.getOrDefault(cur - k, 0);
            map.put(cur, map.getOrDefault(cur, 0) + 1);
        }
        return res;
    }
}