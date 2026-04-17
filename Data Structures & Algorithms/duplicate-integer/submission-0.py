class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = [] #Initializing a new list
        for i in nums: #Iterating through the nums list.
            if i not in new:
                new.append(i)
            else:
                return True
        return False



         