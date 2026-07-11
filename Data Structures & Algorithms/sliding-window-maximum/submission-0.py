class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        # we need max-heap, so multiply each number by -1
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)
        for i in range(len(nums) - k + 1):
            while h[0][1] < i:
                heapq.heappop(h)
            maxElements.append(-h[0][0])
            if i + k < len(nums):
                heapq.heappush(h, (-nums[i + k], i + k))
        return maxElements