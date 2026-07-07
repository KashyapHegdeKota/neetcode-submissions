from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        def bfs(x,y):
            queue = deque([(x,y)])
            visited.add((x,y))
            perimeter = 0

            while queue:
                i,j = queue.popleft()
                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if (new_i < 0
                        or new_j < 0
                        or new_i >= rows
                        or new_j >= cols
                        or grid[new_i][new_j] == 0):
                        perimeter += 1
                    elif (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        queue.append((new_i,new_j))
            return perimeter 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i,j)
        return 0