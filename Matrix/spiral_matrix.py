# https://leetcode.com/problems/spiral-matrix/
class Solution:
    '''
    1. Keep track of the direction in index i (idx == 0 means Right, 1 means)
    2. Keep track of the bounds in the floor,ceil,left,right var's
    3. If we hit a bound
            Change direction (idx++)
            decrement the bound
            (R --> right-1)
            (D --> ceil-1)
            (L --> left+1)
            (U --> floor+1)
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #          R     D      L     U     
        direc = [[0,1],[1,0],[0,-1],[-1,0]]
        n = len(direc)
        idx = 0
        
        ans = []
        floor, ceil = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        r,c = 0,0
        while floor <= ceil and left <= right:
            
            ans.append(matrix[r][c])
            #print(r,c,ans)
            if idx == 0:   # R
                if c >= right:
                    idx = (idx+1)%n
                    floor += 1
            elif idx == 1: # D
                if r >= ceil:
                    idx = (idx+1)%n
                    right -= 1
            elif idx == 2: # L
                if c <= left:
                    idx = (idx+1)%n
                    ceil -= 1
            elif idx == 3: # U
                if r <= floor:
                    idx = (idx+1)%n
                    left += 1
                
            dx, dy = direc[idx]
            r += dx
            c += dy
        
        return ans