/**
 * You are a professional robber planning to rob houses along a street. Each
 * house has a certain amount of money stashed, the only constraint stopping you
 * from robbing each of them is that adjacent houses have security system
 * connected and it will automatically contact the police if two adjacent houses
 * were broken into on the same night.
 * 
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight without
 * alerting the police.
 * 
 */
public class HouseRobber {
    /**
     * @param nums: an integer array without negative numbers.
     * @return the maximum amount of money follows the robbing rule.
     * 
     *         Time Complexity: O(n), Space Complexity: O(1)
     */
    public int rob(int[] nums) {
        if (nums.length == 0)
            return 0;
        int preMax = 0, curMax = 0;
        for (int n : nums) {
            int tmp = preMax;
            preMax = curMax;
            curMax = Math.max(tmp + n, curMax);
        }
        return curMax;
    }
}