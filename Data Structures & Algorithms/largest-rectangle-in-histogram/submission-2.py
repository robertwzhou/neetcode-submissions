class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            # if stack empty or current height > stack's height
            #     append (index, height)
            #if len(stack) < 1 or h > stack[-1][1]:
            #    stack.append((i, h))
            # while stack not empty and current height < stack's height:
            #     pop and calculate
            while stack and h < stack[-1][1]:
                pop_i, pop_h = stack.pop()
                max_area = max(max_area, pop_h * (i - pop_i))
                #stack.append((pop_i, h))
                start = pop_i
            stack.append((start, h))
        while stack:
            pop_i, pop_h = stack.pop()
            max_area = max(max_area, pop_h * (len(heights) - pop_i))
        return max_area