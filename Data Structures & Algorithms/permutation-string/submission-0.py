class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        start = 0

        for end in range(len(s2)):
            window[s2[end]] += 1
            if end - start + 1 > len(s1):
                window[s2[start]] -= 1
                start += 1
            if need == window:
                return True
        return False