class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Intuition: In our recursive fn loop, start from start + 1, this ensures we will not get repeat values and we will get the full combo
        res = []

        def dfs(start, cur):
            if len(cur) >= k:
                res.append(cur.copy())
                return

            for i in range(start, n + 1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()

        dfs(1, [])
        return res
