class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(rowIndex):
            tmp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(tmp[j] + tmp[j+1])
            res.append(row)
        return res[rowIndex]