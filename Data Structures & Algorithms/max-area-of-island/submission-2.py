class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        noOfRows, noOfColumns = len(grid), len(grid[0])
        maxArea = 0

        def calcArea(r, c):
            if r < 0 or c < 0 or r >= noOfRows or c >= noOfColumns or grid[r][c] == 0:
                return 0
            
            # Mark cell as visited directly in-place
            grid[r][c] = 0

            return 1 + calcArea(r - 1, c) + calcArea(r + 1, c) + calcArea(r, c - 1) + calcArea(r, c + 1)

        for i in range(noOfRows):
            for j in range(noOfColumns):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, calcArea(i, j))
        
        return maxArea