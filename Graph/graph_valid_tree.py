# https://leetcode.com/problems/graph-valid-tree/
from collections import defaultdict
class Solution:
    '''
    Boils down to finding a cycle in the graph. If there is no cycle, then it is a tree.
    Do a DFS on the graph and make sure its not possible to visit any node twice.
    Since the graph is undirected make sure that you don't check for the parent of where you came from.
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        
        adj_list = defaultdict(list)
        for v, u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        
        visited = set()
        return self.is_tree(0, -1, adj_list, visited) and len(visited) == n
    
    def is_tree(self, node, parent, adj_list, visited):
        
        if node in visited:
            return False
        
        visited.add(node)
        for neighbor in adj_list[node]:
            
            if neighbor == parent: continue
                
            if not self.is_tree(neighbor, node, adj_list, visited):
                return False
        
        return True