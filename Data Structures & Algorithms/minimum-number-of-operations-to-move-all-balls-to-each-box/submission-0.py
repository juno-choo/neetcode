class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ballSet = set()
        for i, x in enumerate(boxes):
            if x == "1":
                ballSet.add(i)
        print(ballSet)

        res = []

        for i in range(len(boxes)):
            cnt = 0
            for x in ballSet:
                if x - i != 0:
                    cnt += abs(x-i)
            res.append(cnt)

        return res