# https://leetcode.com/problems/number-of-islands/
class Solution:
    '''
    Classic number of islands problem using a depth first search
    Search 4-directionally wherever there is a "1", marking the spaces you
    visit with a "0" when you visit them.
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
                
        return islands