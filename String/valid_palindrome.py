# https://leetcode.com/problems/valid-palindrome/
class Solution:
    '''
    ignore all alphanumeric char's
    compare first and last c's in string to see if it is a palindrome
    '''
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lo, hi = 0, len(s)-1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            
            if s[lo] != s[hi]: return False
            lo += 1
            hi -= 1
        return True