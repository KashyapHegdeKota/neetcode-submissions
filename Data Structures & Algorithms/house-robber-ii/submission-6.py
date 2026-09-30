class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(i, end):
            if i >= end:
                return 0
            rob_curr = nums[i] + dp(i+2, end)
            skip_curr = dp(i+1,end)

            return max(rob_curr, skip_curr)
        rob_first = dp(0, len(nums)-1)
        rob_second = dp(1, len(nums))
        return max(rob_first, rob_second)
