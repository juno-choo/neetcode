class Solution:
    def climbStairs(self, n: int) -> int:
        # constant space
        # one, two = 1, 1

        # for i in range(2, n + 1):
        #     temp = one + two
        #     one = two
        #     two = temp

        # return two

        # linear space, iterative
        # dp = [1] * (n + 1)
        # for i in range(2, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[-1]

        # recurisve
        dp = [0] * (n + 1)
        def dfs(i):
            if dp[i] != 0:
                return dp[i]

            if i == 0 or i == 1:
                return 1

            dp[i] = dfs(i-1) + dfs(i-2)
            return dp[i]

        return dfs(n)
            
            
