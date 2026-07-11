class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWater = (j - i) * min(heights[i], heights[j])
        while i < j:
            if heights[i] < heights[j]:
                i += 1
            else: # if heights[i] > heights[j]:
                j -= 1
            maxWater = max(maxWater, (j - i) * min(heights[i], heights[j]))
        return maxWater