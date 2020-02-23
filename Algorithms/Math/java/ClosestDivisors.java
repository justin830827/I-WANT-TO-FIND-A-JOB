import java.util.Arrays;

/**
 * Given an integer num, find the closest two integers in absolute difference
 * whose product equals num + 1 or num + 2.
 * 
 * Return the two integers in any order
 * 
 * Idea of solution: Iterate a from sqrt(x+2) to 1, and check: if (x + 1) % a ==
 * 0, we directly return the pair [a, (x + 1) / a]. if (x + 2) % a == 0, we
 * directly return the pair [a, (x + 2) / a]. The first valid pair we meet will
 * have be the closet pair.
 * 
 * Time complexity: O(sqrt(n)), Space complexity: O(1)
 */
public class ClosestDivisors {
    /**
     * 
     * @param num: Given an integer num. 0 < num < 10^7.
     * @return the two integers which are the divisors of num in any order with
     *         minimum difference
     */
    public int[] closestDivisors(int num) {
        int[] res = new int[2];
        for (int i = (int) Math.sqrt(num + 2); i > 0; i--) {
            res[0] = i;
            if ((num + 1) % i == 0) {
                res[1] = (num + 1) / i;
                break;
            }
            if ((num + 2) % i == 0) {
                res[1] = (num + 2) / i;
                break;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int num = 8;
        int[] res = new ClosestDivisors().closestDivisors(num);
        System.out.println(Arrays.toString(res));
    }
}