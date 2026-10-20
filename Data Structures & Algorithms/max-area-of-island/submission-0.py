class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= nrows or col < 0 or col >= ncols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col -1)
        
        max_area = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area