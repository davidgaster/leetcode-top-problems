# https://leetcode.com/problems/container-with-most-water/
class Solution:
    '''
    2 pointer approach.
    At each step, keep the bar with the larger height
    Keep track of the max area seen overall
    '''
    def maxArea(self, height: List[int]) -> int:
        lo = 0
        hi = len(height)-1
        area = 0
        while lo < hi:
            area = max(area, (hi - lo)*min(height[hi], height[lo]))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return area