class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in seen:
            if n - 1 not in seen:
                curr = 1
                while n + curr in seen:
                    curr += 1
                res = max(res, curr)
        return res


