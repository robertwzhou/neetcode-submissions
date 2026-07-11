class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find left and right bounds
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        if nums[l] <= target and target <= nums[len(nums)-1]:
            r = len(nums)
        else:
            r = l
            l = 0
        # find target index via binary search
        while l < r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m
            else:
                return m
        return -1