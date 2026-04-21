class Solution:
    def prefixProduct(self, nums: List[int]) -> List[int]:
        prefArr = [1] * (len(nums))
        curr = 1
        for i in range(len(nums)):
            prefArr[i] = curr
            curr *= nums[i]
        return prefArr
    
    def suffixProduct(self, nums: List[int]) -> List[int]:
        suffArr = [1] * (len(nums))
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            suffArr[i] *= curr
            curr *= nums[i]
        return suffArr
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = i+1
        prefix = self.prefixProduct(nums)
        #print(prefix)
        suffix = self.suffixProduct(nums)
        #print(suffix)

        res = []

        for i in range(len(nums)):
            res.append(suffix[i] * prefix[i])
        return res