class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for course, preReq in prerequisites:
            adjList[course].append(preReq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True

            visited.add(course)
            for preReq in adjList[course]:
                if not dfs(preReq): return False
                visited.remove(course)
                adjList[course] = []
                return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True