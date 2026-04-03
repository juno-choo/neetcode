class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      
        def dfs(r, c, i, seen):
            if i >= len(word):
                return True
          
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r,c) in seen or board[r][c] != word[i]:
                return False
            
            seen.add((r,c))
            if dfs(r-1,c,i+1, seen) or dfs(r, c-1, i+1, seen) or dfs(r+1, c, i+1, seen) or dfs(r, c+1, i+1, seen):
                return True

            seen.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c, 0, set()):
                    return True

        return False