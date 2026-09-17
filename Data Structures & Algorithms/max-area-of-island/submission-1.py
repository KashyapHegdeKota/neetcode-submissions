class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        maxArea = 0
        def dfs(row, col) -> int:
            if(
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] == 0
            ):
                return 0
            grid[row][col] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    tmp = dfs(i,j)
                    if tmp > maxArea:
                        maxArea = tmp
        return maxArea 