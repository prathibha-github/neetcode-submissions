from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for row in range(rowIndex+1):
            current = [1] * (row + 1)
            for col in range(1, row):
                current[col] = triangle[row-1][col-1] + triangle[row-1][col]
            triangle.append(current)
        return triangle[rowIndex]