#take all edges sort them
#if add edges are in in the same disjoint set dont add, continue untill add verticies are visited

from heapq import *

def kruskal(graph):
  djs = DisjointSet()
  edges = []
  h = []
  solution = []
  for key in graph.key():
    for edge in graph[key]:
      heappush(h, (weight(edge), edge))

  for vertex in graph.keys():
    djs.add(vertex)

  #Algorithm
  while h:
    edge = heappop(h)
    if (find(edge[0]) == find(edge[1])): #How to get this
      pass
    else:
      djs.union(edge[0], edge[1])
      solution.append(edge)

  return solution

