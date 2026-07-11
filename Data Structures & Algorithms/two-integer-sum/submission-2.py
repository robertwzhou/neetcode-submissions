class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {target - ni: i for i, ni in enumerate(nums)}
        for j, nj in enumerate(nums):
            if nj in complements and complements[nj] != j:
                i = complements[nj]
                return [min(i, j), max(i, j)]