class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(path, index):
            if index == len(nums):
                res.append(path[:])
                return
            path.append(nums[index])
            backtrack(path, index+1)
            path.pop()

            next = index + 1
            while next < len(nums) and nums[next] == nums[index]:
                next += 1
            backtrack(path, next)
        backtrack([],0)
        return res