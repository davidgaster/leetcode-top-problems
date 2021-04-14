# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    '''
    Same as longest palindromic substring but instead you count if you were able to expand around center
    '''
    def countSubstrings(self, s: str) -> int:
        
        def expandAroundCenter(l, r):
            ans = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]: 
                    break
                l -= 1
                r += 1
                ans += 1
                
            return ans
        
        palindromes = 0
        for i in range(0, len(s)):
            palindromes += expandAroundCenter(i, i)
            palindromes += expandAroundCenter(i, i+1)
        
        return palindromes