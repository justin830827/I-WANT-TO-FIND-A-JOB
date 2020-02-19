from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Given a collection of intervals, merge all overlapping intervals.

        Args:
            intervals: an array contains multiple intervals with start and end time such as [1,3]

        Returns:
            return the intervals list/array without overlapping intervals.

        Example:
            Input: [[1,3],[2,6],[8,10],[15,18]]
            Output: [[1,6],[8,10],[15,18]]

            Input: [[1,4],[4,5]]
            Output: [[1,5]]

        Idea of solution:
            Sort the input list with the start time, (i.e. interval[0]) and merge the list
            if the current interval has overlap with previous interval.

        Time Complexity: O(nlog(n))
        Space Complexity: O(n) 
        """
        if len(intervals) < 2:
            return intervals
        # Sort the array by the start time.
        intervals.sort(key=lambda x: x[0])

        # Generate the results
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


if __name__ == "__main__":
    test = Solution()
    input = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(test.merge(input))
