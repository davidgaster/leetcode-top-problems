# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        1 0    1 1    1 1    1 1
        0 0 -> 1 0 -> 1 2 -> 1 2    ans = 3
        0 0    0 0    1 0    1 3   
        At any point in time, the total # of ways to get to the current square is the
        sum of the number of ways it took to get to the square above and the square to the left.
        dp[i] = dp[i][j-1] + dp[i-1][j]
        '''
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1: continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[m][n]
        