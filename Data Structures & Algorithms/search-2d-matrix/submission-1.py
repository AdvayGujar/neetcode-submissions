class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        row = None

        #rows
        left = 0
        right = rows -1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target or matrix[mid][columns-1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][columns-1] > target:
                row = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][columns - 1] < target:
                left = mid + 1
        
        if row is not None:
            left = 1
            right = columns - 2
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                elif matrix[row][mid] < target:
                    left = mid + 1

        return False