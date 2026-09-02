class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colmap = [set() for i in range(9)]
        for boxrow in range(3):
            boxmap = [set() for i in range(3)]
            for row in range(3):
                rowset = set()
                for c in range(9):
                    r = boxrow * 3 + row
                    square = board[r][c]
                    if square != ".":
                        if square in rowset:
                            return False
                        rowset.add(square)
                        if square in boxmap[c // 3]:
                            return False
                        boxmap[c // 3].add(square)
                        if square in colmap[c]:
                            return False
                        colmap[c].add(square)
        return True