/**
 * Check a matrix is Toeplitz if every diagonal from top-left to bottom-right
 * has the same element.
 *
 * Example: Input:[[1,2,3,4],[5,1,2,3],[9,5,1,2]] Output: true
 * 
 * Input: [[1,2],[2,2]] Output: false
 * 
 */
public class ToeplitzMatrix {
  /**
   * The main method to identify if the matrix is Toeplitz.
   * 
   * @param matrix: an given m x n matrix.
   * @return: True if and only if the matrix is Toeplitz.
   * 
   *          Time Complexity: O(n^2), Space Complexity: O(1)
   */
  public boolean isToeplitzMatrix(int[][] matrix) {
    if (matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }

    for (int i = 1; i < matrix.length; i++) {
      if (!isEqual(matrix[i - 1], matrix[i])) {
        return false;
      }
    }
    return true;
  }

  /**
   * Check the two array if they are diagonally equal. Example: Input: arr1 =
   * [1,2,3,4,5], arr2 = [0,1,2,3,4], Output: true.
   * 
   * @param arr1: the previous row
   * @param arr2: the current row
   * @return true if these two array are diagonally equal. Otherwise, return
   *         false.
   */
  private boolean isEqual(int[] arr1, int[] arr2) {
    for (int i = 0; i < arr1.length - 1; i++) {
      if (arr1[i] != arr2[i + 1]) {
        return false;
      }
    }
    return true;
  }
}