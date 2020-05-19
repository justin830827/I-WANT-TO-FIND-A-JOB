/**
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 * 
 * Example:
 * 
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 * 
 * A solution set is: [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]
 * 
 * Idea of solution: Use the same technique on 3sum and 3sum cloest, 3sum
 * smaller problems, but add one more loop so that we fix the first and second
 * element and two pointer to search the results.
 */
public class FourSum {
    /***
     * 
     * @param nums:   Given an array of integers.
     * @param target: an integer
     * @return the number of index triplets that the sum is smaller than target
     * 
     *         Time Complexity: O(n^3), Space Complexity: O(1)
     */
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i - 1] == nums[i])
                continue;
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j - 1] == nums[j])
                    continue;
                int left = j + 1, right = nums.length - 1;
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        res.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[j], nums[left], nums[right])));
                        while (left < right && nums[left + 1] == nums[left])
                            left++;
                        while (left < right && nums[right - 1] == nums[right])
                            right--;
                    }
                    if (sum < target)
                        left++;
                    else
                        right--;
                }
            }
        }
        return res;
    }
}