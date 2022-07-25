class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        coursesPre = {}
        
        for p in prerequisites:
            if p[0] not in coursesPre:
                coursesPre[p[0]] = []
            coursesPre[p[0]].append(p[1])
            
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            elif course not in coursesPre or len(coursesPre[course]) == 0:
                return True
            
            visited.add(course)
        
            for c in coursesPre[course]:
                canFinish = dfs(c)
                if not canFinish:
                    return False
            
            visited.remove(course)
            coursesPre[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True