from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        current_row = [1]
        for row in range(1, rowIndex+1):
            next_row = [1] * (row + 1)
            for col in range(1, row):
                next_row[col] = current_row[col-1] + current_row[col]
            current_row = next_row
        return current_row