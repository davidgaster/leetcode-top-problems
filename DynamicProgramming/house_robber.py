# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, houses: List[int]) -> int:
        '''
        dynamic programming
        dp[i] = max amount of money you can rob up to i houses
        houses =     1 2 3 1
        dp     = 0 0 1 0 0 0
        At each step you either choose to take the profit of the current house + the profit of
        the 2nd house behind you. Or you choose not to rob the current house, thus keep the profit
        of the house directly behind you.
        '''
        n = len(houses)
        dp = [0]*(n+2)
        for i in range(2, n+2):
            dp[i] = max(dp[i-2] + houses[i-2], dp[i-1])
        return dp[n+1]

    def rob_SpaceOptimized(self, houses: List[int]) -> int:
        prev = 0
        curr = 0
        for i in range(len(houses)):
            new = max(houses[i] + prev, curr)
            prev = curr
            curr = new

        return curr