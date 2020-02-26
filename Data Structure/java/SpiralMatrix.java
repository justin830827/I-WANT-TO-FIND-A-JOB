import java.util.*;

/**
 * Given a matrix of m x n elements (m rows, n columns), return all elements of
 * the matrix in spiral order.
 * 
 * For example:
 * 
 * Input: [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] Output: [1,2,3,6,9,8,7,4,5]
 * 
 * Time Complexity: O(m+n), Space Complexity: O(1)
 */

public class SpiralMatrix {
    /**
     * @param matrix a m x n integer matrix.
     * @return a list with spiral order of matrix.
     */
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<Integer>();
        if (matrix.length == 0)
            return res;
        int rs = 0, re = matrix.length - 1, cs = 0, ce = matrix[0].length - 1;
        while (rs <= re && cs <= ce) {
            // left to right
            for (int i = cs; i <= ce; i++) {
                res.add(matrix[rs][i]);
            }
            rs++;
            // top to bottom
            for (int i = rs; i <= re; i++) {
                res.add(matrix[i][ce]);
            }
            ce--;
            if (rs <= re) {
                // right to left
                for (int i = ce; i >= cs; i--) {
                    res.add(matrix[re][i]);
                }
                re--;
            }
            if (cs <= ce) {
                // bottom to top
                for (int i = re; i >= rs; i--) {
                    res.add(matrix[i][cs]);
                }
                cs++;
            }
        }
        return res;
    }
}