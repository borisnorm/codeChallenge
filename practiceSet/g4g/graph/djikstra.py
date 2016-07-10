#Implement djikstra and A start
from heapq import *

def find_min(dist):
  min

def d_stra(source, graph):
  size = len(graph.keys())
  #Visited does not matter, if you iterate all of the time and improve
  visited = set()
  h = []
  heappush(h, (0, source))

  #Distance declaration
  distance = {}
  for key in graph.keys():
    distance[key] = Math.MAX_INTEGER
  distance[source] = 0

  #Alg
  #Start with source, for each neighbor
  while len(visit) < size:
    item = h.pop()
    if item not in visited:
      visited.add(item):
      for node in getNeighbors(item):
        if distance(source, item) + distance(item, node) < distance(source, node):
          distance[target] = distance(source, item) + distance(item, node)
        heappush(h, (distance[node], node))


#A - star modification, a greedy dfs?
def a_star(source, target, graph):
  size = len(graph.keys())

  distance = {}
  for key in graph.keys():
    distance[key] = Math.MAX_INTEGER
  distance[source] = 0

  visited = set()
  h = []
  heappush(h, (0, source))

  while len(visit) < size:
    item = h.pop()
    if item not in visited:
      if item == target:
        return True
      visited.add(item)
      for node in getNeighbors(item):
        heappush(h, (distance(source, item) + distance(item, node) + heur(node, target)

  return False
