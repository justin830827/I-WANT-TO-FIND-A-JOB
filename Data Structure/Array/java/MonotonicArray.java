/**
 * Check the array if in asc order. If not, reverse the array to check.
 *
 * Example: Input:[1,2,2,3] Output: true
 * 
 * Input: [6,5,4,4] Output: true
 * 
 * Input:[1,3,2] Output: false
 * 
 */
public class MonotonicArray {
  /**
   * Check the input array whether it is monotonic. Idea of solution: First check
   * the first and last element in which possible order, then compare if the array
   * is asc. In other words, we only need to consider the array if asc order.
   * 
   * @param arr: a given array, which may contain duplicate and unsorted order.
   * @return boolean: to indicate whether the array is monotonic.
   * 
   *         Time Complexity: O(n), Space Complexity: O(1)
   */
  public boolean isMonotonic(int[] arr) {
    if (arr[arr.length - 1] < arr[0])
      reverse(arr);

    for (int i = 1; i < arr.length; i++) {
      if (arr[i] < arr[i - 1])
        return false;
    }

    return true;
  }

  /**
   * Reverse an array. Only call this function if the the last element is smaller
   * than the first element of array.
   * 
   * @param arr: An array, which is the same as the input arr.
   */
  private void reverse(int[] arr) {
    for (int i = 0; i < arr.length / 2; i++) {
      int temp = arr[i];
      arr[i] = arr[arr.length - 1 - i];
      arr[arr.length - 1 - i] = temp;
    }
  }

  public static void main(String args[]) {
    int[] input = { 1, 2, 3, 4 };
    boolean res = new MonotonicArray().isMonotonic(input);
    System.out.println(res);
  }
}
