class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(path, index, total):
            if total == target:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                num = candidates[i]
                if i > index and num == candidates[i-1]:
                    continue
                if total + num > target:
                    break
                path.append(num)
                backtrack(path, i + 1, total + num)
                path.pop()
        backtrack([],0,0)
        return res