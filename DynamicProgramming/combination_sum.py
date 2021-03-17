# https://leetcode.com/problems/combination-sum-iv/
from collections import defaultdict
class Solution:
    '''
    Top-Down Dynamic Programming
    nums = [1,2,3], target = 4
    Starting with a target of 4, we pick a number of [1, 2, 3] and recurse on the remaining sum (target-num).
    If we hit to a value of 0, we have found a way of combining numbers to meet this sum and return 1 as a possibility.
    If less than 0, this is not a way to sum to target, so we return 0.
    Make use of memoization to cache intermediate results.
    '''
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = defaultdict(int)
        return self.helper(nums, target, memo)
    
    def helper(self, nums, target, memo):
        if target in memo:
            return memo[target]
        
        if target == 0:
            return 1
        
        if target < 0:
            return 0
        
        for num in nums:
            memo[target] += self.helper(nums, target-num, memo)
        
        return memo[target]

    '''
    Bottom-Up Dynamic Programming
    dp[t] = # of combinations to sum nums up to sum t
    answer will be dp[target]
    
    At each step, you choose a number num and simulate using it as part of your
    sum up to target. lets say your target is 4, and you are using 2 in your sum, then
    the total number of combinations you can make up the sum by using 2 in your sum is located at
    dp[4-2] in the dynamic programming array. We add this to the answer
    '''
    def combinationSum4DP(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        print(dp)
        for t in range(target+1):
            for num in nums:
                if num > t:
                    break
                dp[t] += dp[t - num]
                print(dp)
            print('----------')
                
        
        return dp[target]