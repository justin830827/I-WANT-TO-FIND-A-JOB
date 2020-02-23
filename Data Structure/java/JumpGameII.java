/**
 * Given an array of non-negative integers, you are initially positioned at the
 * first index of the array. Each element in the array represents your maximum
 * jump length at that position.The goal is to reach the last index in the
 * minimum number of jumps.
 * 
 * Time Complexity: O(n), Space Complextiy: O(1)
 */
public class JumpGameII {
    /**
     * 
     * @param nums: given an array of non-negative integers.
     * @return minimum number of jumps to the last element.
     */
    public int jump(int[] nums) {
        int maxReach = 0, end = 0, res = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            maxReach = Math.max(maxReach, i + nums[i]);
            if (i == end) {
                res++;
                end = maxReach;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = { 2, 3, 1, 1, 4 };
        int res = new JumpGameII().jump(nums);
        System.out.println(res);
    }
}