class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in seen:
                return [seen[compl], i]

            seen[nums[i]] = i