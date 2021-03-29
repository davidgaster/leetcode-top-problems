# https://leetcode.com/problems/insert-interval/
class Solution:
    '''
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]
    
    startTime = newInterval[0]
    endTime = newInterval[1]
    if startTime <= intervals[i][1]:
    
    1. Find first end time which is greater than or equal to the insert interval's start time
    2. Find the last start time which is less than or equal to the insert interval's end time
    
    [[1,5], [8,9]], [2,7]
    [[1,7], [8,9]]
    
    if insert end time is less than start time. then make previous intervals end time = end time
    if insert end time is less than current end time. stop
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        new_start, new_end = newInterval
        for i, (start, end) in enumerate(intervals):
            
            # no overlap and new interval appears before current interval
            if start > new_end:
                ans.append([new_start, new_end])
                new_start, new_end = intervals[i]
            # overlap, update the merged interval
            elif end >= new_start:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
            # no overlap
            else:
                ans.append(intervals[i])
                
        ans.append([new_start, new_end])
        return ans