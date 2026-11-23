class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        intervals = sorted(intervals, key=lambda interval: interval[1])
        _, previous_end = intervals[0]
        removed = 0
        for i in range(1, n):
            current_start, current_end = intervals[i]
            if previous_end <= current_start:
                previous_end = current_end
            elif current_start < previous_end:
                removed += 1
        return removed