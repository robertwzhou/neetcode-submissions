class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_sets = [set() for _ in range(9)]
        def validSubboxes(subboard: List[List[str]]) -> bool:
            subbox_sets = [set() for _ in range(3)]
            for row in subboard:
                row_set = set()
                for c in range(len(row)):
                    digit = row[c]
                    if digit != ".":
                        if digit in row_set or digit in subbox_sets[c // 3] or digit in column_sets[c]:
                            return False
                        row_set.add(digit)
                        subbox_sets[c // 3].add(digit)
                        column_sets[c].add(digit)
            return True
        return validSubboxes(board[0:3]) and validSubboxes(board[3:6]) and validSubboxes(board[6:9])