from typing import List
class Solution:
    def add2Rows(self, row1: List[int], row2: List[int]) -> List[int]:
        if not row1 and not row2:
            return []
        if not row1:
            return row2
        if not row2:
            return row1
        i = 0
        j = 0
        result = []
        carry = 0
        while i < len(row1) and j < len(row2):
            total = row1[i] + row2[j] + carry
            digit = total % 10
            carry = total // 10
            result.append(digit)
            i += 1
            j += 1
        while i < len(row1):
            total = row1[i] + carry
            digit = total % 10
            carry = total // 10
            result.append(digit)
            i += 1
        while j < len(row2):
            total = row2[j] + carry
            digit = total % 10
            carry = total // 10
            result.append(digit)
            j += 1
        if carry:
            result.append(carry)
        return result



    def addRows(self, rows: List[List[int]]) -> List[int]:
        if not rows:
            return []
        row1 = rows[0]
        for i in range(1, len(rows)):
            row2 = rows[i]
            row1 = self.add2Rows(row1, row2)
        return row1

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        digits1 = list(reversed(num1))
        digits2 = list(reversed(num2))
        rows = []
        i = 0
        for i, ch2 in enumerate(digits2):
            carry = 0
            row = [0] * i
            for ch1 in digits1:
                mul = int(ch1) * int(ch2) + carry
                digit = mul % (10)
                carry = mul // (10)
                row.append((digit))
            while carry:
                row.append((carry % 10))
                carry = carry // 10
            i += 1
            rows.append(row)
        result = reversed(self.addRows(rows))
        return "".join([str(num) for num in result])
        