# https://leetcode.com/problems/meeting-rooms/
class Solution:
    '''
    Boils down to finding if any of the intervals are overlapping.
    Approach: Sort all intervals
    Check if there exists 2 intervals that are overlapping, if so return False.
    '''
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort()
        for interval1, interval2 in zip(intervals, intervals[1:]):
            if interval2[0] < interval1[1]:
                return False
        return True