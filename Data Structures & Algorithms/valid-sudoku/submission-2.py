class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                idx = (c // 3) * 3 + r // 3

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in box[idx]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[idx].add(board[r][c])

        return True

                