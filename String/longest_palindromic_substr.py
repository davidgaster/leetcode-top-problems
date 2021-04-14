# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    '''
    Expand around the center.
    Loop through the string and keep expand from the center as far as you can go.
    Return the length you have expanded so far.
    Note you have to expand around a single char (odd length) and two char's (even length)
    '''
    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            return (l, r)
        
        longest = 1
        max_l, max_r = 0, 1
        for i in range(0, len(s)-1):
            l, r = expandAroundCenter(i, i)
            if r-l > longest:
                longest, max_l, max_r = r-l, l, r
            
            l, r = expandAroundCenter(i, i+1)
            if r-l > longest:
                longest, max_l, max_r = r-l, l, r
        
        return s[max_l:max_r]