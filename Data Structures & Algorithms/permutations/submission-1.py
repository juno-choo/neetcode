class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, cur = [], []
        n = len(nums)
        seen = set()

        def dfs():
            if len(cur) == n:
                res.append(cur.copy())
                return

            for x in nums:
                if x not in seen:
                    cur.append(x)
                    seen.add(x)
                    dfs()
                    cur.pop()
                    seen.remove(x)

        dfs()
        return res
            