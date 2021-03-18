"""
https://leetcode.com/problems/minimum-cost-for-tickets/

In a country popular for train travel, you have planned some train travelling one year in advance.  
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 
Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
7 day = $7 + 5*$2 = $17

Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000

dp[i] = min # dollars you need to travel every day in list of days up to index i
        1 2 3 4 5 6 7 8 . . . 20
dp = [0 2 4 6 7 7 7 7 9         0
dp[4] = min(8, 7, 15)
dp[5] = min(8, dp[i-6]+7, dp[i-29]+15)
dp[8] = min(dp[i-1]+2, dp[i-6]+7, ) = min(7+2, 4+7,
dp[20] = min(dp[i-1]+2, dp[i-6]+7, 

dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])

"""
def min_travel_dollars(days, costs):
    days_set = set(days)
    n = 365+30+1
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if i in days_set:
            dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
        else:
            dp[i] = dp[i-1]

    return dp[-1]

def mincostTickets(self, days, costs):
        import sys
        import bisect
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n=len(days)
        dp = [sys.maxint] * (1+n)
        dp[0]=0
        idx_to_cost={0:1, 1:7, 2:30}
        
        for i, day in enumerate(days,1):
            for j in range(len(costs)):
                idx = bisect.bisect_right(days, day-idx_to_cost[j])
                # print(i,j,day-d[j], idx)
                dp[i] = min(dp[i], costs[j] + dp[idx])
        
        #print(dp)
        return dp[n]
    
    

if __name__ == "__main__":
    tests = [
        ([1,4,6,7,8,20], [2,7,15]),
        ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]),
        ([1,3,7], [1,4,20]),
        ([1,4,6,7,8,20], [7,2,15])
    ]
    expected = [
        11,
        17,
        3,
        6
    ]
    for i, test in enumerate(tests):
        print('----')
        days = test[0]
        costs = test[1]
        got = min_travel_dollars(days, costs)
        print(f"expected: {expected[i]}, got: {got}")
        assert expected[i] == got
