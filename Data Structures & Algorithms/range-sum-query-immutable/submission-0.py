class NumArray:

    def __init__(self, nums: List[int]):
        # Prefix sum of array nums
        self.prefixSum = []
        cur = 0
        for num in nums:
            cur += num
            self.prefixSum.append(cur)


    def sumRange(self, left: int, right: int) -> int:
        # Formula of sumRange: arr[r] - arr[l - 1]
        # Edge case 
        if left == 0:
            return self.prefixSum[right]

        return self.prefixSum[right] - self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)