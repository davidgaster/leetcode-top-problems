# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        text1 = abcde
        text2 = ace
        dp[i][j] = longest common subsequence of strings text1[:i] and text2[:j]
             a b c d e
           0 0 0 0 0 0
         a 0 1 1 1 1 1 
         c 0 1 1 2 2 2
         e 0 1 1 2 2 3
         take substrings abc, ac
         the last characters 'c' match, so the answer is 1 + the LCS of ab and a.
        '''
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]