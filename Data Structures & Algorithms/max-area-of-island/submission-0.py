class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        area = 1
        adj = [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]
        for row, col in adj:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                area += self.dfs(grid, row, col)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        maxArea = max(maxArea, self.dfs(grid, r, c))
                        
        return maxArea