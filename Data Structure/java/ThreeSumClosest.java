import java.util.*;

/**
 * Given an array nums of n integers and an integer target, find three integers
 * in nums such that the sum is closest to target. Return the sum of the three
 * integers. You may assume that each input would have exactly one solution.
 * 
 * Time Complexity: O(n^2), Space Complextiy: O(1)
 */

public class ThreeSumClosest {
    /**
     * @param nums:   an interger array with negative and duplicates.
     * @param target: an interger
     * @return the sum of the three integers is cloest to target. Assume that each
     *         input would have exactly one solution.
     */
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int res = Integer.MAX_VALUE - Math.abs(target); // We need to do this trick since Integer.MIN_VALUE always
                                                        // return negative in Math.abs
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            // Two Pointer
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == target)
                    return sum;
                if (Math.abs(target - sum) < Math.abs(target - res)) {
                    res = sum;
                }
                if (sum > target)
                    right--;
                if (sum < target)
                    left++;
            }
        }
        return res;
    }
}