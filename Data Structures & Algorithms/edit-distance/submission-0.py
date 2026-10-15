class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1

        return dp[-1][-1]

        """
             ""  a. b. c
        ""   0   1  2. 3
        a    1   0  1  2
        b.   2   1. 0. 1
        """