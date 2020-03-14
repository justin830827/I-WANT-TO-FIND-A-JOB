import java.util.*;

/**
 * Given a set of candidate numbers (candidates) (without duplicates) and a
 * target number (target), find all unique combinations in candidates where the
 * candidate numbers sums to target. The same repeated number may be chosen from
 * candidates unlimited number of times.
 * 
 * Time Complexity: O(n * 2^n), Space Complexity: O(2^n)
 */
public class CombinationSum {
    /**
     * @param candidates: Given a set of distinct integers.
     * @param target:     A interger to meet the requirement.
     * @return all possible solutions with sum == target.
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        helper(res, new ArrayList<Integer>(), candidates, target, 0, 0);
        return res;
    }

    /**
     * @param res:        A List to save the all possible solutions.
     * @param cur:        A List to save the current solution.
     * @param candidates: The same input. i.e. Given a set of distinct integers.
     * @param target:     A interger to meet the requirement.
     * @param start:      the index start point for exploring.
     * @param sum:        the sum of cur array.
     */
    private void helper(List<List<Integer>> res, List<Integer> cur, int[] candidates, int target, int start, int sum) {
        if (sum == target)
            res.add(new ArrayList(cur));
        for (int i = start; i < candidates.length; i++) {
            if (sum < target) {
                sum += candidates[i];
                cur.add(candidates[i]);
                helper(res, cur, candidates, target, i, sum);
                sum -= cur.get(cur.size() - 1);
                cur.remove(cur.size() - 1);
            }
        }
    }

    // TODO: Add a DP solution
    public List<List<Integer>> dp(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        return res;
    }
}