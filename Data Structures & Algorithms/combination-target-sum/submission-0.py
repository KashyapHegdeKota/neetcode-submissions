class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path, start, total):
            if total == target:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if total + num > target:
                    continue
                path.append(num)
                backtrack(path, i, total+num)
                path.pop()
        backtrack([], 0, 0)
        return res