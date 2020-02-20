class Solution:
    """
    Args:
        intervals: an array of meeting time intervals consisting of start
        and end times [[s1,e1],[s2,e2],...] (si < ei).

    Returns:
        return the minimum number of conference rooms required.

    Example:
        Input: [[0,30],[5,10],[15,20]]
        Output: 2

        Input: [[7,10],[2,4]]
        Output: 1
    
    Idea of solution: 
        One trick here is we only need to sort the start time and end time of intervals 
        since we only need another meeting room when the start time is earlier than end time.
    
    Time complexity: O(nlog(n))
    Space complexity: O(n)
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        end_index, res = 0, 0
        for i in range(len(start)):
            if start[i] < end[end_index]:
                res += 1
            else:
                end_index += 1
        return res