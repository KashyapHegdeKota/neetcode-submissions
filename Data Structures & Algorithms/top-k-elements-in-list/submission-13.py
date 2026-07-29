from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        dict = defaultdict(int)
        for i in nums:
            dict[i] += 1

        for num, freq in dict.items():
            buckets[freq].append(num)

        res = []

        for i in range(len(buckets)-1, 0, -1):
            for nums in buckets[i]:
                res.append(nums)
                if len(res) == k:
                    return res
        