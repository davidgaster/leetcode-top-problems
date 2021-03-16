# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        store the number and its index into a map
        when encountering each new number, to check if there exists any other number that adds to the target,
        we check if (target - num) exists already in the hashmap.
        If so, return the indices of the two nums
        '''
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [i, hashmap[target - num]]
            else:
                hashmap[num] = i
                
        return []