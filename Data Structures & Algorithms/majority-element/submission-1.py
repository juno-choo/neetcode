class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tally = 0
        cur = nums[0]

        for num in nums:
            if num == cur:
                tally += 1
                if tally == 1:
                    cur = num
            else:
                if tally > 0:
                    tally -= 1
                if tally == 0:
                    cur = num

        return cur