# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Starting at the end of the array, we want to see if it was possible to get there from
        a previous jump. If so, that means the current pos + its max jump would have landed
        us on the previous square. Thus, we update the end to that square.
        At the end, if it was possible then we would be at index 0.
        '''
        end = nums[-1]
        pos = len(nums)-1
        while pos >= 0:
            if pos + nums[pos] >= end:
                end = pos
            pos -= 1
            
        return end == 0
    