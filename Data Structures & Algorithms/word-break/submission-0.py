class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start = 0
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        word_set = set(wordDict)
        for end in range(1, n+1):
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break
        return dp[n]
        
