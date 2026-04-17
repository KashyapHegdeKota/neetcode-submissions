class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = [x for x in s]
        S.sort()
        print(S)
        T =[x for x in t]
        T.sort()
        if(S == T):
            return True
        return False