class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        cycle, visit = set(), set()

        def dfs(node):
            if node in cycle: return False
            if node in visit: return True

            cycle.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            cycle.remove(node)
            visit.add(node)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True