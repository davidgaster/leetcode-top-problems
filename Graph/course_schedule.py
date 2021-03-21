# https://leetcode.com/problems/course-schedule/
from collections import defaultdict, deque
class Solution:
    '''
    Courses can be represented as a graph and the problem boils down to if
    there exists a cycle in the graph.
    1. Build graph and keep track of indegree of every node
    2. BFS on the graph and 'take' a course decrement the indegree of the next node
    3. If all prereqs are taken (indegree == 0), add to BFS queue
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = {n:0 for n in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        sources = deque([n for n in indegree if indegree[n] == 0])
        taken = 0
        while sources:
            course = sources.popleft()
            taken += 1
            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    sources.append(nextCourse)
        
        # if all courses are taken it is valid
        return taken == numCourses
            
        