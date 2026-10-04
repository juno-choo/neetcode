class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        total = sum(matchsticks)
        if total % 4 != 0: return False
        target = total // 4

        def dfs(i):
            if i == len(matchsticks):
                return True

            for side in range(4):
                if sides[side] + matchsticks[i] <= target:
                    sides[side] += matchsticks[i]

                    if dfs(i + 1):
                        return True

                    sides[side] -= matchsticks[i]

                    if sides[side] == 0:
                        return False

            return False

        return dfs(0)