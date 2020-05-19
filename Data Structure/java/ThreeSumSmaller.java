/**
 * Given an array of n integers nums and a target, find the number of index
 * triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
 * nums[j] + nums[k] < target.
 * 
 * Idea of solution: Use the same technique on 3sum and 3sum cloest problems,
 * fix the first elements and use two pointer to search the results.
 */
public class ThreeSumSmaller {
    /***
     * 
     * @param nums:   Given an array of integers.
     * @param target: an integer
     * @return the number of index triplets that the sum is smaller than target
     * 
     *         Time Complexity: O(n^2), Space Complexity: O(1)
     */
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int res = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < target) {
                    res += right - left;
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        return res;
    }
}