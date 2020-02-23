/**
 * This is a program to count the number of days between two dates. The two
 * dates are given as strings, their format is YYYY-MM-DD as shown in the
 * examples.
 * 
 * Idea of solution: use the juilian days transformation to calculate the number
 * of days on each input and count the difference.
 * 
 * Time Complexity: O(1), Space Complexity: O(1)
 */
public class NumberOfDays {
    /**
     * 
     * @param date1: the first date in YYYY-MM-DD format.
     * @param date2: the second date in YYYY-MM-DD format.
     * @return the difference of days between these two dates.
     */
    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(getDays(date1) - getDays(date2));
    }

    /**
     * 
     * @param date: the data in YYYY-MM-DD format.
     * @return the total days start from Julian day.
     */
    private int getDays(String date) {
        String[] splitDate = date.split("-");
        int y = Integer.valueOf(splitDate[0]), m = Integer.valueOf(splitDate[1]), d = Integer.valueOf(splitDate[2]);
        if (m == 1 || m == 2) {
            m += 12;
            y -= 1;
        }
        return 365 * y + y / 4 - y / 100 + y / 400 + d + (153 * m + 8) / 5;
    }

    public static void main(String[] args) {
        String date1 = "2019-06-29", date2 = "2019-06-30";
        int res = new NumberOfDays().daysBetweenDates(date1, date2);
        System.out.println(res);
    }
}