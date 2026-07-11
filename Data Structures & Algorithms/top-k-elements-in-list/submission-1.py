class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        s = sorted([[f, n] for n, f in frequencies.items()], reverse=True)
        return [s[i][1] for i in range(k)]