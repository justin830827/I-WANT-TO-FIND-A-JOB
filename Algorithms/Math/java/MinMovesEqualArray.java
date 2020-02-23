/**
 * Given a non-empty integer array of size n, find the minimum number of moves
 * required to make all array elements equal, where a move is incrementing n - 1
 * elements by 1.
 * 
 * Idea of solution: Adding 1 to n - 1 elements is the same as subtracting 1
 * from one element, w.r.t goal of making the elements in the array equal. So,
 * best way to do this is make all the elements in the array equal to the min
 * element. sum(array) - n * minimum
 * 
 * Time Complexity: O(n), Space Complexity: O(1)
 */
public class MinMovesEqualArray {
    /**
     * 
     * @param nums: Given a non-empty integer array of size n.
     * @return the minimum number of moves required to make all array elements
     *         equal.
     */
    public int minMoves(int[] nums) {
        int sum = 0, min = Integer.MAX_VALUE;
        for (int num : nums) {
            min = Math.min(min, num);
            sum += num;
        }
        return sum - nums.length * min;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3 };
        int res = new MinMovesEqualArray().minMoves(nums);
        System.out.println(res);
    }
}