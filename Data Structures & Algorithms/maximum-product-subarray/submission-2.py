class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            temp = n*curMax
            curMax = max(n, n*curMax, n*curMin)
            curMin = min(n, temp, n*curMin)

            res = max(res, curMax)

        return res