from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        def bfs(x,y):
            queue = deque([(x,y)])
            visited.add((x,y))
            area = 0

            while queue:
                i, j = queue.popleft()
                area += 1

                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]

                    if(
                        0 <= new_i < rows and
                        0 <= new_j < cols and
                        grid[new_i][new_j] == 1 and
                        (new_i, new_j) not in visited
                    ):
                        visited.add((new_i, new_j))
                        queue.append((new_i,new_j))
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, bfs(i,j))
        
        return maxArea