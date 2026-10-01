class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums)+1) for _ in range(len(nums))]
        def dp(i,j):
            if i == len(nums):
                return 0
            if memo[i][j+1] != -1:
                return memo[i][j+1]
            #Not including current
            maxLen = dp(i+1,j)
            if j == -1 or nums[j] < nums[i]:
                maxLen = max(maxLen, 1 + dp(i+1,i))
            memo[i][j+1] = maxLen
            return memo[i][j+1]
        return dp(0,-1)

