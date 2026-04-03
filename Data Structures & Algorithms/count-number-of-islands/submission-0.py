class Solution:

    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        # List of adjacent nodes
        adj = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in adj:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == "1":
                self.dfs(grid, row, col)
           

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    islands += 1

        return islands