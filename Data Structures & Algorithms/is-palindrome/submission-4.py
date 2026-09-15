class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n-1
        while start < end:  
            while start < n and not s[start].isalnum():
                start += 1
            while end >= 0 and not s[end].isalnum():
                end -= 1
            print(str(start) +" " + str(end))
            if start >= n or end < 0:
                return True
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True