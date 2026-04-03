class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                sq_idx = (row // 3) * 3 + col // 3
                
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in square[sq_idx]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[sq_idx].add(board[row][col])
        return True

"""
               0           1           2            col // 3
            0  1  2  |  3  4  5  |  6  7  8  
        ------------------------------------    
        0 |           |           |
        1 |     0     |     1     |     2           (row // 3) * 3 + col // 3
        2 |           |           |
        ------------------------------------
        3 |           |           |
        4 |     3     |     4     |     5           (row // 3) * 3 + col // 3
        5 |           |           |
        ------------------------------------
        6 |           |           |
        7 |     6     |     7     |     8           (row // 3) * 3 + col // 3
        8 |           |           |
"""