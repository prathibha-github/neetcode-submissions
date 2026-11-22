class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets:
            return False
        n = len(triplets)
        merged = None
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if merged is None:
                merged = [a, b, c]
            else:
                merged = [max(a, merged[0]), max(b, merged[1]), max(c, merged[2])]
            if merged == target:
                return True
        return False
