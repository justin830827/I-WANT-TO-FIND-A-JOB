class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        Args:
            date1: the first date in YYYY-MM-DD format.
            date2: the second date in YYYY-MM-DD format.

        Returns:
            return the difference of days between these two dates.

        Example:
            Input: date1 = "2019-06-29", date2 = "2019-06-30"
            Output: 1

            Input: date1 = "2020-01-15", date2 = "2019-12-31"
            Output: 15

        Idea of solution:
            Use the juilian day transformation to calculate the number of days on each input and count the difference.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        def get_days(date):
            y, m, d = map(int, date.split("-"))
            if m == 1 or m == 2:
                y -= 1
                m += 12
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5
        return abs(get_days(date2) - get_days(date1))