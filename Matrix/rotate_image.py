# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1 2 3      1 4 7      7 4 1
        4 5 6  ->  2 5 8  ->  8 5 2 
        7 8 9      3 6 9      9 6 3
        flip       reverse
        diagonals  rows
        """
        N, M = len(matrix), len(matrix[0])
        for j in range(M):
            for i in range(j,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(N):
            left, right = 0, M-1
            while left <= right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
