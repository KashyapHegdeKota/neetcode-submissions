from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in s:
            dict1[i] += 1
        
        for j in t:
            dict2[j] += 1

        if dict1.items() == dict2.items():
            return True
        return False