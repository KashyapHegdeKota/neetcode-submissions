class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cels = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = (i//3 + 3*(j//3))
                val = board[i][j]
                if val != '.':
                    if val in rows[i] or val in cols[j] or val in cels[cell]:
                        print(f"{i} {j} {val in rows[i]} {val in cols[j]} {val in cels[cell]}")
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    cels[cell].add(val)
        return True