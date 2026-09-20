class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        start = 0
        end = start + 1
        seen = dict()
        seen[s[start]] = start
        n = len(s)
        maxlen = 0
        while end < n:
            if s[end] in seen:
                until = seen[s[end]]
                while start < until+1:
                    if s[start] in seen:
                        seen.pop(s[start])
                    start += 1
            seen[s[end]] = end
            end += 1
            maxlen = max(maxlen, end - start)
            
        return maxlen