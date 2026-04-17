class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = [0] *26
        d2 = [0] * 26

        for i in s:
            d1[ord(i)-ord('a')] += 1
        for j in t:
            d2[ord(j)-ord('a')] += 1
        if d1 == d2:
            return True
        return False
        
