import java.util.*;

/**
 * Given an array of integers, find indices of the two numbers such that they
 * add up to a specific target.
 * 
 * Example:
 * 
 * Input: nums = [2, 7, 11, 15], target = 9 Output: [0,1]
 * 
 * Idea of Solution: use hash table to save the previous index with desired
 * difference (tagret - nums[i]) as Keys
 * 
 * Time Complexity: O(n) Space Complexity: O(n)
 */

public class TwoSum {
    /**
     * 
     * @param nums:   interger array.
     * @param target: integer.
     * @return integer array with two indices.
     */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] res = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                res[0] = map.get(nums[i]);
                res[1] = i;
                break;
            } else {
                map.put(target - nums[i], i);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] input = { 2, 7, 11, 15 };
        int target = 9;
        int[] ans = new TwoSum().twoSum(input, target);
        System.out.println(Arrays.toString(ans));
    }
}