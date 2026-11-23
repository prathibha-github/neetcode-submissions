"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        if n == 1:
            return 1
        intervals = sorted(intervals, key=lambda interval:interval.start)
        heap = []
        for i in range(n):
            meeting_start, meeting_end = intervals[i].start, intervals[i].end
            if heap and heap[0] <= meeting_start:
                heapq.heappop(heap)
            heapq.heappush(heap, meeting_end) 
        return len(heap)