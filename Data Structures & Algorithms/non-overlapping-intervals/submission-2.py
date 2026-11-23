class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        intervals = sorted(intervals, key=lambda interval: interval[1])
        print(intervals)
        previous_start, previous_end = intervals[0]
        count = 0
        for i in range(1, n):
            current_start, current_end = intervals[i]
            if previous_end <= current_start:
                previous_start = current_start
                previous_end = current_end
                continue
            elif current_start < previous_end:
                count += 1
        return count