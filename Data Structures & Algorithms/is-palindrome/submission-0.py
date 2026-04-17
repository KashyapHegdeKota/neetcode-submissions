class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =s.lower()
        S = []
        rev = []
        for i in s:
            if i.isalnum():
                S.append(i)
        for i in S:
            rev.insert(0,i)
        print(S)
        print(rev)
        if S == rev:
            return True
        return False