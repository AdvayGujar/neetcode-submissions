from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, prev, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prev:
                return

            visited.add((r, c))

            dfs(r - 1, c, heights[r][c], visited)
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)

        for r in range(rows):
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)
        for c in range(cols):
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)

        return [list(cell) for cell in (pacific & atlantic)]