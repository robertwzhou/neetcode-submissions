class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque() # always decreasing
        # initialize d
        for i in range(k):
            while d and d[-1][1] < nums[i]:
                d.pop()
            d.append((i, nums[i]))
        maxElements = [d[0][1]]
        for i in range(k, len(nums)):
            if d[0][0] <= i - k:
                d.popleft()
            while d and d[-1][1] < nums[i]:
                d.pop()
            d.append((i, nums[i]))
            maxElements.append(d[0][1])
        return maxElements