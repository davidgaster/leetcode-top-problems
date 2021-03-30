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
    
    Optimization: keep a cache of intermediate results, all the ones that have already been found to
    originate from the pacific/atlantic already will be set to True.
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ret = []
        M,N = len(heights), len(heights[0])
        dirs = [[1,0], [-1,0], [0,-1], [0,1]] # UDLR
        
        can_reach_pacific = [[False for i in range(N)] for j in range(M)]
        can_reach_atlantic = [[False for i in range(N)] for j in range(M)]
        
        def get_pacific(i,j):
            
            if can_reach_pacific[i][j]:
                return
            
            can_reach_pacific[i][j] = True
            
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < M and nj >= 0 and nj < N and heights[ni][nj] >= heights[i][j]:
                    get_pacific(ni,nj)
        
        def get_atlantic(i,j):
            if can_reach_atlantic[i][j]:
                return
            
            can_reach_atlantic[i][j] = True
            
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < M and nj >= 0 and nj < N and heights[ni][nj] >= heights[i][j]:
                    get_atlantic(ni,nj)
        
        for x in range(M):
            get_pacific(x,0)
            get_atlantic(x,N-1)
            
        for y in range(N):
            get_pacific(0,y)
            get_atlantic(M-1,y)
        
        
        for i in range(M):
            for j in range(N):
                if can_reach_atlantic[i][j] and can_reach_pacific[i][j]:
                    ret.append([i,j])
        
        return ret