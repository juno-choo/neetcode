class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # build graph and degree array
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        degree = [0] * n
        for i in range(n):
            degree[i] = len(graph[i])

        # put leaf nodes in q
        q = deque([i for i in range(n) if degree[i] == 1])
        visited = set()

        # remove nodes doing multisource bfs by decrementing degree[i]
        remaining = n
        while remaining > 2:
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()

                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei) # its a leaf node

                remaining -= 1
        # either one or 2 nodes will be left for mst
        return list(q)

