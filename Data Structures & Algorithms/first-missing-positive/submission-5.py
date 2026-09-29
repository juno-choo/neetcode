class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n = max(nums)

        # lookup = set(nums)
        
        # for i in range(1, n + 1):
        #     if i not in lookup:
        #         return i

        # return n + 1 if n >= 0 else 1
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1