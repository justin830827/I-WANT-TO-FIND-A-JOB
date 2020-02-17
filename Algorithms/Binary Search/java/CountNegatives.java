/**
 * Given a m * n matrix grid which is sorted in non-increasing order both
 * row-wise and column-wise. Return the number of negative numbers in grid.
 * 
 * Example:
 * 
 * Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] Output: 8
 * 
 * Input: grid = [[3,2],[1,0]] Output: 0
 * 
 * Input: grid = [[1,-1],[-1,-1]] Output: 3
 * 
 * Idea of solution: Use Binary search to find the leftmost index of negative
 * numbers in arr.
 * 
 * Time Complexity: O(nlog(n)) Space Complexity: O(n)
 */
public class CountNegatives {
    /**
     * 
     * @param grid: a m * n matrix grid which is sorted in non-increasing order both
     *              row-wise and column-wise
     * @return number of negative numbers in grid.
     */
    public int countNegatives(int[][] grid) {
        int res = 0;
        for (int[] row : grid) {
            int left = search(row);
            res += row.length - left;
        }
        return res;

    }

    /**
     * 
     * @param arr: a sorted arr
     * @return the leftmost index of negative numbers.
     */
    private int search(int[] arr) {
        int left = 0;
        int right = arr.length;

        while (left < right) {
            int pivot = left + (right - left) / 2;
            if (arr[pivot] < 0) {
                right = pivot;
            } else {
                left = pivot + 1;
            }
        }
        return left;
    }
}