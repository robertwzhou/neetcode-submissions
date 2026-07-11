class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        starting_nums = [num for num in unique_nums if num - 1 not in unique_nums]
        longest = 0
        for num in starting_nums:
            length = 1
            while num + 1 in unique_nums:
                length += 1
                num += 1
            longest = max(longest, length)
        return longest