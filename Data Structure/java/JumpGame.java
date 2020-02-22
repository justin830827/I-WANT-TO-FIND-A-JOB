/**
 * Given an array of non-negative integers, you are initially positioned at the
 * first index of the array.Each element in the array represents your maximum
 * jump length at that position.Determine if you are able to reach the last
 * index.
 * 
 * 
 * Idea of solution: we use the benefits of Greedy approach. Record the maximum
 * index it can reach, if we our current index is greater than the maximum
 * reachable index, then we know it is impossible to reach at the end of array.
 * 
 * Time complexity: O(n), Space complextiy: O(1)
 */
public class JumpGame {
    /**
     * 
     * @param nums: an array of non-negative integers.
     * @return true if you are able to reach the last index. Otherwise, false.
     */
    public boolean canJump(int[] nums) {
        int step = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > step) {
                return false;
            }
            step = Math.max(step, i + nums[i]);
        }
        return true;
    }

    public static void main(String[] args) {
        int[] nums1 = { 2, 3, 1, 1, 4 };
        int[] nums2 = { 3, 2, 1, 0, 4 };
        boolean res1 = new JumpGame().canJump(nums1);
        boolean res2 = new JumpGame().canJump(nums2);
        System.out.println(res1);
        System.out.println(res2);
    }
}