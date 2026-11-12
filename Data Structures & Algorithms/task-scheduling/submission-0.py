class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1
            while cooldown and cooldown[0][0] <= time:
                    available_time, remaining = cooldown.popleft()
                    heapq.heappush(heap, -remaining)
            if heap:
                remaining = -heapq.heappop(heap)
                remaining -= 1

                if remaining > 0:
                    cooldown.append((time+n+1, remaining))
        return time