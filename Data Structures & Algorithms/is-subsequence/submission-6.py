class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        count = 0
        i = 0
        j = 0
        while i < n and j < m:
            if t[j] == s[i]:
                i += 1
            j += 1
        return i >= n