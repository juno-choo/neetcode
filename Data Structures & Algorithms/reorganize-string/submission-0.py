class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = defaultdict(int)
        res = []

        for c in s:
            freqMap[c] += 1

        # Create a max heap
        heap = [(-freq, c) for c, freq in freqMap.items()]
        heapq.heapify(heap)

        # Return "" early if not possible to construct a valid string
        if -heap[0][0] > (len(s) + 1) // 2: 
            return ""

        # This will be cooldown variable
        prev = (0, "")

        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)
    
            if prev[0] < 0:
                heapq.heappush(heap, prev)

            # Holding the char we just processed for the next iteration
            prev = (freq + 1, char)
            
        return ''.join(res)

