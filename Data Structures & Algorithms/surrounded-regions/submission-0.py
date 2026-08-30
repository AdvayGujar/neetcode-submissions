class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        queue = deque()

        for j in range(cols):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[rows - 1][j] == "O":
                queue.append((rows - 1, j))
        
        for i in range(1, rows - 1):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][cols - 1] == "O":
                queue.append((i, cols - 1))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            board[r][c] = "#"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    queue.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"