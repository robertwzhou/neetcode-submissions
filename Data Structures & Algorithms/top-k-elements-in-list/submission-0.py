class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # gets counts for each unique num
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        # bucket sort
        counts_num = [[] for _ in range(len(nums)+1)]
        for num, count in counts.items():
            counts_num[count].append(num)
        # get k most frequent
        output = []
        i = len(counts_num) - 1
        while k > 0:
            if counts_num[i]:
                output += counts_num[i]
                k -= len(counts_num[i])
            i -= 1
        return output
