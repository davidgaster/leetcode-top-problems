class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        You have 2 situations (forget about 0's for a second). 
        First scenario: you have even number of negative numbers. Then - the solutions is whole array. 
        Second scenario: you have odd number of negative numbers. Then - the solutions starts from left 
        till the last negiative number or the other way around.
        Now, think about 0's. They are nothing different than just start of an array, 
        and you don't have to think about them at all
        nums =          [2, 3, -2, 4]
        left_product =  [2, 6, -12, -48]
        right_product = [-48, -24, -8, 4]
        ans = 6
        '''
        max_prod = float('-inf')
        product = 1
        for num in nums:
            product *= num
            max_prod = max(product, max_prod)
            if product == 0:
                product = 1
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product *= nums[i]
            max_prod = max(product, max_prod)
            if product == 0:
                product = 1
        
        return max_prod