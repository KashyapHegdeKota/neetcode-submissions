class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stk = []
        d = {'(':')', '[':']','{':'}'}
        print(d.keys())
        for i in s:
            if i in d.keys():
                stk.append(i)
            elif i in d.values():
                if stk:
                    item = stk.pop()
                else:
                    return False
                if i != d[item]:
                    return False
                
        if stk:
            return False
        else:
            return True
        