class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            low, high = i+1, len(nums) - 1
            while low < high:
                if nums[i] + nums[low] + nums[high] < 0:
                    low += 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    tmp = [nums[i], nums[low], nums[high]]
                    if tmp not in res:
                        res.append(tmp)
                    low += 1
                    high -= 1
        return res