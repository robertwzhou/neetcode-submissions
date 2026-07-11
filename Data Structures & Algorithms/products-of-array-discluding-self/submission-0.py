class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        factor = 1
        for i in range(1, (len(nums))):
            factor *= nums[i-1]
            output[i] = factor
        factor = 1
        for i in range(len(nums)-2, -1, -1):
            factor *= nums[i+1]
            output[i] *= factor
        return output