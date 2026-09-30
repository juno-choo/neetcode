class Solution:
    def climbStairs(self, n: int) -> int:
        # one, two = 1, 1

        # for i in range(2, n + 1):
        #     temp = one + two
        #     one = two
        #     two = temp

        # return two

        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]