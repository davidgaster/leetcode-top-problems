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
        if len(intervals) == 1:
            return intervals
                
        intervals.sort()
        output = []
        lo = 0
        while lo < len(intervals):
            hi = lo
            max_end = intervals[hi][1]
            while hi < len(intervals)-1 and max_end >= intervals[hi+1][0]:
                max_end = max(max_end, intervals[hi+1][1])
                hi += 1
            output.append([intervals[lo][0], max_end])
            lo = hi+1
                
        return output