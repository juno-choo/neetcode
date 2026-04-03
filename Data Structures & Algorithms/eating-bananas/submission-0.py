import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            count = 0
            for n in piles:
                count += math.ceil(n/k)

            if count > h:
                l = k + 1
            else:
                r = k - 1

        return l
