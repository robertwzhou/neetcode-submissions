class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                subtrahend = stack.pop()
                stack.append(stack.pop() - subtrahend)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                divisor = stack.pop()
                stack.append(int(stack.pop() / divisor))
            else:
                stack.append(int(token))
        return stack[0]