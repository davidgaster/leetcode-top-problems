class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        We can only buy and sell once. 
        We simply find the minimum price in the array
        and the maximum price occuring after, and take that difference.
        We can do this by substracting the current price - min_price and keep track of previous max.
        '''
        if not prices: return 0
        
        max_profit = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
            
        return max_profit
        