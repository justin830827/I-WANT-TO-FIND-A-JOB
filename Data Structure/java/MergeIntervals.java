import java.util.*;

/**
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Example: Input: [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]]
 * 
 * Input: [[1,4],[4,5]] Output: [[1,5]]
 * 
 * Idea of solution: Sort the input list with the start time, (i.e. interval[0])
 * and merge the list if the current interval has overlap with previous
 * interval.
 * 
 * Time Complexity: O(nlog(n)), Space Complexity: O(n)
 */

public class MergeIntervals {
    /**
     * 
     * @param intervals: an array contains multiple intervals with start and end
     *                   time such as [1,3]
     * @return the intervals list/array without overlapping intervals.
     */
    public int[][] merge(int[][] intervals) {
        if (intervals.length < 2) {
            return intervals;
        }
        // Sort array by the start time.
        Arrays.sort(intervals, (a, b) -> (a[0] - b[0]));

        // Generate the results
        List<int[]> res = new ArrayList<>();
        for (int[] interval : intervals) {
            if (res.isEmpty() || res.get(res.size() - 1)[1] < interval[0]) {
                res.add(interval);
            } else {
                res.get(res.size() - 1)[1] = Math.max(res.get(res.size() - 1)[1], interval[1]);
            }
        }
        return res.toArray(new int[res.size()][]);
    }

    public static void main(String[] args) {
        int[][] input = { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };
        int[][] ans = new MergeIntervals().merge(input);
        System.out.println(Arrays.deepToString(ans));
    }
}