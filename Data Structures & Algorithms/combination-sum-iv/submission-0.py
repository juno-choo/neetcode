class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = { 0: 1 }

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            if remaining < 0:
                return 0

            ways = 0
            for num in nums:
                ways += dfs(remaining - num)

            memo[remaining] = ways
            return ways

        return dfs(target)