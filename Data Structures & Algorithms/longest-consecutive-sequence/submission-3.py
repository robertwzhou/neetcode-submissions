class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        seq_lens = {"": 0}
        def find_seq_lens(n: int) -> None:
            if n not in seq_lens:
                if n + 1 in numset:
                    find_seq_lens(n + 1)
                    seq_lens[n] = 1 + seq_lens[n + 1]
                else:
                    seq_lens[n] = 1
        for n in numset:
            find_seq_lens(n)
        return max(seq_lens.values())