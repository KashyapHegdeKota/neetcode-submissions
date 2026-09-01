class Solution:
    def computeHappy(self, n: int) -> bool:
        output = 0
        while n:
            digit = n%10
            digit = digit ** 2
            output += digit
            n = n//10
        return output
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.computeHappy(n)

        while slow != fast:
            fast = self.computeHappy(self.computeHappy(fast))
            slow = self.computeHappy(slow)
        return True if fast == 1 else False
        