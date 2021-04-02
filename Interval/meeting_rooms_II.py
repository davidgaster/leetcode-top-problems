import heapq
# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    
    '''
    order heap by ending time
    if start time of next interval is less than
    end time of previous interval, add to heap
    answer is the max size of the heap during the loop
    
    [[4, 19], [4, 25], [19, 26], [19, 28], [26, 29]]
    
    19 > 4
            19
          25
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 1: return 1
        
        intervals.sort()
        heap = []
        heapq.heappush(heap, intervals[0][1])
        max_rooms = 1
        for i in range(1, len(intervals)):
            
            start = intervals[i][0]
            if heap and heap[0] > start:
                heapq.heappush(heap, intervals[i][1])
                max_rooms = max(max_rooms, len(heap))
            else:
                while heap and heap[0] <= start:
                    heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
        return max_rooms
                    