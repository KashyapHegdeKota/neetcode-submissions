class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col):
            if(
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != "O"
            ):
                return
            board[row][col] = "T"
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    