class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        def check(r, c, steps):
            if r < 0 or r == ROWS or c < 0 or c == COLS or rooms[r][c] != 2147483647 or (r, c) in visit:
                return
            visit.add((r, c))
            rooms[r][c] = steps
            q.append((r,c))

        steps = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                check(r+1, c, steps+1)
                check(r, c+1, steps+1)
                check(r-1, c, steps+1)
                check(r, c-1, steps+1)

            steps += 1