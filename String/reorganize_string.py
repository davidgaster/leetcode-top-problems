# https://leetcode.com/problems/reorganize-string/
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        # s = aabbcaa
        # n = 6
        # list = [a _ a _ a _ a]
        # num of a's here can be at most (N+1)/2
        # if any character's count is greater than that, we fail and return ''
        # so the solution is to find the char with max count
        # slot it in positions 0,2,4,6,...
        # then continue putting characters of distance 2 to the end of the string
        # then put all remaining char's in 1,3,5,...
        if not S:
            return ""
        
        n = len(S)
        res = ['']*n
        
        counter = Counter(S)
        counts = [(count,char) for char, count in counter.items()]
        counts.sort(reverse=True)
        
        max_count, max_char = counts[0]
        if max_count > (n+1)/2: return ''
        
        idx = 0
        for x in range(max_count):
            res[idx] = max_char
            idx += 2
        
        for i in range(1,len(counts)):
            count, char = counts[i]
            for j in range(count):
                if idx >= n: idx = 1
                res[idx] = char
                idx += 2
            
        return ''.join(res)
    
    '''
    Use a MaxHeap that also keeps character count. 
    Poll from the heap, place each character at least 2 positions away from each other.
    Very similar to the above solution, just using a heap instead.
    '''
    def reorganizeStringMaxHeap(self, S: str) -> str:
        counter = Counter(S)
        maxheap = MaxHeap()
        N = len(S)
        for char,count in counter.items():
            if count > (N+1) / 2:
                return ''
            
            maxheap.push((count,char))
        
        res = ['']*N
        idx = 0
        while not maxheap.empty():
            count, char = maxheap.pop()
            for _ in range(count):
                if idx >= N:
                    idx = 1
                res[idx] = char
                idx += 2
        return ''.join(res)
        
class MaxHeap:
    
    def __init__(self):
        self.maxheap = []
    
    def empty(self):
        return len(self.maxheap) == 0
    
    def push(self, item):
        count, char = item
        heapq.heappush(self.maxheap, (-count,char))
    
    def pop(self):
        count, char = heapq.heappop(self.maxheap)
        return (-count, char)
    
    def top(self):
        count, char = self.maxheap[0]
        return (-count, char)