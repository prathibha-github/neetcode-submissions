class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0] * (n+1)
        ways[0] = 1
        for length in range(1, len(s)+1):
            last_digit = s[length-1]
            if last_digit != "0":
                ways[length] += ways[length-1]
            if length >= 2:
                last_two_digits = int(s[length-2:length])
                if 10 <= last_two_digits <= 26:
                    ways[length] += ways[length-2]
        return ways[n]
            