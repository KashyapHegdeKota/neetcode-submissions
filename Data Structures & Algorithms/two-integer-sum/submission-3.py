class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j] == target):
                    x.append(i)
                    x.append(j)
        return x