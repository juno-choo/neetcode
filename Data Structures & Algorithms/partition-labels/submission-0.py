class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_seen = { c: i for i, c in enumerate(s) }

        res = []
        l, r = 0, 0
        end = 0

        for r in range(len(s)):
            end = max(end, last_seen[s[r]])

            if r == end:
                res.append(r - l + 1)
                l = r + 1

        return res