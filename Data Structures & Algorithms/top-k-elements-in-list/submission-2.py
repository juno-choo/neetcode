class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        map = {}
        
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1 
            else: 
                map[nums[i]] += 1 

        #--------------BRUTE FORCE----------------
        # Time complexity: O(n * k)
        # res = []

        # for j in range(k):
        #     max_key = max(map, key=map.get)
        #     res.append(max_key)
        #     map.pop(max_key)

        # return res

        #-----------------HEAP-------------------
        # Time complexity: O(n log k)
        # heap = []

        # for key, value in map.items():
        #     if len(heap) < k or value > heap[0][0]:
        #         heapq.heappush(heap, [value, key])
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = []

        # for i in heap:
        #     res.append(i[1])

        # return res

        #------------BUCKET SORT------------------
        # Time complexity: O(n)
        freq = [[] for i in range(len(nums) + 1)]
        for key, value in map.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

