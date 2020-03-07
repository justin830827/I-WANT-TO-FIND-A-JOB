import java.util.*;

public class ThreeSumClosest {
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