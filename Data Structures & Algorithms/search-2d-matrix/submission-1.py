class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or matrix[len(matrix)-1][len(matrix[0])-1] < target:
            return False
        l, r = 0, len(matrix)
        while l < r:
            m = l + (r - l) // 2
            if target < matrix[m][0]:
                r = m
            elif matrix[m][len(matrix[0])-1] < target:
                l = m + 1
            else:
                break
        l, r = 0, len(matrix[0])
        while l < r:
            c = l + (r - l) // 2
            if target < matrix[m][c]:
                r = c
            elif matrix[m][c] < target:
                l = c + 1
            else:
                return True
        return False