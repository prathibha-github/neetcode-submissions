class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n-1
        while start < end:
            start_char = s[start].lower()
            end_char = s[end].lower()
            print(start_char+" "+end_char)
            if not start_char.isalnum():
                start += 1
                continue
            elif not end_char.isalnum():
                end -= 1
                continue
            if start_char != end_char:
                return False
            start += 1
            end -= 1
        return True