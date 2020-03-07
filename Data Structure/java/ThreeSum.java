import java.util.*;

/**
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the sum
 * of zero.
 * 
 * Idea of solution: we essentially need to find three numbers x, y, and z such
 * that they add up to the given value. If we fix one of the numbers say x, we
 * are left with the two-sum problem at hand!
 * 
 * Time Complexity: O(n^2), Space Complextiy: O(1)
 */

public class ThreeSum {
    /**
     * @param nums: an interger array with negative and duplicates.
     * @return a list of all unique triplets in the array with sum = 0
     */
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            // Two pointers to find solution
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[left], nums[right])));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1])
                        left++;
                    while (left < right && nums[right] == nums[right + 1])
                        right--;
                }
                if (sum > 0)
                    right--;
                if (sum < 0)
                    left++;
            }
        }
        return res;
    }
}