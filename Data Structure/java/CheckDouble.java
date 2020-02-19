import java.util.HashSet;

/**
 * Check if there exists two integers N and M such that N is the double of M (
 * i.e. N = 2 * M).
 * 
 * Example: Input: [10,2,5,3] Output: true
 * 
 * Input: [7,1,14,11] Output: true
 * 
 * Input:[3,1,7,11] Output: false
 * 
 * Idea of solution: The tricky part of this problem is to also check both 2 *
 * arr[i] and arr[i] / 2 if in the array. To make the search efficiently, we can
 * use Hash Set to save the previous value, and check if the incoming element
 * meet the requirements.
 * 
 * Time Complexity: O(n) Space Complexity: O(n)
 */
public class CheckDouble {
  /**
   * @param arr: Given an array of integers.
   * @return: return true if there exists two indices i and j such that : 1. i !=
   *          j 2. 0 <= i, j < arr.length 3. arr[i] == 2 * arr[j]
   */
  public boolean checkIfExist(int[] arr) {
    HashSet<Integer> table = new HashSet<Integer>();
    for (int i = 0; i < arr.length; i++) {
      if ((table.contains(2 * arr[i])) || (arr[i] % 2 == 0 && table.contains(arr[i] / 2))) {
        return true;
      }
      table.add(arr[i]);
    }
    return false;
  }

  public static void main(String args[]) {
    int[] input1 = { 10, 2, 5, 3 };
    boolean res1 = new CheckDouble().checkIfExist(input1);
    System.out.println(res1);

    int[] input2 = { 7, 1, 14, 11 };
    boolean res2 = new CheckDouble().checkIfExist(input2);
    System.out.println(res2);

    int[] input3 = { 3, 1, 7, 11 };
    boolean res3 = new CheckDouble().checkIfExist(input3);
    System.out.println(res3);
  }
}