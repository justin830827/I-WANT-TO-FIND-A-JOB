/**
 * Given an integer array nums, find the contiguous subarray within an array
 * (containing at least one number) which has the largest product.
 * 
 * Idea of solution: We first don't consider 0 in the array, the problem will be
 * very simple. if there is only odd number of negative integer, then the
 * maximum will be the prod of subarray berfore/affter the negative integer.
 * 
 * For example: 1. arr = [+,+,-,+] => max = arr[0] * arr[1] or arr[3] 2. arr =
 * [+,-,+,-,-,+] => max = arr[0] or arr[2:] or arr[5] or arr[:4].
 * 
 * Either way we can have max from prefix or postfix of product of subarray.
 * Now, if we consider 0 in the array, then we only start the value next to 0 on
 * both prefix or postfix.
 * 
 * Time Complexity: O(n), Space Complexity: O(1)
 */
public class MaxProdSubArr {
    /**
     * @param nums: an integer array with both negative and positive integers.
     * @return the maximum product of subaray.
     */
    public int maxProduct(int[] nums) {
        int res = nums[0], pos = nums[0], neg = nums[0];
        for (int i = 1; i < nums.length; i++) {
            // swap min and max if input < 0
            if (nums[i] < 0) {
                int tmp = pos;
                pos = neg;
                neg = tmp;
            }
            pos = Math.max(nums[i], pos * nums[i]);
            neg = Math.min(nums[i], neg * nums[i]);
            res = Math.max(res, pos);
        }
        return res;
    }
}