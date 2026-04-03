class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            m = ( l + r ) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
        
        #     [4,5,6,7,0,1,2]
        #              l m 
        #              r 

        # l = 4
        # r = 6
        # m = 5
        # res = 1


        # if num[m] >= num[l]:
        #   search right
        # else:
        #   search left