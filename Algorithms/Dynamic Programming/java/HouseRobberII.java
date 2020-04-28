import java.util.Arrays;

/**
 * You are a professional robber planning to rob houses along a street. Each
 * house has a certain amount of money stashed. All houses at this place are
 * arranged in a circle. That means the first house is the neighbor of the last
 * one. Meanwhile, adjacent houses have security system connected and it will
 * automatically contact the police if two adjacent houses were broken into on
 * the same night.
 * 
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight without
 * alerting the police.
 * 
 */
public class HouseRobberII {
    /**
     * @param nums: an interger array without negetive numbers.
     * @return the maximum amount of money
     * 
     *         Time Complexity: O(n), Space Complexity: O(1)
     */
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0)
            return 0;
        return n == 1 ? nums[0]
                : Math.max(helper(Arrays.copyOfRange(nums, 1, n)), helper(Arrays.copyOfRange(nums, 0, n - 1)));
    }

    /**
     * @param nums: a slice array of nums
     * @return the maximum amount of money
     */
    private int helper(int[] nums) {
        int preMax = 0, curMax = 0;
        for (int n : nums) {
            int tmp = curMax;
            curMax = Math.max(preMax + n, curMax);
            preMax = tmp;
        }
        return curMax;
    }
}