class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        start = 0
        end = len(heights) - 1
        maxArea = -1
        while start < end:
            area = (end - start) * min(heights[start], heights[end])
            maxArea = max(area, maxArea)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return maxArea