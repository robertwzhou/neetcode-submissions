class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if target < nums[m]:
                hi = m
            elif target > nums[m]:
                lo = m + 1
            else:
                return m
        return -1