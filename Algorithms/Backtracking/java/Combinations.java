import java.util.*;

/**
 * Given two integers n and k, return all possible combinations of k numbers out
 * of 1 ... n.
 */

public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        helper(n, k, res, new ArrayList<Integer>(), 1);
        return res;

    }

    private void helper(int n, int k, List<List<Integer>> res, List<Integer> cur, int start) {
        if (k == 0) {
            res.add(new ArrayList<Integer>(cur));
            return;
        }

        for (int i = start; i < n - k + 2; i++) {
            cur.add(i);
            helper(n, k - 1, res, cur, i + 1);
            cur.remove(cur.size() - 1);
        }
    }
}