# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    # depth first search from every node
    # every time you encounter a new node, add as a new connected component
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(vertex):
            for u in graph[vertex]:
                if u not in visited:
                    visited.add(u)
                    dfs(u)
        
        visited = set()
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        ans = 0
        for v in range(n):
            if v not in visited:
                visited.add(v)
                dfs(v)
                ans += 1
        
        return ans