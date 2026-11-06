class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, reachable):
            if (row, col) in reachable:
                return
            reachable.add((row, col))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for row_delta, col_delta in directions:
                next_row = row + row_delta
                next_col = col + col_delta

                if not (0 <= next_row < rows and 0 <= next_col<cols) or not heights[next_row][next_col] >= heights[row][col]:
                    continue

                dfs(next_row, next_col, reachable)
        
        # cells touching the pacific
        for col in range(cols):
            dfs(0, col, pacific)

        for row in range(rows):
            dfs(row, 0, pacific)

        # cells touching the atlantic
        for col in range(cols):
            dfs(rows-1, col, atlantic)

        for row in range(rows):
            dfs(row, cols-1, atlantic)

        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append((row, col))
        return result