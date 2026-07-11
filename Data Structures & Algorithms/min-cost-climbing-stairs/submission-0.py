class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cumulative_cost = [0 for _ in range(len(cost) + 1)]
        for i in range(2, len(min_cumulative_cost)):
            min_cumulative_cost[i] = min(min_cumulative_cost[i - 2] + cost[i - 2], min_cumulative_cost[i - 1] + cost[i - 1])
        return min_cumulative_cost[len(cost)]