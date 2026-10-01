class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i,j):
            if i == len(nums):
                return 0
            #Not including current
            maxLen = dp(i+1,j)
            if j == -1 or nums[j] < nums[i]:
                maxLen = max(maxLen, 1 + dp(i+1,i))
            return maxLen
        return dp(0,-1)

