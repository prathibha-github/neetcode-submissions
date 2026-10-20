from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= nrows or col < 0 or col >= ncols or grid[row][col] == "0":
                return 0
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        islands = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    islands += 1
                dfs(i, j)
        return islands