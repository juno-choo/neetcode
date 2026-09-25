class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l <= r:
            m = (l + r) // 2

            days_needed = 1
            cur_load = 0
            for weight in weights:
                if cur_load + weight > m:
                    days_needed += 1
                    cur_load = weight

                else:
                    cur_load += weight

            if days_needed > days:
                l = m + 1

            else:
                r = m - 1

        return l

