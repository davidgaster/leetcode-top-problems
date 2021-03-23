# https://leetcode.com/problems/alien-dictionary/
from collections import defaultdict, deque
class Solution:
    
    '''
    compare each letter of each word pairwise.
    the first letter that is not matching comes next in the language
    construct a directed graph where each letter is a vertex and one vertex is
    connected to another if it comes earlier in the language
    
    if there is a cycle, invalid
    [wertf, wer] --> invalid
    '''
    def alienOrder(self, words: List[str]) -> str:
        
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for word1, word2 in zip(words, words[1:]):
            
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for c1, c2 in zip(word1, word2):
                
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break # when you find an unmatching character must break and go to the next word
                            
        ans = []
        queue = deque( [c for c in indegree if indegree[c] == 0] )
        while queue:
            c1 = queue.popleft()
            ans.append(c1)
            for c2 in graph[c1]:
                indegree[c2] -= 1
                if indegree[c2] == 0:
                    queue.append(c2)
        
        # if there is a cycle it means we didnt visit everything and thus len(ans) would be different
        return "".join(ans) if len(ans) == len(indegree) else "" 