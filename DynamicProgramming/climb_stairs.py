# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
             _
           _| |
         _|   |
        |_____|
        Dynamic programming: memoize previously computed subproblems.
        Top-down approach, take all the ways to jump to the nth stair from
        the n-1th and n-2th stairs.
        '''
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        
        return memo[n]