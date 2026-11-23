class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if not intervals:
            return result
        intervals = sorted(intervals)
        n = len(intervals)
        merged_start, merged_end = intervals[0]
        for i in range(1, n):
            current_start, current_end = intervals[i]
            if current_start <= merged_end:
                merged_end = max(merged_end, current_end)
            else: #disconnected intervals
                result.append([merged_start, merged_end])
                merged_start = current_start
                merged_end = current_end
        result.append([merged_start, merged_end])
        return result


