class Solution:
    def helper(self, nums):
        house0 = 0
        house1 = 0

        for num in nums:
            curr = max(num+house0, house1)
            house0 = house1
            house1 = curr

        return curr

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))