class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # given prereqs = [[a, b]...], map a -> [b...]

        # given queries = [[u, v]...], search from u, if we arrive back at self, return false (in 'visiting' set). elif arrive v, return true. when search ends, return false. append the res to array

        # use set after visited nodes
        prereq_map = defaultdict(list)
        for a, b in prerequisites:
            prereq_map[a].append(b)

        def dfs(crs, pre, visited, visiting):
            if crs in visiting or crs in visited: # cycle or theres no path to the target (pre)
                return False

            if crs == pre: # we reached our destination
                return True

            visiting.add(crs)
            for nei in prereq_map[crs]:
                if dfs(nei, pre, visited, visiting):
                    return True
            visiting.remove(crs)
            visited.add(crs)
            return False

        res = []
        for u, v in queries:
            res.append(dfs(u, v, set(), set()))

        return res
