class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        result = []
        end = len(digits) - 1
        carry = 1
        while end >= 0:
            if digits[end] + carry > 9:
                result.insert(0, 0)
                carry = 1
            else:
                result.insert(0, digits[end]+carry)
                carry = 0
            end -= 1
        if carry == 1:
            result.insert(0, 1)
        return result