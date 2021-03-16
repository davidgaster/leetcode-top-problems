# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    # [1, 2, 3, 4]
    # left product = [1,  1, 2, 6]
    # right product =  [24, 12, 4, 1]
    # prod = 1
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # find the left product of all elements in the array so far
        # going from left --> right
        # find the right product of all elments in the array so far
        # going from left <-- right
        # product of array except self is the product of two elements in these arrays.
        left_product = []
        prod = 1
        for num in nums:
            left_product.append(prod)
            prod *= num
        
        ans = [1]*len(nums)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = prod*left_product[i]
            prod *= nums[i]
            
        return ans