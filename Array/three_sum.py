class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort the array, then have 3 pointers for an O(N^2) approach.
        [-4, -1, -1, 0, 1, 2]
        i = low element
        j = mid element that iterates through
        k = hi element
        If the sum of the 3 elements is less than 0, increment j, if greater, decrement k,
        otherwise add it in.
        '''
        ans_set = []
        nums.sort()
        for i in range(len(nums)):
            
            if i == 0 or nums[i-1] != nums[i]:
                j = i+1
                k = len(nums)-1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        ans_set.append([nums[i],nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j-1] == nums[j]:
                            j += 1
        
        return ans_set
        