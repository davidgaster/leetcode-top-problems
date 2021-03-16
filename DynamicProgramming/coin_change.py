# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coins = [1, 2, 5], amount = 11
        dp[i] = fewest number of coins needed to make up amount i
        coins[0] = 1
              0  1  2  3  4  5  6  7  8  9  10 11
        dp = [0 12 12 12 12 12 12 12 12 12 12 12] 
        dp[0] = 0
        Simulate either taking the current coin, or not taking it. If we take the current coin,
        we would be adding 1 + the min # of coins needed to make up (amount - coin), i.e. dp[a-c]
        '''
        coins.sort()
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for a in range(amount+1):
            for c in coins:
                if c > a:
                    break
                dp[a] = min(dp[a], 1 + dp[a-c] )
                
        return dp[amount] if dp[amount] < amount+1 else -1