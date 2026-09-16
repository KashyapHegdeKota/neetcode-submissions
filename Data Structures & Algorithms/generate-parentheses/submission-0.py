class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, open, close):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            for i in ["(", ")"]:
                if i == "(" and open >= n:
                    continue
                if i == ")" and close >= open:
                    continue
                
                path.append(i)
                if i  == "(":
                    backtrack(path, open+1, close)
                else:
                    backtrack(path, open, close + 1)
                path.pop()
        backtrack([],0,0)
        return res