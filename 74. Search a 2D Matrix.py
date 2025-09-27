class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        columns_no=len(matrix[0])
        rows_no=len(matrix)
        for row in range(0,rows_no):
            if target<=matrix[row][columns_no-1]:
                for column in range(0,columns_no):
                    if matrix[row][column]==target:
                        return True
        return False
        