# https://leetcode.com/problems/edit-distance/
class Solution(object):
    def minDistance(self, word1, word2):
        """
        Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

        You have the following three operations permitted on a word:

        Insert a character
        Delete a character
        Replace a character
        
        word1 = "horse"
        word2 = "ros"
        output = 3 (replace 'h' with 'r', remove 2nd 'r', remove 'e')
        
        dp[i][j] = min # ops to convert word1[:i] to word2[:j]
            h o r s e
          0 1 2 3 4 5
        r 1 1 2 2 0 0
        o 2 0 0 0 0 0
        s 3 0 0 0 0 0
        """
        n = len(word1)
        m = len(word2)
        if word1 == '': return m
        if word2 == '': return n
        
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    
        return dp[n][m]
        