class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = stop = end = 0

        for i in range(len(nums) - 1):
            end = max(end, i + nums[i])
            if i == stop:
                jumps += 1
                stop = end

        return jumps