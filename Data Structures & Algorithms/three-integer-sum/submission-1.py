class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i - 1] == num:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if num + nums[l] + nums[r] < 0:
                    l += 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplets.append([num, nums[l], nums[r]])
                    # keep looking
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return triplets