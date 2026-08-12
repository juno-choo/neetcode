class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, a, b):
            if node in seen:
                return

            seen.add(node)

            for nei in adj[node]:
                if (node == a and nei == b) or (node == b and nei == a):
                    continue

                dfs(nei, a, b)

        for i in range(len(edges) - 1, -1, -1):
            seen = set()

            a, b = edges[i]
            dfs(1, a, b)

            if len(seen) == len(edges):
                return edges[i]

