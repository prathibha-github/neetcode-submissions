class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        fresh = 0
        queue = deque()

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        while queue and fresh > 0:
            current_level_size = len(queue)
            for _ in range(current_level_size):
                (row, col) = queue.popleft()
                for row_change, col_change in directions:
                    next_row = row + row_change
                    next_col = col + col_change

                    if not (0 <= next_row < nrows and 0 <= next_col < ncols) or not grid[next_row][next_col] == 1:
                        continue

                    grid[next_row][next_col] = 2
                    fresh -= 1
                    queue.append((next_row, next_col))
            minutes += 1
        if fresh > 0:
            return -1
        return minutes
