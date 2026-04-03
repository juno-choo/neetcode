class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != word[i] or (r, c) in visit:
                return False

            visit.add((r, c))
            lst = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for row, col in lst:  
                if dfs(row, col, i + 1):
                    return True

            visit.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False