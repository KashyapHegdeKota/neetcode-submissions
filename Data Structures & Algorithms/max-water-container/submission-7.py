class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        height = 0
        maxArea = 0
        while l < r:
            minHeight = min(heights[l], heights[r])
            maxArea = max(maxArea, (minHeight * (r-l)))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea