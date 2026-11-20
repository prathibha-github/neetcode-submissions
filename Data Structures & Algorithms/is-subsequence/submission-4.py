class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        count = 0
        i = 0
        j = 0
        while i < n:
            while j < m:
                if t[j] == s[i]:
                    print(t[j], " ", s[i])
                    count += 1
                    j += 1
                    break
                else:
                    j += 1
            i += 1
        return count >= n