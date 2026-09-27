class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = max(nums)

        lookup = set(nums)
        
        for i in range(1, n + 1):
            if i not in lookup:
                return i

        return n + 1 if n >= 0 else 1