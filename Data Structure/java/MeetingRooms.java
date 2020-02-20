import java.util.Arrays;

/**
 * Given an array of meeting time intervals consisting of start and end times
 * [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
 * meetings.
 * 
 * Time complexity: O(nlog(n)), Space complexity: O(1)
 */
public class MeetingRooms {
    /**
     * @param intervals: an array of meeting time intervals consisting of start and
     *                   end times [[s1,e1],[s2,e2],...] (si < ei).
     * @return true if a person could attend all meeting. Otherwise, false.
     */
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> (a[0] - b[0]));
        int preEnd = -1;
        for (int[] interval : intervals) {
            if (interval[0] < preEnd) {
                return false;
            }
            preEnd = interval[1];
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] intervals = { { 0, 30 }, { 5, 10 }, { 15, 20 } };
        boolean test = new MeetingRooms().canAttendMeetings(intervals);
        System.out.println(test);
    }
}