class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def g(available_open_parentheses: int, available_close_parentheses: int, current_string: str) -> List[str]:
            if available_open_parentheses == available_close_parentheses:
                return g(available_open_parentheses - 1, available_close_parentheses, current_string + "(")
            if available_open_parentheses == 0:
                return [current_string + ")" * available_close_parentheses]
            return g(available_open_parentheses - 1, available_close_parentheses, current_string + "(") + g(available_open_parentheses, available_close_parentheses - 1, current_string + ")")
        return g(n, n, "")