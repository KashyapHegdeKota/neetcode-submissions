class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in nums:
            if i in counts.keys():
                counts[i] += 1
            else:
                counts[i] = 1
        majority = max(counts, key = counts.get)
        return majority