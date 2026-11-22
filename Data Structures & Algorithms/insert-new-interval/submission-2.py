class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        target_start, target_end = newInterval
        i = 0
        while i < n and intervals[i][1] < target_start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= target_end:
            start, end = intervals[i]
            target_start = min(start, target_start)
            target_end = max(end, target_end)
            i += 1
            
        result.append([target_start, target_end])

        while i < n:
            result.append(intervals[i])
            i += 1
        return result
                
        