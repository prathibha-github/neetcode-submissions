class Solution:
    def isHappy(self, n: int) -> bool:
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
        
        digits = extractDigits(n)
        total = squareSummation(digits)
        print(digits, total)
        while total > 9:
            digits = extractDigits(total)
            total = squareSummation(digits)
        return total == 1
