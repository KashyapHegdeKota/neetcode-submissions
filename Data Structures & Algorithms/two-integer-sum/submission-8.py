class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i
        print(hash)
        
        for j, n in enumerate(nums):
            if target - n in hash and hash[target-n] != j:
                ans.append(j)
                ans.append(hash[target-n])
                break
        return ans