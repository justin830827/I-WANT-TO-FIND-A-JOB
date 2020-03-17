/**
 * There are a row of n houses, each house can be painted with one of the k
 * colors. The cost of painting each house with a certain color is different.
 * You have to paint all the houses such that no two adjacent houses have the
 * same color.
 * 
 * The cost of painting each house with a certain color is represented by a n x
 * k cost matrix. For example, costs[0][0] is the cost of painting house 0 with
 * color 0; costs[1][2] is the cost of painting house 1 with color 2, and so
 * on... Find the minimum cost to paint all houses.
 */
public class PaintHouseII {
    /**
     * @param costs: integer n x 3 matrix without negative integers.
     * @return the minimum cost for painting house.
     */
    public int minCostII(int[][] costs) {
        if (costs.length == 0)
            return 0;
        int n = costs.length, k = costs[0].length;
        if (n == 0)
            return 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < k; j++) {
                costs[i][j] += getMin(costs[i - 1], j);
            }
        }
        return getMin(costs[n - 1], -1);

    }

    /**
     * @param arr: the current row of houses.
     * @param j:   index to indicate the current index
     */
    private int getMin(int[] arr, int j) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if (i == j)
                continue;
            res = Math.min(res, arr[i]);
        }
        return res;
    }
}