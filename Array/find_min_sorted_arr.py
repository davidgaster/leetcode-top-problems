# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        We want to find the position in which nums[i] > nums[i+1]. Then we return nums[i+1].
        We do a modified binary search to determine which half of the array this occurs in.
         0 1 2 3 4 5 6 7
        [3,4,5,6,7,0,1,2]
        --> (7,0) return 0
        lo = 3
        mid = 6
        hi = 2
        (mid+1 <= hi)
        mid > mid+1 --> return mid+1
        '''
        if nums[0] <= nums[-1]: return nums[0]
        
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[lo] > nums[mid]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid
            else:
                return -1 #impossible, array not rotated and sorted
        
        return -1