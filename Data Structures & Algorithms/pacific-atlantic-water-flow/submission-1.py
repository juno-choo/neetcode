class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()

        def dfs(row, col, visit, prev):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or heights[row][col] < prev or (row, col) in visit:
                return

            visit.add((row, col))

            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for r in range(ROWS):
            # pac
            dfs(r, 0, pac, 0)
            # atl
            dfs(r, COLS - 1, atl, 0)

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)  

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        
        return res

