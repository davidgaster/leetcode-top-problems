# https://leetcode.com/problems/word-break/
class Solution(object):
    
    '''
    Recursion using memoization
    Loop through the string and check if the substring up to index i is a word in the
    word dict. If so, break the string and recurse on the remainder of the string.
    Continue recursion until you get to a string that is itself in the wordDict.
    If you reach out of the for loop, you know that combination did not work, so you add it to
    memo set to not recurse on it later again.
    '''
    def wordBreak(self, s, wordDict):
        return self.helper(s, set(wordDict), set())
        
    def helper(self, s, wordDictSet, memo):
        if s in memo:
            return False
        
        if s in wordDictSet:
            return True
        
        for i in range(1,len(s)+1):
            word = s[:i]
            if word in wordDictSet:
                rest = s[i:]
                if self.helper(rest, wordDictSet, memo):
                    return True
        
        memo.add(s)
        return False


    '''
    Dynamic Programming
    dp[i] represents whether s[:i] can be broken up into words
    wordDict = ["leet", "code"]
    s  =    l e e t c o d e
    dp = [T F F F F F F F F]
    If the previous ending index of the string (j) is True, it means 
    a word was successfully broken up to that point. Then, check if 
    the next string up from s[j:i] is also a word, if so
    we mark its ENDing index (i) as True
    '''
    def wordBreakDP(self, s, wordDict):
        
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        wordDictSet = set(wordDict)
        
        for i in range(1, n+1):
            for j in range(i):
                
                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True
        
        return dp[n]
        
        
        
        