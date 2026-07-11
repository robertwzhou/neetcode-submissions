class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        while l < r:
        # move left or right pointer, whichever max height is shorter
        # update max height
        # add max height - height to maxArea
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                maxArea += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                maxArea += maxRight - height[r]
        return maxArea