class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = []
        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))

        while heap:
            count1, char1 = heapq.heappop(heap)

            if len(res) > 1 and res[-2:] == [char1, char1]:
                if not heap: break
                count2, char2 = heapq.heappop(heap)

                res.append(char2)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))
                
                heapq.heappush(heap, (count1, char1))

            else:
                res.append(char1)
                count1 += 1
                if count1 < 0:
                    heapq.heappush(heap, (count1, char1))

        return "".join(res)

        