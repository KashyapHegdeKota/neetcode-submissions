from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2147483647

        def bfs(row, col):
            q = deque([(row,col)])
            visited = [[False] * cols for _ in range(rows)]
            visited[row][col] = True
            dist = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return dist
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if(
                            0 <= nr < rows and
                            0 <= nc < cols and
                            not visited[nr][nc] and
                            grid[nr][nc] != -1
                        ):
                            visited[nr][nc] = True
                            q.append((nr,nc))
                dist += 1
            return INF
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)
        