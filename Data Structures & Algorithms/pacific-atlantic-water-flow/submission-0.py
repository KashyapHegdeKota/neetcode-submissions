class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set() #Hash set to store cells connected to Pacific Ocean
        atlantic = set() # Hash set to store cells connected to Atlantic Ocean

        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col, visited, prevHeight):
            # Boundary check
            if(
                row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                (row, col) in visited or
                heights[row][col] < prevHeight
            ):
                return
            
            visited.add((row,col))

            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])
        
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols - 1, atlantic, heights[i][cols-1])
        
        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])
        
        res = []

        for k in range(rows):
            for l in range(cols):
                if (k,l) in pacific and (k,l) in atlantic:
                    res.append([k,l])
        return res