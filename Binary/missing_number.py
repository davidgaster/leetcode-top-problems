# https://leetcode.com/problems/missing-number/
class Solution:
    '''
    Use an array to set every number that exists to 1
    Loop through and find the missing number
    '''
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = [0]*(len(nums)+1)
        for n in nums:
            all_nums[n] = 1
        
        n = 0
        while n < len(all_nums):
            if all_nums[n] == 0:
                return n
            n += 1
        return n
    '''
    Harness the fact that XOR is its own inverse to find the missing element
    XOR n with every index and value, will be left with the missing number.
    '''
    def alternate_sol(self, nums: List[int]) -> int:
        missing = len(nums)
        for i,n in enumerate(nums):
            missing ^= i ^ n
        return missing
        