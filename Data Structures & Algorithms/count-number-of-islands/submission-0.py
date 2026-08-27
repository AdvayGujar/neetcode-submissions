class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = set()
        island = 0

        noOfRows = len(grid)
        noOfColumns = len(grid[0])

        def explore(grid, curRow, curCol):
            if (curRow < 0 or curCol < 0
            or curRow >= noOfRows or curCol >= noOfColumns
            or (curRow, curCol) in explored
            or grid[curRow][curCol] == "0"):
                return
            
            explored.add((curRow,curCol))

            explore(grid, curRow - 1, curCol)
            explore(grid, curRow, curCol - 1)
            explore(grid, curRow + 1, curCol)
            explore(grid, curRow, curCol + 1)

        for i in range(noOfRows):
            for j in range(noOfColumns):
                if (i,j) not in explored and grid[i][j] == "1":
                    explore(grid, i, j)
                    island += 1
        
        return island