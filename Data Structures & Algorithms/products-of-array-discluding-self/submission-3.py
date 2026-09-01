class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        factor = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= factor
            factor *= nums[i]
        return output
        """
        factors_ahead = [1] * len(nums)
        factors_behind = [1] * len(nums)
        # forward pass
        for i in range(1, len(nums)):
            factors_ahead[i] = factors_ahead[i - 1] * nums[i - 1]
        # backward pass
        for i in range(len(nums) - 2, -1, -1):
            factors_behind[i] = factors_behind[i + 1] * nums[i + 1]
        return [factors_ahead[i] * factors_behind[i] for i in range(len(nums))]
        """