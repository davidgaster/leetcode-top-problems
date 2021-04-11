# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    """
    Instead of using auxillary space to store the rows and columns,
    we can use the last row and last col to a 0 if a 0 exists there.
    Then, loop through the remainder of the matrix and set those columns
    or rows to 0. 
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = not all(matrix[0])
        first_col_has_zero = False
        
        for row in matrix:
            if row[0] == 0:
                first_col_has_zero = True
                break
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
                    
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        if first_row_has_zero:
            matrix[0] = [0] * n
        
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
          
    def nPlusMspace(self, matrix: List[List[int]]) -> None:
        """
        1 1 1
        1 0 1
        1 1 1
        rows = F F F
        cols = F F F
        O(M + N) space
        O(MN) runtime
        """  
        M = len(matrix)
        N = len(matrix[0])
        row = [False for _ in range(M)]
        col = [False for _ in range(N)]
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(M):
            for j in range(N):
                if row[i] or col[j]:
                    matrix[i][j] = 0
                        