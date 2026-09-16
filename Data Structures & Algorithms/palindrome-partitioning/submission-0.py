class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(path, i):
            def isPalindrome(s, i, j):
                while i < j:
                    if s[i] != s[j]:
                        return False
                    i, j = i+1, j - 1
                return True
            if i == len(s):
                res.append(path[:])
                return
            for end in range(i, len(s)):
                if isPalindrome(s, i, end):
                    path.append(s[i:end+1])
                    backtrack(path, end+1)
                    path.pop()
        
        backtrack([],0)
        return res