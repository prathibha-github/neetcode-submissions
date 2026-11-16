class Solution:
    def longestPalindrome(self, s: str) -> str:
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
            if (candidate1[1]-candidate1[0]) > (longest[1]-longest[0]):
                longest = candidate1
            len_longest = longest[1]-longest[0]
            if (candidate2[1]-candidate2[0]) > (longest[1]-longest[0]):
                longest = candidate2
        return s[longest[0]:longest[1]+1]


        

