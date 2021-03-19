# https://leetcode.com/problems/decode-ways/
class Solution:
    '''
    Top Down Dynamic Programing
    Take the original string-
    1. Check first and second character, check if this substring can be mapped as a letter either
       from 10 - 19 or 20 - 26
    2. If so, recurse on both cases (a single character and a double character)
    3. If the starting string is a "0", it can't be decoded
    '''
    def numDecodings(self, s: str) -> int:
        return self.helper(s, {})
    
    def helper(self, s, memo):
        
        if s in memo:
            return memo[s]
        
        if len(s) == 0:
            return 1
        
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            return 1
        
        if (s[0] == "1" and "0" <= s[1] <= "9") or (s[0] == "2" and "0" <= s[1] <= "6"):
            memo[s] = self.helper(s[1:], memo) + self.helper(s[2:], memo)
        else:
            memo[s] = self.helper(s[1:], memo)       
        
        return memo[s]