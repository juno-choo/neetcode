class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
            
        res = []
        cycle, visit = set(), set()

        def dfs(node):
            if node in cycle: return False
            if node in visit: return True
            
            cycle.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            visit.add(node)
            cycle.remove(node)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res