class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(self, s: str) -> boolean:
            if not s or len(s) == 1:
                return True
            start = 0
            end = len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        def expand(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return (left+1, right-1)
        n = len(s)
        longest = (0, 0)
        for i in range(n):
            candidate1 = expand(i, i)
            candidate2 = expand(i, i+1)
            len_candidate1 = (candidate1[1]-candidate1[0])
            len_candidate2 = (candidate2[1]-candidate2[0])
            len_longest = longest[1]-longest[0]
            if len_candidate1 > len_longest:
                longest = candidate1
            if len_candidate2 > len_longest:
                longest = candidate2
        return s[longest[0]:longest[1]+1]


        

