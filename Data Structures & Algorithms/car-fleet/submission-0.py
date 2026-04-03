class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        track = []

        for i in range(len(speed)):
            track.append((position[i], speed[i]))

        track.sort()

        leadTime = (target - track[-1][0]) / track[-1][1]
        for i in range(len(track)-1, -1, -1):
            curTime = (target - track[i][0]) / track[i][1]

            if curTime > leadTime:
                res += 1
                leadTime = curTime

        return res