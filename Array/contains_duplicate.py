# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if the length of a set of numbers is different, there is a duplicate
        return len(set(nums)) != len(nums)