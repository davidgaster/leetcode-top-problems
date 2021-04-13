# https://leetcode.com/problems/word-search/
class Solution:
    '''
    Do a depth first search from the letter that matches the first letter in the word.
    Remember, you cannot reuse letters, so make sure that when backtracking, you replace
    the letter with what was their previously.
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, idx):
            if idx >= len(word):
                return True
            
            if r < 0 or c < 0 or r >= n or c >= m or board[r][c] != word[idx]:
                return False
            
            tmp = word[idx]
            board[r][c] = ''
            found = dfs(r+1,c,idx+1) or dfs(r,c+1,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c-1,idx+1)
            if found:
                return True
            board[r][c] = tmp
            
            return False
        
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False