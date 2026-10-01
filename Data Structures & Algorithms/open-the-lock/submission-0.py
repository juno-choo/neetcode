class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def get_neighbors(state):
            res = []
            state_l = list(state)

            # for each elem, mutate the elem to 2 possible turns and append the entire state
            for i in range(len(state_l)):
                right_turn = str((int(state_l[i]) + 1) % 10)
                left_turn = str((int(state_l[i]) - 1) % 10)

                # create 2 copies and mutate the elem at idx
                state_copy_r = state_l.copy()
                state_copy_l = state_l.copy()

                state_copy_r[i] = right_turn
                state_copy_l[i] = left_turn

                res.append("".join(state_copy_r))
                res.append("".join(state_copy_l))

            return res

        deadends = set(deadends)
        visited = { "0000" }
        if "0000" in deadends: return -1
        if target == "0000": return 0

        q = deque(["0000"])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                neighbors = get_neighbors(node)

                for nei in neighbors:
                    if nei not in visited and nei not in deadends:
                        q.append(nei)
                        visited.add(nei)
                        if nei == target:
                            return level + 1

            level += 1

        return -1