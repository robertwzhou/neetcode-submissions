class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        multiplier = nums[0]
        for i in range(1, len(nums)):
            output[i] *= multiplier
            multiplier *= nums[i]
        multiplier = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= multiplier
            multiplier *= nums[i]
        return output