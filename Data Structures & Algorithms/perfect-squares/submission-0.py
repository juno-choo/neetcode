class Solution:
    def numSquares(self, n: int) -> int:
        # generate squares

        i = 1
        perfect_sqs = []
        perfect_sq = 1
        while perfect_sq <= n:
            perfect_sqs.append(perfect_sq)

            i += 1
            perfect_sq = i * i

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for x in perfect_sqs:
                if i >= x:
                    dp[i] = min(dp[i], 1 + dp[i - x])

        return dp[-1]


