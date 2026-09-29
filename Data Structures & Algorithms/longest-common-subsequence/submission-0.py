class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len = len(text1)
        text2_len = len(text2)

        matrix = [[0] * text1_len for _ in range(text2_len)]

        for i in range(text2_len):
            for j in range(text1_len):
                if text1[j] == text2[i]:
                    diag = matrix[i - 1][j - 1] if i >= 1 and j >= 1 else 0
                    matrix[i][j] = diag + 1
                else:
                    top = matrix[i - 1][j] if i >= 1 else 0
                    left = matrix[i][j - 1] if j >= 1 else 0
                    matrix[i][j] = max(top, left)
        
        return matrix[-1][-1]