class Solution:    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        noOfRows, noOfColumns = len(grid), len(grid[0])

        def dfs(r,c,level):
            if r < 0 or c < 0 or r >= noOfRows or c >= noOfColumns or grid[r][c] == -1 or level > grid[r][c]:
                return
            
            grid[r][c] = level

            dfs(r-1, c  , level+1)
            dfs(r  , c-1, level+1)
            dfs(r+1, c  , level+1)
            dfs(r  , c+1, level+1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i,j, 0)