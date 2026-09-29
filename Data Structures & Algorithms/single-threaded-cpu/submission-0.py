class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t: t[0])

        heap = []
        res = []
        time = tasks[0][0]
        i = 0

        while i < len(tasks) or heap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                proc_time, idx = heapq.heappop(heap)
                time += proc_time
                res.append(idx)

            else:
                time = tasks[i][0]

        return res


