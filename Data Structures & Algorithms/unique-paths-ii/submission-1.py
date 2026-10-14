class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        if obstacleGrid[0][0] == 1: return 0

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    continue

                if c > 0:
                    dp[r][c] += dp[r][c-1]

                if r > 0:
                    dp[r][c] += dp[r-1][c]



        return dp[-1][-1]