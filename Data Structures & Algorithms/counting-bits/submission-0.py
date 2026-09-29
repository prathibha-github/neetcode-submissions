class Solution:
    def count(self, number: int) -> int:
        total = 0
        while number > 0:
            total += 1
            number &= (number - 1)
        return total
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.count(i))
        return result