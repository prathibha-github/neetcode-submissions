class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        result = 0
        half = self.myPow(x, abs(n) // 2)
        if n % 2 == 0:
            result = half * half
        else:
            result = x * half * half
        if n < 0:
            return 1/result
        else:
            return result