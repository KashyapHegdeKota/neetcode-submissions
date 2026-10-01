class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            prev_max = curr_max
            prev_min = curr_min

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

            answer = max(answer, curr_max)

        return answer