class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for _ in range(len(nums))]

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
    
        for key, val in seen.items():
            freq[val - 1].append(key)

        res = []

        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k: 
                return res