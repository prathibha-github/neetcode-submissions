class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrows = len(grid)
        ncols = len(grid[0])
        queue = deque()

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 0: # the treasure chest
                    queue.append((i, j))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            (row, col) = queue.popleft()

            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change

                if not (0 <= next_row < nrows and 0 <= next_col < ncols) or not grid[next_row][next_col] == 2147483647:
                    continue

                grid[next_row][next_col] = grid[row][col] + 1
                queue.append((next_row, next_col))
