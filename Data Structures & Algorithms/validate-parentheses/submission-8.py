class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stk = []
        opn = ['[','{','(']
        close = [']','}',')']
        d = {'(':')', '[':']','{':'}'}
        for i in s:
            if i in opn:
                stk.append(i)
                print(i + "has been appended to stack")
            elif i in close:
                if stk:
                    item = stk.pop()
                else:
                    return False
                print(item + "has been popped")
                if i == d[item]:
                    continue
                elif i != d[item]:
                    return False
                
        if stk:
            return False
        else:
            return True
        