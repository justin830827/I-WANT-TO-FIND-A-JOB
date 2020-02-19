import java.util.Arrays;

/**
 * Create an class with function to calcaute the product except itself without
 * using division.
 * 
 * Time Complexity: O(n) Space Complexity: O(n)
 */

public class ProductExceptSelf {
    /**
     * 
     * @param nums: an array nums of n integers where n > 1.
     * @return an array output such that output[i] is equal to the product of all
     *         the elements of nums except nums[i].
     */
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        res[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        int prod = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            prod *= nums[i + 1];
            res[i] *= prod;
        }
        return res;
    }

    public static void main(String[] args) {
        int[] input = { 1, 2, 3, 4 };
        int[] test = new ProductExceptSelf().productExceptSelf(input);
        System.out.println(Arrays.toString(test));
    }
}