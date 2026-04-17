class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            print(s[l], s[r])
            if (s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True
    def isAlphaNum(self, i):
        if ord(i)>=ord('A') and ord(i)<= ord('Z'):
            return True
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            return True
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            return True
        else:
            return False