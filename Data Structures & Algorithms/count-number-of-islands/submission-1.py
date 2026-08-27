class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        noOfRows, noOfColumns = len(grid), len(grid[0])
        islands = 0

        def explore(r, c):
            if r < 0 or c < 0 or r >= noOfRows or c >= noOfColumns or grid[r][c] == "0":
                return
            
            # Mark cell as visited directly in-place
            grid[r][c] = "0"

            explore(r - 1, c)
            explore(r + 1, c)
            explore(r, c - 1)
            explore(r, c + 1)

        for i in range(noOfRows):
            for j in range(noOfColumns):
                if grid[i][j] == "1":
                    explore(i, j)
                    islands += 1
        
        return islands