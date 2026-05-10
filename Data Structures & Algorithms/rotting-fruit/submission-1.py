class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))

                elif grid[r][c] == 1:
                    fresh += 1

        dir = [(0,1), (0,-1), (1,0), (-1,0)]

        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()

                for r, c in dir:
                    newR, newC = row + r, col + c
                    if newR >= 0 and newC >= 0 and newR < ROWS and newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh -= 1
                
            res += 1

        return res if fresh == 0 else -1
            
