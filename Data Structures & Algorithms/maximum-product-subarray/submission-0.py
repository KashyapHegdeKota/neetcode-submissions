class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[0], nums[0]
            prev_max, prev_min = dp(i-1)
            curr_max = max(
                nums[i],
                nums[i] * prev_max,
                nums[i] * prev_min
            )
            curr_min = min(
                nums[i],
                nums[i] * prev_max,
                nums[i] * prev_min
            )
            return (curr_max, curr_min)
        answer = nums[0]
        for i in range(len(nums)):
            curr_max, curr_min = dp(i)
            answer = max(answer, curr_max)
        return answer