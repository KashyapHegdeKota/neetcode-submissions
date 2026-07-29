class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        maxLength = 0
        for i in seq:
            if i - 1 not in seq:
                longest = 1
                while(i+longest) in seq:
                    longest += 1
                maxLength = max(longest, maxLength)
        return maxLength
                
