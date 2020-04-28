/**
 * Given a 2D binary matrix filled with 0's and 1's, find the largest square
 * containing only 1's and return its area.
 * 
 * Example:
 * 
 * Input: [[1 0 1 0 0], [1 0 1 1 1], [1 1 1 1 1], [1 0 0 1 0]]
 * 
 * Output: 4
 * 
 * Idea of solution: Using dynamic programing the maximum edge on the current
 * cell. To achieve, We need to compare the cell on matrix[i-1][j-1],
 * matrix[i-1][j], matrix[i][j]. Find the minimum amoing the cells if the
 * current cell is equal to "1".
 */
public class MaximalSquare {
    /**
     * 
     * @param matrix: a 2D array with '1' and '0'
     * @return the largest area of square of '1'
     * 
     *         Time Complexity: O(mn), Sapce Complexity: O(mn)
     */
    public int maximalSquare(char[][] matrix) {
        int res = 0;
        if (matrix == null || matrix.length == 0)
            return res;
        int[][] dp = new int[matrix.length + 1][matrix[0].length + 1];
        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < dp[0].length; j++) {
                if (matrix[i - 1][j - 1] == '1') {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
                    res = Math.max(res, dp[i][j]);
                } else {
                    dp[i][j] = 0;
                }
            }
        }
        return res * res;
    }

}