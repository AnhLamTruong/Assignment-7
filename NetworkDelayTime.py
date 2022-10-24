import collections
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #BFS
        edges = collections.defualtdict(list)
        for u,v,w in times:
          edges[u].append((v,w))
        minHeap =[(0,k)]
        visit = set()
        #Leght to visit the node
        t=0
        while minHeap:
          w1,n1=heapq.heappop(minHeap)
          if n1 in visit:
            continue
          visit.add(n1)
          t=max(1,w1)
          for n2,w2 in edges[n1]:
            if n2 not in visit:
              heapq.heappush(minHeap, (w1+w2,n2))
        return t if len(visit)==n else -1
s=Solution()
times1 = [[2,1,1],[2,3,1],[3,4,1]]
n1 = 4 
k1 = 2
times2 = [[1,2,1]]
n2 = 2
k2 = 1
times3 = [[1,2,1]] 
n3 = 2
k3 = 2
print(s.networkDelayTime(times1,n1,k1))
print(s.networkDelayTime(times2,n2,k2))
print(s.networkDelayTime(times3,n3,k3))