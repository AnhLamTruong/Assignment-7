from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to the prereq list
        preMap ={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
          preMap[crs].append(pre)
        
        #visitSet = all course along the curr DFS path
        visitSet=set()
        def dfs(crs):
          if crs in visitSet:
            return False
          if preMap[crs]==[]:
            return True
          visitSet.add(crs)
          for pre in preMap[crs]:
            if not dfs(pre): return False
          visitSet.remove(crs)
          preMap[crs]=[]
          return True
        
        # 1 -> 2
        # 3 -> 4
        
        for crs in range(numCourses):
          if not dfs(crs):return False
        return True

s=Solution()
prer1=[[0,1],[0,2],[1,3],[1,4],[3,4]]
prer2=[[0,1],[1,2],[2,0]]
prer3=[[1,2],[3,4]]

print(s.canFinish(5,prer1))
print(s.canFinish(3,prer2))
print(s.canFinish(2,prer3))