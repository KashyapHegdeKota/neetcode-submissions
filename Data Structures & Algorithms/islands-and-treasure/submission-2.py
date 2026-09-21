from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2147483647
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))

        dist = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if(
                        min(nr,nc) < 0 or
                        nr == rows or
                        nc == cols or
                        (nr,nc) in visited or
                        grid[nr][nc] == -1
                    ):
                        continue
                    visited.add((nr,nc))
                    queue.append([nr,nc])
            dist += 1
                