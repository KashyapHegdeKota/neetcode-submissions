class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if(
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[index]
            ):
                return False
            tmp = board[row][col]
            board[row][col] = "#"

            for dr, dc in moves:
                nr = row + dr
                nc = col + dc

                if backtrack(nr, nc, index + 1):
                    board[row][col] = tmp
                    return True
            board[row][col] = tmp
            return False
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False
        
