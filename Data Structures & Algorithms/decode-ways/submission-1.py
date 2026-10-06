class Solution:
    def numDecodings(self, s: str) -> int:
        # recursive memoization
        # time: O(n), space: O(n)
        memo = { len(s) : 1 }
        def dfs(i):
            if i in memo:
                return memo[i]

            if s[i] == "0":
                return 0

            ways = dfs(i + 1)

            if 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)