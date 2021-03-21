# https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    '''
    Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
          
    1. Start at the edge of the atlantc ocean, depth first search going from cells that
    have equal or greater height.
    2. When you hit a cell that can no longer be explored further, stop
    3. Start at edges of pacific ocean, do the same procedure and if you find a position
    already explored in parts 1-2, add this to your answer.
    '''
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        def dfs(r, c, prev, visited):
            
            if r < 0 or c < 0 or r >= m or c >= n or (r,c) in visited or matrix[r][c] < prev:
                return
            
            curr = matrix[r][c]
            visited.add((r, c))
            dfs(r-1, c, curr, visited)
            dfs(r+1, c, curr, visited)
            dfs(r, c-1, curr, visited)
            dfs(r, c+1, curr, visited)
                    
        if not matrix:
            return []
        
        atlantic = set()
        pacific = set()
        
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            dfs(i, n-1, -1, atlantic)
            dfs(i, 0, -1, pacific)
        
        for i in range(n):
            dfs(m-1, i, -1, atlantic)
            dfs(0, i, -1, pacific)
        
        return list(filter(lambda x: x in atlantic, pacific))