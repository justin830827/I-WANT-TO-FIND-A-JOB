import java.util.Arrays;

/**
 * Given an array of meeting time intervals consisting of start and end times
 * [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
 * required.
 * 
 * Idea of solution: One trick here is we only need to sort the start time and
 * end time of intervals since we only need another meeting room when the start
 * time is earlier than end time.
 * 
 * Time Complexity: O(nlogn), Space Complexity: O(n)
 */
public class MeetingRoomsII {
    /**
     * 
     * @param intervals: Given an array of meeting time intervals consisting of
     *                   start and end times [[s1,e1],[s2,e2],...] (si < ei)
     * @return the minimum number of conference rooms required.
     */
    public int minMeetingRooms(int[][] intervals) {
        int[] start = new int[intervals.length];
        int[] end = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        Arrays.sort(start);
        Arrays.sort(end);
        int res = 0;
        int endIndex = 0;
        for (int i = 0; i < start.length; i++) {
            if (start[i] < end[endIndex]) {
                res += 1;
            } else {
                endIndex += 1;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[][] intervals = { { 0, 30 }, { 5, 10 }, { 15, 20 } };
        int ans = new MeetingRoomsII().minMeetingRooms(intervals);
        System.out.println(ans);
    }
}