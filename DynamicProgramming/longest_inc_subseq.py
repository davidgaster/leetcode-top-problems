class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The LIS is [2,3,7,101], therefore the length is 4.
        dp[i] = longest increasing subsequence up to index i
        dp  = [ 1, 1, 1, 1, 1, 1,   1,  1]
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        '''
        dp = [1]*len(nums)
        ans = 1
        for i in range(len(dp)):
            for j in range(i):
                # check if any previous nums are less, and find the max LIS from there
                # it is either 1 + the LIS of that position or, the current LIS
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
                    ans = max(dp[i], ans)
        
        return ans