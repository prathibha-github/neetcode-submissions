class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = dict()
        maxlen = 0
        for end, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = end
            maxlen = max(maxlen, end - start + 1)
            
        return maxlen