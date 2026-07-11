class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # make queue of treasure chest locations
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        def update(i: int, j: int) -> None:
            # location is within bounds and non-negative int
            # update adjacent locations
            # add valid adjacent locations (within bounds, positive int)
            if i > 0 and grid[i-1][j] > grid[i][j]+1:
                grid[i-1][j] = grid[i][j]+1
                q.append((i-1,j))
            if i + 1 < len(grid) and grid[i+1][j] > grid[i][j]+1:
                grid[i+1][j] = grid[i][j]+1
                q.append((i+1,j))
            if j > 0 and grid[i][j-1] > grid[i][j]+1:
                grid[i][j-1] = grid[i][j]+1
                q.append((i,j-1))
            if j + 1 < len(grid[0]) and grid[i][j+1] > grid[i][j]+1:
                grid[i][j+1] = grid[i][j]+1
                q.append((i,j+1))
        # while queue:
        while q:
        #   poll from queue
            i ,j = q.popleft()
        #   call function on polled item
            update(i, j)
        #       update graph
        #       put adjacent land locations in queue