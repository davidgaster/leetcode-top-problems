# https://leetcode.com/problems/valid-anagram/
from collections import Counter, defaultdict
class Solution:
    '''
    Anagrams have the same count of characters in both strings
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for c in s:
            count_s[c] += 1
        for c in t:
            count_t[c] += 1
        
        for c in count_s:
            if c not in count_t or count_t[c] != count_s[c]:
                return False
        
        return True
        
        # simplest answer
        # return Counter(s) == Counter(t)