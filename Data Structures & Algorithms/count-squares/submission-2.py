class CountSquares:

    def __init__(self):
        self.counts = Counter()

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ways = 0
        x1, y1 = point
        for (x2, y2), copies in self.counts.items():
            if y1 != y2 or x1 == x2:
                continue
            side = abs(x2 - x1)
            ways += copies * self.counts[(x2, y2 + side)] * self.counts[(x1, y1 + side)] 
            ways += copies * self.counts[(x2, y2 - side)] * self.counts[(x1, y1 - side)]
        return ways
