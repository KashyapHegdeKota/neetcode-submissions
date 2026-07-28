from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)

        for i in nums:
            if counts[i] >= 1:
                return True
            else:
                counts[i] += 1
        return False