from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)


        for i in strs:
            S = [x for x in i]
            S.sort()
            S = tuple(S)
            dict[S].append(i)
        return list(dict.values())