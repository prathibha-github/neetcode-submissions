from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        def iways(n):
            a = 1
            b = 1
            count = 2
            total = 1
            while count <= n:
                total = a + b
                a = b
                b = total
                count += 1
            return total
        ''' top down dynamic programming
        @lru_cache(None)
        def ways(n):
            if n <= 1:
                return 1
            if n == 2:
                return 2 # 1 + 1, 2
            return ways(n-1) + ways(n-2) '''
        return iways(n)