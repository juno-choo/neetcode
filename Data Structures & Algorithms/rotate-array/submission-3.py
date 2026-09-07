class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n

        # reverse partitions from 0 -> k-1
        reverse(0, n - k - 1)

        # reverse partitions from k -> len(nums)-1
        reverse(n - k, n - 1)


        # reverse entire list
        reverse(0, n - 1)
        