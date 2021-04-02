# https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    '''
    Also known as Interval Scheduling Maximization. This is a Greedy solution. Approach:
    Sort all intervals by the END time.
    Pick the interval with the earliest end time, and remove all the intervals that are conflicting with this end time.
    
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
    
    You may assume the interval's end point is always bigger than its start point.
    Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
        
        
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x : x[1])
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end: # delete this interval as it is conflicting
                count += 1
            else:
                end = intervals[i][1] # update the next earliest end time
                
        return count
            