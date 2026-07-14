class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0] * len(temperatures)
        for t in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[t] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                result[t] = stack[-1] - t
            stack.append(t)
        return result