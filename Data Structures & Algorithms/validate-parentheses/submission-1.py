class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                d.append(c)
            elif len(d) == 0:
                return False
            elif (c == ")" and d[-1] == "(") or (c == "}" and d[-1] == "{") or (c == "]" and d[-1] == "["):
                d.pop()
            else:
                return False
        return len(d) == 0