# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp[i] = max money you can rob up to house i
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        [1 8 3 1 4]
        [1 8 8 9 12]
        The problem reduces down to max between the original house robber problem for the
        1 ... n-1 houses   and
        2 ... n-2 houses
        '''
        if len(nums) <= 3:
            return max(nums)
        
        n = len(nums)
        dp = [0]*(n+2)
        ans = 0
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        
        ans = dp[-2]
        dp = [0]*(n+2)
        for i in range(3, n+2):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
            
        return max(ans, dp[-1])