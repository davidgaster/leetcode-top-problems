# https://leetcode.com/problems/rearrange-string-k-distance-apart/
class Solution:
    '''
    s = aaabbbc, k = 3
    [a b _ a b _ | a b] 
               6  +  2  = 8
    (Mfreq-1)*k + Nct
    
    There are 2 characters with a max freq (Mfreq) of 3.
    n is the length of the string. the # of those characters will fill up
    a total of (Mfreq-1)*k + Nct slots. If this is greater than the length of
    the string, then it is impossible and we return ''.
    Else, we slot all the characters in their respective places in the string, similar to
    the idea from task-scheduler and reorganize string problems.
    '''
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        counts = Counter(s)
        maxf = max(counts.values())
        # math similar to task scheduler of why this works, see comments above
        if (maxf - 1) * k + Counter(counts.values())[maxf] > len(s):
            return ""
        
        n = len(s)
        ans = ['']*n
        i = 0
        sorted_counts = [(count,char) for char,count in counts.items()]
        for count,char in sorted(sorted_counts, reverse=True):
            for _ in range(count):
                ans[i] = char
                i = i + k
                if i >= n:
                    i = (i - 1) % k
        return ''.join(ans)
            
    
    '''
    Heap based approach, add to the end of the string each time by
    polling k characters from the heap with the max count.
    '''
    def rearrangeStringHeap(self, s: str, k: int) -> str:
        
        if k == 0:
            return s
        
        counts = Counter(s)
        maxf = max(counts.values())
        # math similar to task scheduler of why this works, see comments above
        if (maxf - 1) * k + Counter(counts.values())[maxf] > len(s):
            return ""
        
        maxheap = MaxHeap()
        for char,count in counts.items():
            maxheap.push((count,char))
        
        ans = []
        while not maxheap.isempty():
            
            collect_k = []
            i = 0
            while not maxheap.isempty() and i < k:
                count,char = maxheap.pop()
                count -= 1 # execute a task
                collect_k.append((count,char))
                i += 1
            
            ans.extend([x[1] for x in collect_k]) # add the characters to the output
                
            for count,char in collect_k:
                if count > 0: 
                    maxheap.push((count,char))
            
            if maxheap.isempty():
                break
                
        return ''.join(ans)
    
class MaxHeap:
    
    def __init__(self):
        self.maxheap = []
    def push(self, item):
        heapq.heappush(self.maxheap, (-item[0],item[1]))
    def pop(self):
        item = heapq.heappop(self.maxheap)
        return (-item[0],item[1])
    def isempty(self):
        return len(self.maxheap) == 0