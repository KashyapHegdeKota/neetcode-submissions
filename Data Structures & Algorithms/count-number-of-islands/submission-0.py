class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        def dfs(x,y):
            if (x < 0 or y < 0
                or x >= rows or y >= cols
                or grid[x][y] == "0"):
                return
            grid[x][y] = "0" # Mark as visited

            for direction in directions:
                dfs(x+direction[0], y+direction[1])
        
        count_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count_islands += 1
        return count_islands