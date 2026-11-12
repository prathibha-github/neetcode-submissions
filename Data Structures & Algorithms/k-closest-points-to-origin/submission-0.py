import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = math.sqrt(x**2+y**2)
            heapq.heappush(heap, (distance, point))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result