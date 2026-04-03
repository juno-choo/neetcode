class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row:
                    return False
                row.add(board[r][c])

        for c in range(9):
            col = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in col:
                    return False
                col.add(board[r][c])

        box = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                idx = (r // 3) * 3 + c // 3
                if board[r][c] == '.':
                    continue
                if board[r][c] in box[idx]:
                    return False
                box[idx].add(board[r][c])

        return True