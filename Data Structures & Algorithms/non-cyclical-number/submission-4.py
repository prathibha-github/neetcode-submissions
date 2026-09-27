class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def extractDigits(n):
            result = []
            while n > 0:
                digit = n % 10
                result.append(digit)
                n = n // 10
            return result
        
        def squareSummation(digits):
            summation = 0
            for digit in digits:
                summation += digit * digit
            return summation
        
        while n != 1 and n not in seen:
            seen.add(n)
            digits = extractDigits(n)
            n = squareSummation(digits)
        return n == 1
