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
            #print("considering ", s[end])
            if s[end] not in seen:
                seen[s[end]] = end
                end += 1
                maxlen = max(maxlen, end - start)
                #print(s[start:end]," ", seen, " ", maxlen)
            else:
                until = seen[s[end]]
                #print(start, " ", until, " ", end)
                while start < until+1:
                    if s[start] in seen:
                        seen.pop(s[start])
                    start += 1
                seen[s[end]] = end
                end += 1
                #print("end=", end)
                maxlen = max(maxlen, end - start)
                #print(s[start:end]," ", seen, " ", maxlen)
            
        return maxlen