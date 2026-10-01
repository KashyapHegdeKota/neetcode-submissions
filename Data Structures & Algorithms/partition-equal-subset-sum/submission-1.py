class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        memo = {}
        def dp(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            if (i, target) in memo:
                return memo[(i,target)]

            memo[(i,target)] = dp(i+1, target) or dp(i+1, target-nums[i])
            return memo[(i,target)]
        return dp(0,sum(nums)//2)