class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0: return False

        target = total // 2

        dp = set([0])
        for x in nums:
            new_dp = set()
            for y in dp:
                new_dp.add(y)
                new_dp.add(x + y)

            dp = new_dp

        return target in dp