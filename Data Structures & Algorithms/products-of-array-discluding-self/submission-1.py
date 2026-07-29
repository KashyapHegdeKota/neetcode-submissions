class Solution:
    def buildPref(self, nums: List[int]) -> List[int]:
        pref = [1] * (len(nums)+1)
        for i in range(len(nums)):
            pref[i+1] = pref[i] * nums[i]
        return pref

    def buildSuff(self, nums: List[int]) -> List[int]:
        suf = [1] * (len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            suf[i] = suf[i+1] * nums[i]
        return suf
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        suff = []
        pref = self.buildPref(nums)
        suff = self.buildSuff(nums)
        # print(pref)
        # print(suff)
        for i in range(len(nums)):
            output.append(pref[i]*suff[i+1])
        return output
