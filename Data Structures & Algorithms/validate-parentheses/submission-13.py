class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: odd length strings can never be balanced
        if len(s) % 2 != 0:
            return False
            
        stk = []
        d = {'(': ')', '[': ']', '{': '}'}
        
        for char in s:
            if char in d:  # If it's an opening bracket
                stk.append(char)
            else:          # If it's a closing bracket
                if not stk or d[stk.pop()] != char:
                    return False
                
        # Valid only if all opened brackets were closed
        return len(stk) == 0