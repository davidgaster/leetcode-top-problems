# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    '''
    store a dictionary of <char, idx>
    loop through the string, and every time we see a character, put its
    index in the dictionary
    s = dvdf
    indices = {
        d: 0,
        v: 1
    }
    prev = 1
    ans = 1 - 0 + 1 = 2
    ""
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        seen = {}
        ans, prev = 0, 0
        for i,c in enumerate(s):
            if c in seen and prev <= seen[c]: # s = tmmfdtf. this check makes sure not to update pointer on 2nd 't'
                prev = seen[c]+1
            else:
                ans = max(ans, i - prev + 1)
            seen[c] = i
        
        return ans
        
