"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda interval:interval.start)
        p_start, p_end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            c_start, c_end = intervals[i].start, intervals[i].end
            if c_start < p_end:
                return False
            p_start = c_start
            p_end = c_end
        return True