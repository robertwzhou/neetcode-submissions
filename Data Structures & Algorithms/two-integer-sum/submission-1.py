class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        # traverse
        for i, num in enumerate(nums):
            # if complement in visited, answer found
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            # else, put num, i in visited
            visited[num] = i