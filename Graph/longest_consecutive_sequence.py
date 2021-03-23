# https://leetcode.com/problems/longest-consecutive-sequence/
from collections import deque
class Solution:
    '''
    [100,4,200,1,3,2]
    100
    
    200
    
    4 -- 3
         |
         |
    1 -- 2
    
    {
     100: [],
     200: [],
     4: [3],
     3: [2, 4],
     2: [1]
     1: [2]
    }
    
    Approach: Traverse through the array and build an undirected graph where to nodes are connected if they are of
    distance 1 from eachother, i.e. 4 and 3 are connected.
    Traverse every node in the graph once more, and the longest traversal is the longest sequence of nums in a row.
    
    Improvement: we don't need an entire graph, just a set. From each number we can try to traverse forward/backward
    from the numbers in the set. Sets have O(1) lookup, so this would still be an O(N) time complexity
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        
        graph = {}
        for num in nums:
            if num not in graph:
                graph[num] = []
            for i in [-1, 1]:
                x = num + i
                if x in graph:
                    graph[x].append(num)
                    graph[num].append(x)
        
        max_count = 0
        visited = set()
        for node in graph:
            
            if node in visited: continue
            
            # count distance all the way to lowest element
            curr = node
            count = 0
            while curr-1 in graph[curr]:
                visited.add(curr)
                count += 1
                curr = curr-1
            
            # count distance all the way to highest element
            curr = node
            while curr+1 in graph[curr]:
                visited.add(curr)
                count += 1
                curr = curr+1
            
            # take total count + 1 (the starting num)
            max_count = max(max_count, count+1)
            
            
        return max_count    

    '''
    Alternate solution: Use union find using disjoint sets!
    Each num is in the same set if they are connected to num-1, num+1 element.
    Find parents and join them together
    '''
    def union_find(self, nums: List[int]) -> int:
        
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i,j):
            pi, pj = find(i), find(j)
            if pi != pj:
                if rank[pi] >= pj:
                    parent[pj] = pi
                    rank[pi] += 1
                else:
                    parent[pi] = pj
                    rank[pj] += 1
        
        if not nums:
            return 0
        
        # first pass is initialize parent and rank for all num in nums
        parent, rank, nums = {}, {}, set(nums)
        for num in nums: # init
            parent[num] = num
            rank[num] = 0
            
        # second pass: union nums[i] with nums[i]-1 and nums[i]+1 if ums[i]-1 and nums[i]+1 in nums
        for num in nums:
            if num-1 in nums:
                union(num-1, num)
            if num+1 in nums:
                union(num+1, num)
                    
        # second pass find numbers under the same parent
        d = collections.defaultdict(list)
        for num in nums:
            d[find(num)].append(num)
        return max([len(l) for l in d.values()])
        
        
    