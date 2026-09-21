class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in s:
            if i in hash1.keys():
                hash1[i] += 1
            else:
                hash1[i] = 1
        
        for j in t:
            if j in hash2.keys():
                hash2[j] += 1
            else:
                hash2[j] = 1
        
        if hash1 == hash2:
            return True
        else:
            return False