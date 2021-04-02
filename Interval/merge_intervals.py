# https://leetcode.com/problems/merge-intervals/
class Solution(object):
    '''
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an 
    array of the non-overlapping intervals that cover all the intervals in the input.
    '''
    def merge(self, intervals):
        """
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
        
        Determine if 2 intervals are overlapping
        --> keep track of the maximum ending time throughout. avoid a case like this:
        [[1,10],[2,3],[4,5],[6,7],[8,9]]
        ignore all the intervals that have end time less than 10.

        3 cases
        1. Non overlapping
           a [    ]
                    b []
        2. Overlapping
            a [    ]
               b [   ]
        3. Completely contained
            a [     ]
              b [ ]
        """
        if len(intervals) <= 1:
            return intervals
                
        intervals.sort()
        output = []
        currentInterval = intervals[0]
        for i in range(1, len(intervals)):
            
            interval = intervals[i]
            if currentInterval[1] < interval[0]: # before
                output.append(currentInterval)
                currentInterval = intervals[i]
            else: # all other cases
                currentInterval[0] = min(currentInterval[0], interval[0])
                currentInterval[1] = max(currentInterval[1], interval[1])
        output.append(currentInterval)
        return output