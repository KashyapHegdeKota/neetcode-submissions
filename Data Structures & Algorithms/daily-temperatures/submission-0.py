class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                stkTop, stkIndex = stk.pop()
                res[stkIndex] = i-stkIndex
            stk.append((temp, i))
        return res