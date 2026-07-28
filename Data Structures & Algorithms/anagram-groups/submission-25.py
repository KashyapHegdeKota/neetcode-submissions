from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            s = [0] * 26
            for j in i:
                s[ord(j)-ord('a')] += 1
            dict[tuple(s)].append(i)
        return list(dict.values())