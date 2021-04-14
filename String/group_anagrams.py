# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Return a list of lists where all anagrams are grouped together
        [0, 0, 0, ... , 0]
         a  b  c, ... , z
         ord(letter) - ord('a')
        Approach: get the tuple of all counts and store in buckets of 26. append to answer
        '''
        hmap = defaultdict(list)
        for s in strs:
            letters = [0]*26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            hmap[tuple(letters)].append(s)
            
        return [val for _,val in hmap.items()]