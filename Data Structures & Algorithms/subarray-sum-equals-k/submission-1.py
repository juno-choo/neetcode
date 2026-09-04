class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        freq = {0: 1}
        res = 0

        for num in nums:
            prefix += num

            # num of subarray sum k that ends here
            res += freq.get(prefix - k, 0)

            freq[prefix] = freq.get(prefix, 0) + 1

        return res