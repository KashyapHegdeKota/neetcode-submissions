class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i in nums:
            if i in hash.keys():
                hash[i] += 1
            else:
                hash[i] = 1
        print(hash.values())
        for j in hash.values():
            if j > 1:
                return True
                break
        return False