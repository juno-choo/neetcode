class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True

            # handle ambiguous case
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue

            # left half sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right half sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False

        # target = 0
        # [1, 0, 1, 1, 1]
        #        m
        #              r
        #  l
       

