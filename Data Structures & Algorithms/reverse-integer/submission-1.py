class Solution:
    def reverse(self, x: int) -> int:
        if x == -2147483648:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = sign * x
        reversed_number = 0
        while x != 0:
            digit = x % 10
            x = x // 10
            if reversed_number > 214748364:
                return 0
            if reversed_number == 214748364 and digit > 7:
                return 0
            reversed_number = reversed_number * 10
            reversed_number += digit
        
        return sign*reversed_number