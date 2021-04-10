# https://leetcode.com/problems/word-break/
class Solution(object):                   
    '''
    Using recursion with memoization. Cache previously returned function calls
    in a set, where we have already computed if the substring can be broken down.
    Return out of the recursion early if it has already been computed.
    O(N^2) = size of recursion tree can go up to N^2, the length of each string
             is of length N, every time we check the dictionary for substrings
    Thus, final runtime is O(N^3)
    '''
    def wordBreak(self, s, wordDict):
        
        def helper(s):
            
            if s in memo:
                return False
            
            if s in wordDict or s == "":
                return True
            
            for i in range(1, len(s)+1):
                start = s[:i]
                if start in wordDict and helper(s[i:]):
                    return True
            
            memo.add(s)
            return False
        
        wordDict = set(wordDict)
        memo = set()
        return helper(s)
        
       
    '''
    Using Bottom Up Dynamic Programming
    dp[i] represents whether s[:i] can be broken up into words
    wordDict = ["leet", "code"]
    s  =    l e e t c o d e
    dp = [T F F F F F F F F]
    If the previous ending index of the string (j) is True, it means 
    a word was successfully broken up to that point. Then, check if 
    the next string up from s[j:i] is also a word, if so
    we previously marked its ENDing index (i) as True
    '''
    def bottomUpDP(self, s, wordDict):
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        wordDictSet = set(wordDict)

        for i in range(1, n+1):
            for j in range(i):

                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True

        return dp[n]
        
        
    '''
    Using a Trie and Bottom-Up dynamic programming.
    O(N^2) solution
    dp[i][j] = substr from i to j is a word in the dict
    leetcode [leet, code]
    ex: we are at the 'c' and leet is a word
    0 1 2 3 
    h i m e
    h    dp[0][1] = F
    hi   dp[0][2] = T
    i    dp[1][2] = F
    him  dp[0][3] = F
    im   dp[1][3] = F
    m    dp[2][3] = F
    hime dp[0][4] = T
    ime  dp[1][4] = F
    me   dp[2][4] = F
    e    dp[3][4] = F
    '''
    def bottomUpDPwithTrie(self, s, wordDict):
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and trie.isWord(s[j:i]):
                    dp[i] = True
        return dp[n] 
'''
How can we improve this solution from O(N^3) to O(N^2)?
We can build a Trie out of the word dictionary.
Create a dp[i][j] array where dp[i][j] denotes
whether the substr from i up to j is a word in the dict or not.
Maintain a Trie that during nested for loop, we traverse to see if the
word exists in the tree and mark it as True/False.
'''
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.chars[ord(c)-ord('a')] is None:
                curr.chars[ord(c)-ord('a')] = TrieNode(c)
            curr = curr.chars[ord(c)-ord('a')]
            
            if i == len(word)-1:
                curr.isWord = True
        
    def isWord(self, word):
        curr = self.root
        for c in word:
            if curr.chars[ord(c)-ord('a')] is None:
                return False
            curr = curr.chars[ord(c)-ord('a')]
        
        return curr.isWord
    
    
class TrieNode:
    def __init__(self, c='', isWord=False):
        self.chars = [None]*26
        self.isWord = isWord        