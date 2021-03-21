# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    
    def __init__(self):
        self.visited = {}
    '''
     1 -- 2
     |    |
     4 -- 3
     
     [3]
     
     1 -- 2
     |    |
     4    3
     
     visited
     {
         1: 1
         2: 2
         3: 3
         4: 4
     }
     1. perform bfs/dfs
     2. for all unvisited neighbors, create new neighbors
     3. add neighbor on both sides
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        self.visited[node] = Node(node.val, [])
        self.cloneGraphDFS(node)
        return self.visited[node]

    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        
        queue = deque([node])
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in self.visited:
                    self.visited[neighbor] = Node(neighbor.val, [])
                    queue.appendleft(neighbor)
                self.visited[curr].neighbors.append(self.visited[neighbor])
                            
    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        
        for neighbor in node.neighbors:
            if neighbor not in self.visited:
                self.visited[neighbor] = Node(neighbor.val, [])
                self.cloneGraph(neighbor)
            self.visited[node].neighbors.append(self.visited[neighbor])
                
                