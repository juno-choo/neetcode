from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        res = ""
        l, r = 0, len(self.timeMap[key]) - 1 if self.timeMap[key] else 0
        while l <= r:
            m = (l+r) // 2

            if timestamp >= self.timeMap[key][m][0]:
                res = self.timeMap[key][m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        