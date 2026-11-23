class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_positive = 0x7FFFFFFF
        while b != 0:
            xor = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = xor
            b = carry
        if a <= max_positive:
            return a
        return ~(a ^ mask)