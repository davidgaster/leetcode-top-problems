# https://leetcode.com/problems/word-search-ii/
class TrieNode:
    def __init__(self, word=None):
        self.letters = {}
        self.word = word

class Solution:
    '''
    Create a Trie of all words in the dictionary, if the letter in the board
    currently exists during traversal of the trie, then continue on. Store the actual
    words IN the Trie, so that when we find a word, we can safely add it to
    the final output list.
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def helper(trienode, r, c):
            letter = board[r][c]
            if letter == '*' or letter not in trienode.letters:
                return
            
            node = trienode.letters[letter]
            if node.word:
                output.append(node.word)
                node.word = None
                
            board[r][c] = '*'
            if r-1 >= 0: helper(node, r-1, c)
            if c-1 >= 0: helper(node, r, c-1)
            if r+1 < len(board): helper(node, r+1, c)
            if c+1 < len(board[r]): helper(node, r, c+1)
            board[r][c] = letter

            
        if not board or not words: return []
        
        root = TrieNode()
        for word in words:
            trienode = root
            for c in word:
                if c not in trienode.letters:
                    trienode.letters[c] = TrieNode()
                trienode = trienode.letters[c]
            trienode.word = word
            
        output = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] in root.letters:
                    helper(root, i, j)
        
        return output