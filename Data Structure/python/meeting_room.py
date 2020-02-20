class Solution:
    """
    Args:
        intervals: an array of meeting time intervals consisting of start
        and end times [[s1,e1],[s2,e2],...] (si < ei).

    Returns:
        return true if a person could attend all meeting. Otherwise, false.

    Example:
        Input: [[0,30],[5,10],[15,20]]
        Output: false

        Input: [[7,10],[2,4]]
        Output: true
    
    Time complexity: O(nlog(n))
    Space complexity: O(1)
    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pre_end = -1
        for start, end in sorted(intervals, key=lambda x: x[0]):
            if start < pre_end:
                return False
            pre_end = end
        return True
