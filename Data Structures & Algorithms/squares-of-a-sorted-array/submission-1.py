class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        res = []

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] > nums[r]:
                res.append(nums[l])
                l += 1
            else:
                res.append(nums[r])
                r -= 1

        return res[::-1]
