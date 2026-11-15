class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.tmap[key]
        start = 0
        end = len(values) - 1
        answer = ""
        while start <= end:
            mid = (start + end) // 2
            if values[mid][0] <= timestamp:
                answer = values[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return answer
        
