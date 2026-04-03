class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n-2):
            l = i + 1
            r = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:               
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                
        return res

        # [-4,-1,-1,0,1,2]
        #      i. l.    r
                