class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i):
            if i  == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            #Consume one digit
            res = dp(i+1)
            
            #Check if the 2-char number is between 10 to 26 (lies within the valid range)
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                #Consume two digits
                res += dp(i+2)
            return res
        return dp(0)