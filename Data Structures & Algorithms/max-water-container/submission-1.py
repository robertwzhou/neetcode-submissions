class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(l: int, r: int) -> int:
            return min(heights[l], heights[r]) * (r - l)
        l = 0
        r = len(heights) - 1
        maxArea = area(l, r)
        while l < r:
            diff = heights[l] - heights[r]
            if diff <= 0:
                l += 1
            if diff >= 0:
                r -= 1
            maxArea = max(maxArea, area(l, r))
        return maxArea