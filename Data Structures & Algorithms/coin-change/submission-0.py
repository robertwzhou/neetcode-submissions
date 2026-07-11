class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = {0: 0}
        for a in range(1, amount + 1):
            l = [amounts[a - c] for c in coins if a - c in amounts]
            if l:
                amounts[a] = min(l) + 1
        return amounts[amount] if amount in amounts else -1