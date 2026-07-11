class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [set() for _ in range(9)]
        for triple_row in range(3):
            subbox = [set() for _ in range(3)]
            for r in range(3):
                row = set()
                for c in range(9):
                    sq = board[r + 3 * triple_row][c]
                    if sq != ".":
                        if sq in row or sq in subbox[c // 3] or sq in column[c]:
                            return False
                        row.add(sq)
                        subbox[c // 3].add(sq)
                        column[c].add(sq)
        return True