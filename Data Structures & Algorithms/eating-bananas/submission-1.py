class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start < end:
            k = (start + end) // 2
            #print("start = ", start, "end = ", end, "k = ", k)
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            #print("hours = ", hours)
            if hours <= h:
                end = k
            else:
                start = k + 1
        return start