# https://leetcode.com/problems/frog-jump/
class Solution:
    '''
    Input: stones = [0,1,3,5,6,8,12,17]
    Output: true
    Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd 
    stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 
    8th stone.
    
    jump = 1
    stone = 0
    memo = set() --> caches all the positions that were unable to reach the end
    '''
    def canCross(self, stones: List[int]) -> bool:
        finish = stones[-1]
        stones = set(stones)
        return self.canCrossDP(stones, 0, 0, finish, set())
    
    def canCrossDP(self, stones, stone, k, finish, memo):
                
        if stone not in stones: return False
        if k < 0: return False
        if (k, stone) in memo:  return False
        
        if stone == finish: return True
        
        for jump in [k+1, k, k-1]:
            if jump > 0 and self.canCrossDP(stones, stone+jump, jump, finish, memo):
                return True
        
        memo.add((k,stone))
        return False