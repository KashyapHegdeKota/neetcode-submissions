class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1
        res = []
        #print(list(counts.items())[0][1])
        for j in list(counts.items()):
            if j[1] > (n//3):
                res.append(j[0])
        return res