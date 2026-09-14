class Solution:
    def isValidBoard(self, board: List[List[str]], start_row, start_col, nrows, ncols):
        rset = set()
        cset = set()
        whole_set = set()
        i = start_row
        j = start_col
        nrow = i + nrows
        ncol = j + ncols
        while i < nrow:
            rset = set()
            j = start_col
            while j < ncol:
                if board[i][j] == ".":
                    j += 1
                    continue
                if board[i][j] in rset or board[i][j] in whole_set:
                    return False
                rset.add(board[i][j])
                whole_set.add(board[i][j])
                j += 1
            i += 1

        whole_set = set()
        rset = set()
        cset = set()
        j = start_col
        while j < ncol:
            cset = set()
            i = start_row
            while i < nrow:
                if board[i][j] == ".":
                    i += 1
                    continue
                if board[i][j] in cset or board[i][j] in whole_set:
                    return False
                cset.add(board[i][j])
                whole_set.add(board[i][j])
                i += 1
            j += 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        ####
        for i in range(rows):
            rset = set()
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rset:
                    return False
                rset.add(board[i][j])

        for j in range(cols):
            cset = set()
            for i in range(rows):
                if board[i][j] == ".":
                    continue
                if board[i][j] in cset:
                    return False
                cset.add(board[i][j])
        ####
        i = 0
        j = 0
        while i < rows:
            j = 0
            while j < cols:
                if not self.isValidBoard(board, i, j, 3, 3):
                    return False
                j += 3
            i += 3
        return True
