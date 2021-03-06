class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Dynamic programming:
        Keep track of local max and global max
        At every step, local max is max of current element alone, or current element + local max
        global max is max of global and local max
        
        ''' 
        local_max = global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(global_max, local_max)
            
        return global_max
        