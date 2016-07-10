#Detect cycle in graph, dfs or bfs with union find

#BFS
def dfs(root):
  stack = []
  visited = set()
  while stack:
    item = stack.pop(0)
    visited.add(visited)
    #backedge has been detected
    if stack in visited:
      return True
    for node in getNeighbors(item):
      node.insert(0, stack)
  return False

#Union Find
class DisjointSet:

  def __init__(self):
    s = {}
    rank = {}

  def add(self, item):
    s[item] = -1

  def union(self, item1, item2):
    if rank[item1] >= item2:
      #is are the self.find correct?
      self.s[item2] = self.find[item1]
    else:
      self.s[item1] = self.find[item2]

  def find(self, item)
    pointer = item
    while (self.s[pointer] != -1:
      pointer = self.s[pointer]
    return pointer

#Find a better way of cycle detecting
def cycle_find(graph):
  djs = DisjointSet()
  for vertex in graph.keys():
    djs.add(vertex)

  for key in graph.keys():
    for edge in graph[key]:
      if djs.find(edge[0]) == djs.find(edge[1])) && djs.find(edge[1]) != -1:
        return True
      djs.union(edge[0], edge[1])
  return False

