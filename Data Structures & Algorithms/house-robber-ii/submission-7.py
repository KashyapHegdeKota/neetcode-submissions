class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def dp(i, end):
            if i >= end:
                return 0
            if (i, end) in memo:
                return memo[(i,end)]
            rob_curr = nums[i] + dp(i+2, end)
            skip_curr = dp(i+1,end)

            memo[(i,end)] = max(rob_curr, skip_curr)
            return memo[(i,end)]
        rob_first = dp(0, len(nums)-1)
        rob_second = dp(1, len(nums))
        return max(rob_first, rob_second)
