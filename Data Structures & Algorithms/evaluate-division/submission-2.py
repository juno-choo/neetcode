class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph bidirectional with inverse weights
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))

        # for each (start, end) traverse to find end, if node == end, return prod

        def dfs(node, target, product, visited):
            if node == target:
                return product

            visited.add(node)
            for nei, weight in graph[node]:
                if nei not in visited:
                    res = dfs(nei, target, product * weight, visited)

                    if res != -1:
                        return res

            return -1

        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(start, end, 1.0, set()))

        return res