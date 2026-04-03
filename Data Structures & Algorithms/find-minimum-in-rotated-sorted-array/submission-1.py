class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m 
            elif nums[l] < nums[m]:
                l = m 
            else:
                return nums[r]
                # [4,5,0,1,2,3]
                #      l r
                #      m

