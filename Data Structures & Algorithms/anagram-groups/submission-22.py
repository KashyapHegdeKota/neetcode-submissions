class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            freq = [0] *26
            for c in i:
                freq[ord(c)-ord('a')] += 1
            res[tuple(freq)].append(i)
        return list(res.values())