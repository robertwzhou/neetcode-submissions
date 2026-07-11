class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        # if land is found, turn the island into water
        def found(i: int, j: int) -> bool:
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i > 0:
                    found(i - 1, j)
                if i + 1 < len(grid):
                    found(i + 1, j)
                if j > 0:
                    found(i, j - 1)
                if j + 1 < len(grid[0]):
                    found(i, j + 1)
                return True
        # search for land
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if found(i, j):
                    islands += 1
        return islands