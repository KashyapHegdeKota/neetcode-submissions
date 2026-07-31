class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []
        operators = {'+', '-', '*', '/'} # Using a set for faster O(1) lookups
        
        for token in tokens:
            if token not in operators:
                stk.append(int(token)) # Convert to int immediately
            else:
                op1 = stk.pop() # This is the second operand
                op2 = stk.pop() # This is the first operand
                
                if token == '+':
                    stk.append(op2 + op1)
                elif token == '-':
                    stk.append(op2 - op1) # Fixed order
                elif token == '*':
                    stk.append(op2 * op1)
                elif token == '/':
                    # Floating division converted to int truncates towards zero
                    stk.append(int(op2 / op1)) # Fixed order & truncation
                    
        return stk.pop()
