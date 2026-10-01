class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        def dp(i):
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if dp(j+1):
                        return True
            return False
        return dp(0)
