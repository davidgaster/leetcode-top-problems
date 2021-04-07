from collections import Counter
import heapq
        
class Solution:
    
    '''
    Put all the tasks into buckets. Simulate trying to execute each task
    tasks = ["A","A","A","B","B","B","C","C"], n = 2
    |A|B| |A|B| |A|B|
    Task A has the maximum count of say Mct. So we slot it in spaces
    of (n+1), in this case 3. Since A has to have 2 idle after it.
    So we do this for Mct-1 of the A's. This is all the A's plus idle spots
    up until the last A. And we add 1 after because we need a spot for the last A job.
    
    However, what if there are multiple jobs with Mct. Then we would have to execute those
    jobs all after the last A. So we add the count of all jobs with Mct to that answer.
    This gives us the forumla:

    (Mct-1)*(n+1) + num_Mct  = (2)*(3)+2 = 8
    
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        Mct = 0
        num_Mct = 0
        for _,c in counts.items():
            if c > Mct:
                Mct = c
                num_Mct = 1
            elif c == Mct:
                num_Mct += 1
        
        return max(len(tasks), (Mct-1)*(n+1) + num_Mct)
        
        
    '''
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: 
    A -> B -> idle -> A -> B -> idle -> A -> B
    There is at least 2 units of time between any two same tasks.
    
    Approach: This problem boils down to finding the minimum amount of idle time.
    Greedy--> Always pick the task with the highest count left
    
            (3, A)
            /
         (3, B)
    n = 2
    '''
    def leastIntervalHeap(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        counts = Counter(tasks)
        maxheap = MaxHeap()
        for _,count in counts.items():
            maxheap.push(count)
        
        time = 0
        while not maxheap.isempty():
            
            tasks_done = []
            i = 0
            while not maxheap.isempty() and i <= n:
                task = maxheap.pop()
                time += 1 # execute a task
                tasks_done.append(task-1)
                i += 1
            
            for task in tasks_done:
                if task > 0: maxheap.push(task)
            
            if maxheap.isempty():
                return time
            time += n-i+1
                
        return time
    
class MaxHeap:
    
    def __init__(self):
        self.maxheap = []
    def push(self, item):
        heapq.heappush(self.maxheap, -item)
    def pop(self):
        item = heapq.heappop(self.maxheap)
        return -item
    def isempty(self):
        return len(self.maxheap) == 0