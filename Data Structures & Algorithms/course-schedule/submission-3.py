class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visited:
                return True

            if crs in visiting:
                return False

            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for prereqs in preMap[crs]:
                if not dfs(prereqs):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

