class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort array by intervals[i][0]
        # if intervals[i][0] < prev_end, count += 1, greedy update the min prev_end
        # else, set prev_end to current end
        res = 0
        intervals.sort()
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                res += 1
                prev_end = min(intervals[i][1], prev_end)

            else:
                prev_end = intervals[i][1]

        return res


                               

