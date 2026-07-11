class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()
        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temperature:
                j, t = stack.pop()
                result[j] = i - j
            stack.append((i, temperature))
        return result