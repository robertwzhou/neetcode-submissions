class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_taken(eating_rate: int) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / eating_rate)
            return hours
        k = max(piles)
        l, r = 1, k
        while l < r:
            m = l + (r - l) // 2
            if hours_taken(m) <= h:
                k = m
                r = m
            else:
                l = m + 1
        return k