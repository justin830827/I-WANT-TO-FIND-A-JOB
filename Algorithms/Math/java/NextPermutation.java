/**
 * Implement next permutation, which rearranges numbers into the
 * lexicographically next greater permutation of numbers. If such arrangement is
 * not possible, it must rearrange it as the lowest possible order (ie, sorted
 * in ascending order). The replacement must be in-place and use only constant
 * extra memory.
 * 
 * Example: 1. 1,2,3 → 1,3,2
 * 
 * 2. 3,2,1 → 1,2,3
 * 
 * 3. 1,1,5 → 1,5,1
 * 
 * Idea of solution:
 * 
 * 1. Find the largest index k such that a[k] < a[k + 1]. If no such index
 * exists, the permutation is the last permutation.
 * 
 * 2. Find the largest index l greater than k such that a[k] < a[l].
 * 
 * 3. Swap the value of a[k] with that of a[l].
 * 
 * 4. Reverse the sequence from a[k + 1] up to and including the final element
 * a[n].
 */
public class NextPermutation {
    /**
     * 
     * @param nums: an integer array.
     * 
     *              Time Complexity: O(n), Spae Complexity: O(1)
     */
    public void nextPermutation(int[] nums) {
        int k = -1, l = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1])
                k = i - 1;
        }
        if (k > -1) {
            for (int j = k + 1; j < nums.length; j++) {
                if (nums[j] > nums[k])
                    l = j;
            }
            swap(nums, k, l);
        }
        reverse(nums, k + 1, nums.length - 1);
    }

    /**
     * 
     * @param nums: an integer array.
     * @param k:    the index of k in algorithm
     * @param l:    the index of l in algorithm
     */
    private void swap(int[] nums, int k, int l) {
        int tmp = nums[k];
        nums[k] = nums[l];
        nums[l] = tmp;
    }

    /**
     * Reverse the array between start and end indexes.
     * 
     * @param nums:  an integer array.
     * @param start: the begining index.
     * @param end:   the ending index.
     */
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

}