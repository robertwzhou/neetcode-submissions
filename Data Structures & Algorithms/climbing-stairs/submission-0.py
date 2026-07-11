class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            ways[i] = ways[i - 2] + ways[i - 1]
        return ways[n]