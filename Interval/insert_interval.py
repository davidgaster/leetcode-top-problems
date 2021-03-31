# https://leetcode.com/problems/insert-interval/
class Solution:
    '''
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]
    
    the main idea is that when iterating over the intervals there are three cases:

    1. the new interval is in the range of the other interval
    2. the new interval's range is before the other
    3. the new interval is after the range of other interval
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        
        for interval in intervals:
			# the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result